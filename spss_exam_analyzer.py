#!/usr/bin/env python3
"""Compute SPSS-exam statistics from CSV/XLSX/SAV data.

Outputs JSON so the agent can turn exact results into Chinese exam wording.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats


def load_data(path: str, sheet: str | None = None) -> tuple[pd.DataFrame, dict]:
    file_path = Path(path)
    suffix = file_path.suffix.lower()
    meta: dict = {"file": str(file_path), "format": suffix.lstrip(".")}
    if suffix == ".csv":
        df = pd.read_csv(file_path)
    elif suffix in {".xlsx", ".xls"}:
        df = pd.read_excel(file_path, sheet_name=sheet or 0)
        meta["sheet"] = sheet or 0
    elif suffix == ".sav":
        try:
            import pyreadstat
        except ImportError as exc:
            raise SystemExit("pyreadstat is required for .sav files") from exc
        df, sav_meta = pyreadstat.read_sav(file_path, apply_value_formats=False)
        meta["variable_labels"] = getattr(sav_meta, "column_labels", None)
        meta["value_labels"] = getattr(sav_meta, "variable_value_labels", None)
    else:
        raise SystemExit(f"Unsupported file type: {suffix}")
    return df, meta


def clean(df: pd.DataFrame, variables: list[str]) -> pd.DataFrame:
    missing = [v for v in variables if v not in df.columns]
    if missing:
        raise SystemExit(f"Missing variables: {', '.join(missing)}")
    return df[variables].dropna()


def as_numeric(series: pd.Series, name: str) -> pd.Series:
    values = pd.to_numeric(series, errors="coerce")
    if values.notna().sum() == 0:
        raise SystemExit(f"Variable is not numeric: {name}")
    return values


def round_float(value):
    if value is None:
        return None
    try:
        if pd.isna(value):
            return None
    except TypeError:
        pass
    if isinstance(value, (np.integer, int)):
        return int(value)
    if isinstance(value, (np.floating, float)):
        number = float(value)
        if number != 0 and abs(number) < 0.000001:
            return number
        return round(number, 6)
    return value


def jsonify(obj):
    if isinstance(obj, dict):
        return {str(k): jsonify(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [jsonify(v) for v in obj]
    return round_float(obj)


def audit(df: pd.DataFrame, meta: dict) -> dict:
    columns = []
    for col in df.columns:
        s = df[col]
        numeric = pd.to_numeric(s, errors="coerce")
        columns.append(
            {
                "name": col,
                "dtype": str(s.dtype),
                "n": int(s.shape[0]),
                "missing": int(s.isna().sum()),
                "unique": int(s.nunique(dropna=True)),
                "numeric_nonmissing": int(numeric.notna().sum()),
                "min": numeric.min() if numeric.notna().any() else None,
                "max": numeric.max() if numeric.notna().any() else None,
                "sample_values": [round_float(v) for v in s.dropna().unique()[:8].tolist()],
            }
        )
    return {"analysis": "audit", "meta": meta, "rows": int(len(df)), "columns": columns}


def descriptive(df: pd.DataFrame, variables: list[str]) -> dict:
    out = {"analysis": "descriptive", "variables": {}}
    for var in variables:
        s = df[var]
        numeric = pd.to_numeric(s, errors="coerce")
        item = {
            "n": int(s.notna().sum()),
            "missing": int(s.isna().sum()),
            "unique": int(s.nunique(dropna=True)),
            "frequencies": s.value_counts(dropna=False).head(20).to_dict(),
        }
        if numeric.notna().sum() > 0:
            item.update(
                {
                    "mean": numeric.mean(),
                    "std": numeric.std(ddof=1),
                    "median": numeric.median(),
                    "min": numeric.min(),
                    "max": numeric.max(),
                }
            )
        out["variables"][var] = item
    return out


def chi_square(df: pd.DataFrame, iv: str, dv: str) -> dict:
    data = clean(df, [iv, dv])
    table = pd.crosstab(data[iv], data[dv])
    chi2, p, dof, expected = stats.chi2_contingency(table)
    n = int(table.to_numpy().sum())
    r, c = table.shape
    phi_cramer = math.sqrt(chi2 / (n * max(1, min(r - 1, c - 1)))) if n else None
    low_expected = int((expected < 5).sum())
    total_cells = int(expected.size)
    return {
        "analysis": "chi-square",
        "iv": iv,
        "dv": dv,
        "n": n,
        "observed": table.to_dict(),
        "chi_square": chi2,
        "df": int(dof),
        "p": p,
        "cramers_v_or_phi": phi_cramer,
        "expected_min": expected.min(),
        "expected_cells_lt5": low_expected,
        "expected_cells_total": total_cells,
        "expected_lt5_percent": low_expected / total_cells if total_cells else None,
    }


def anova(df: pd.DataFrame, iv: str, dv: str) -> dict:
    data = clean(df, [iv, dv]).copy()
    data[dv] = as_numeric(data[dv], dv)
    groups = []
    descriptives = {}
    for name, group in data.groupby(iv, dropna=True):
        vals = group[dv].dropna()
        if len(vals) > 0:
            groups.append(vals)
            descriptives[str(name)] = {
                "n": int(len(vals)),
                "mean": vals.mean(),
                "std": vals.std(ddof=1),
                "min": vals.min(),
                "max": vals.max(),
            }
    if len(groups) < 2:
        raise SystemExit("ANOVA requires at least two non-empty groups")
    f_stat, p = stats.f_oneway(*groups)
    lev_stat, lev_p = stats.levene(*groups, center="median")
    grand = data[dv].mean()
    ss_between = sum(len(g) * (g.mean() - grand) ** 2 for g in groups)
    ss_total = sum((data[dv] - grand) ** 2)
    eta_sq = ss_between / ss_total if ss_total else None
    return {
        "analysis": "anova",
        "iv": iv,
        "dv": dv,
        "n": int(data[dv].notna().sum()),
        "groups": descriptives,
        "f": f_stat,
        "df_between": len(groups) - 1,
        "df_within": int(sum(len(g) for g in groups) - len(groups)),
        "p": p,
        "levene_stat": lev_stat,
        "levene_p": lev_p,
        "eta_squared": eta_sq,
    }


def correlation(df: pd.DataFrame, x: str, y: str, method: str) -> dict:
    data = clean(df, [x, y]).copy()
    xs = as_numeric(data[x], x)
    ys = as_numeric(data[y], y)
    if method == "spearman":
        coef, p = stats.spearmanr(xs, ys)
        label = "spearman"
    else:
        coef, p = stats.pearsonr(xs, ys)
        label = "pearson"
    return {"analysis": "correlation", "method": label, "x": x, "y": y, "n": int(len(data)), "r": coef, "p": p}


def partial_correlation(df: pd.DataFrame, x: str, y: str, controls: list[str]) -> dict:
    import statsmodels.api as sm

    variables = [x, y] + controls
    data = clean(df, variables).copy()
    for var in variables:
        data[var] = as_numeric(data[var], var)
    design = sm.add_constant(data[controls], has_constant="add")
    rx = sm.OLS(data[x], design).fit().resid
    ry = sm.OLS(data[y], design).fit().resid
    coef, p = stats.pearsonr(rx, ry)
    return {"analysis": "partial-correlation", "x": x, "y": y, "controls": controls, "n": int(len(data)), "partial_r": coef, "p": p}


def regression(df: pd.DataFrame, dv: str, predictors: list[str]) -> dict:
    import statsmodels.api as sm
    from statsmodels.stats.outliers_influence import variance_inflation_factor

    variables = [dv] + predictors
    data = clean(df, variables).copy()
    data[dv] = as_numeric(data[dv], dv)
    x = pd.get_dummies(data[predictors], drop_first=True, dtype=float)
    x = sm.add_constant(x, has_constant="add")
    model = sm.OLS(data[dv], x).fit()
    y_std = data[dv].std(ddof=1)
    coefficients = []
    for name in model.params.index:
        beta = None
        if name != "const" and y_std:
            beta = model.params[name] * x[name].std(ddof=1) / y_std
        coefficients.append(
            {
                "term": str(name),
                "b": model.params[name],
                "beta": beta,
                "se": model.bse[name],
                "t": model.tvalues[name],
                "p": model.pvalues[name],
            }
        )
    vif = []
    for idx, name in enumerate(x.columns):
        if name == "const":
            continue
        vif.append({"term": str(name), "vif": variance_inflation_factor(x.to_numpy(), idx)})
    return {
        "analysis": "linear-regression",
        "dv": dv,
        "predictors": predictors,
        "n": int(model.nobs),
        "r_squared": model.rsquared,
        "adjusted_r_squared": model.rsquared_adj,
        "f": model.fvalue,
        "model_p": model.f_pvalue,
        "coefficients": coefficients,
        "vif": vif,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--file", required=True)
    parser.add_argument("--sheet")
    parser.add_argument("--analysis", required=True, choices=["audit", "desc", "chi2", "anova", "corr", "partial-corr", "regression"])
    parser.add_argument("--vars", nargs="*", default=[])
    parser.add_argument("--iv")
    parser.add_argument("--dv")
    parser.add_argument("--x")
    parser.add_argument("--y")
    parser.add_argument("--controls", nargs="*", default=[])
    parser.add_argument("--predictors", nargs="*", default=[])
    parser.add_argument("--corr-method", choices=["pearson", "spearman"], default="pearson")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    df, meta = load_data(args.file, args.sheet)
    if args.analysis == "audit":
        result = audit(df, meta)
    elif args.analysis == "desc":
        variables = args.vars or list(df.columns)
        result = descriptive(df, variables)
    elif args.analysis == "chi2":
        result = chi_square(df, args.iv, args.dv)
    elif args.analysis == "anova":
        result = anova(df, args.iv, args.dv)
    elif args.analysis == "corr":
        result = correlation(df, args.x, args.y, args.corr_method)
    elif args.analysis == "partial-corr":
        result = partial_correlation(df, args.x, args.y, args.controls)
    elif args.analysis == "regression":
        result = regression(df, args.dv, args.predictors)
    else:
        raise SystemExit(f"Unsupported analysis: {args.analysis}")
    print(json.dumps(jsonify(result), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
