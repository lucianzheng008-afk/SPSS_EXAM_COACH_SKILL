# Data Execution Mode

Use this reference when the user sends an SPSS/CSV/Excel dataset together with a题目 and wants Codex to compute the answer directly.

## Goal

Do not guess from the题目 alone when raw data is available. Load the data, audit variables, run the matching statistical procedure, then write the Chinese exam answer from computed values.

## Supported Data

- `.sav`: SPSS data, read with `pyreadstat`.
- `.csv`: read with `pandas.read_csv`.
- `.xlsx` / `.xls`: read with `pandas.read_excel`.

Preferred runtime:

`/Users/zhengsiyuan/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3`

Required packages for full mode: `pandas`, `numpy`, `pyreadstat`, `scipy`, `statsmodels`, `openpyxl`.

Reusable script:

`scripts/spss_exam_analyzer.py`

## High-Accuracy Workflow

1. Save or locate the user's data file.
2. Run an audit first:
   ```bash
   python scripts/spss_exam_analyzer.py --file DATA --analysis audit
   ```
3. Match题目 variables to data columns:
   - Prefer exact column names from the file.
   - Use SPSS variable labels/value labels when `.sav` metadata is available.
   - If two candidate variables are plausible, state the ambiguity and ask only that question.
4. Check variable measurement levels:
   - few unique numeric/text categories -> categorical
   - ordered Likert-style numeric variable -> ordinal, often acceptable for Spearman or scale computation
   - many numeric values -> continuous
5. Run the needed calculation with the script.
6. Write the answer using the standard Response Contract:
   - method choice
   - principle
   - SPSS menu path
   - exact computed output values
   - result interpretation and inference
   - exam-ready conclusion

## Script Commands

Audit:
```bash
python scripts/spss_exam_analyzer.py --file DATA --analysis audit
```

Descriptive statistics:
```bash
python scripts/spss_exam_analyzer.py --file DATA --analysis desc --vars var1 var2
```

Chi-square:
```bash
python scripts/spss_exam_analyzer.py --file DATA --analysis chi2 --iv group_var --dv outcome_var
```

One-way ANOVA:
```bash
python scripts/spss_exam_analyzer.py --file DATA --analysis anova --iv group_var --dv continuous_var
```

Correlation:
```bash
python scripts/spss_exam_analyzer.py --file DATA --analysis corr --x var1 --y var2 --corr-method pearson
python scripts/spss_exam_analyzer.py --file DATA --analysis corr --x var1 --y var2 --corr-method spearman
```

Partial correlation:
```bash
python scripts/spss_exam_analyzer.py --file DATA --analysis partial-corr --x var1 --y var2 --controls control1 control2
```

Linear regression:
```bash
python scripts/spss_exam_analyzer.py --file DATA --analysis regression --dv y --predictors x1 x2 x3
```

## Accuracy Rules

- Always audit before analyzing a new dataset.
- Always report valid `N`; analysis uses listwise deletion for variables included in that model.
- Do not silently choose among ambiguous variables.
- Do not treat coded missing values such as `8`, `9`, `99`, `999` as real answers if labels or codebook say they mean missing/refused/unknown.
- For categorical predictors in regression, the script dummy-codes with one reference category dropped; mention the reference group if visible from variable coding.
- For ANOVA, report Levene's p before choosing ordinary ANOVA/post-hoc wording.
- For chi-square, report expected-count warnings when more than 20% of cells have expected counts below 5.
- If the script result and SPSS screenshot disagree, first check missing-value definitions, filters, weights, value labels, and listwise/pairwise deletion.
