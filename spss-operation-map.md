# SPSS Operation Map

Use this reference for SPSS操作考试题目. Output should be exam-oriented and in Chinese.

When the user asks for 原理、结果描述、推论、怎么看输出, also load `result-interpretation-principles.md`.

## Method Decision

| Situation | Variables | Method |
|---|---|---|
| 描述一个变量的分布、均值、标准差 | one categorical/continuous variable | 描述性统计 |
| 反向题、合并类别、清理杂项 | original variable -> new variable | 重新编码 |
| 找缺失、插补缺失 | one or more variables | 频率 / 替换缺失值 |
| 找偏离值 | continuous variable | 直方图 / 箱图 |
| 多题项加总或求均分 | several items -> new variable | 计算变量 |
| 两个类别变量是否有关 | categorical IV + categorical DV | 卡方检验 |
| 不同组的均值是否不同 | categorical IV + continuous DV | 单因素 ANOVA |
| 两个变量是否相关 | continuous/order variables | 相关分析 |
| 控制第三变量后是否相关 | two main variables + controls | 偏相关 |
| 多个因素解释连续因变量 | continuous DV + multiple IVs | 多元线性回归 |

## 描述性统计

Use when asked for 分布、频数、百分比、均值、标准差、众数、中位数、最小值、最大值、直方图、条形图.

Principle:
- 描述统计用于概括样本本身，不直接做总体假设检验。
- 分类变量看频数/百分比；连续变量看均值、标准差、中位数、极值和图形分布。

SPSS:
- `分析 -> 描述统计 -> 频率`
- Put variable(s) into `变量`.
- For central tendency: click `统计`, select `Mean`, `Median`, `Mode`, `Std. Deviation`, `Minimum`, `Maximum`.
- For charts: click `图表`, choose `条形图` for categorical variables or `直方图` for continuous variables.
- Alternative for mean/SD: `分析 -> 描述统计 -> 描述`, select `平均值` and `标准差`.
- Textbook visual routes:
  - bar chart: `图形 -> 旧对话框 -> 条形图`
  - histogram: `图形 -> 旧对话框 -> 直方图`
  - boxplot: `图形 -> 旧对话框 -> 箱图`

Read:
- Frequency table: 频数、百分比、有效百分比.
- Descriptives table: Mean, Std. Deviation, Minimum, Maximum.
- Charts: bar chart for category concentration; histogram/boxplot for skewness and outliers.

Template:
`变量 X 的均值为 M，标准差为 SD，说明样本总体上处于……水平；标准差越大，说明样本内部差异越大。频率表显示，……选项占比最高，为 ……。`

Traps:
- 分类变量主要报告频数/百分比，不要硬解释均值，除非它是有序量表且老师允许。
- 连续变量适合均值和标准差；偏态明显时可补充中位数。

## 重新编码

Use when asked for 反向题、重新赋值、合并类别、删除其他/不知道/拒答、生成新变量.

Principle:
- 重编码是把旧变量的取值规则转换成新含义，常用于统一方向、合并类别、处理非实质回答。
- 默认保留原变量，用新变量承接结果，方便检查和回退。

SPSS:
- `转换 -> 重新编码为不同的变量`
- Move original variable to input box.
- Enter output variable name and label.
- Click `变化量/Change`.
- Click `旧值与新值`, define mappings.
- Continue, OK.
- Check or edit `值标签`.

Syntax pattern:
```spss
RECODE q1 (1=5)(2=4)(3=3)(4=2)(5=1)(ELSE=SYSMIS) INTO nq1.
VARIABLE LABELS nq1 "经济评价".
EXECUTE.
```

Template:
`本题需要先将变量 X 重新编码为新变量 nX，使数值方向与研究含义一致。旧值……被赋为新值……；杂项值设为系统缺失。完成后需检查新变量的值标签。`

Traps:
- Do not overwrite original variable unless explicitly required.
- Always click `变化量/Change`.
- Update value labels.
- After recoding, run `频率` to verify the new distribution.

## 缺失值和偏离值

Use when asked for 查找缺失值、填补缺失值、异常值、离群值、偏离值.

Principle:
- 缺失值会减少有效样本量并可能造成偏差。
- 偏离值会影响均值、标准差、相关、ANOVA 和回归，因此先识别再决定保留、设缺失、转换或说明。

Missing detection:
- `分析 -> 描述统计 -> 频率`
- Put variable into `变量`.
- Read valid/missing counts and unusual coded values.

Missing imputation:
- `转换 -> 替换缺失值`
- Choose variable.
- Select method:
  - median: robust default for skewed survey variables.
  - mean: acceptable for approximately normal variables.
  - linear trend: mainly for continuous/time-ordered data.

Outlier detection:
- Histogram: `分析 -> 描述统计 -> 频率 -> 图表 -> 直方图`
- Boxplot: `图形 -> 旧对话框 -> 箱图`
- For one variable, choose simple boxplot and place the variable in the analysis field.
- In variable view, define impossible response codes such as `8`, `9`, `99`, `999` as user-missing if the codebook says they mean "不知道/拒答/缺失".

Read:
- Frequency: missing count, unusual values.
- Histogram: extreme bars.
- Boxplot: points outside whiskers.

Template:
`通过频率/箱图检查，变量 X 存在/不存在明显缺失值或偏离值。缺失值采用……方法处理；偏离值根据箱图判断后……。处理后应再次运行描述统计确认数据分布。`

Traps:
- Do not blindly delete many cases.
- Distinguish systematic missing from random missing.
- Imputation should be mentioned as a data-cleaning step before final analysis.

## 计算变量

Use when asked for 合成变量、加总题项、求均分、计算量表分数.

Principle:
- 计算变量把多个观测题项或变量按公式合成一个分析指标。
- 合成前必须确保题项方向一致，必要时先反向重编码；合成后检查范围是否符合理论预期。

SPSS:
- `转换 -> 计算变量`
- Enter target variable name.
- Build numeric expression, such as `nq1 + nq2 + nq3`.
- OK.

Syntax pattern:
```spss
COMPUTE Economic_Eval = nq1 + nq2 + nq3 + nq4 + nq5 + nq6.
VARIABLE LABELS Economic_Eval "Sum of economic evaluation items".
EXECUTE.
```

Recommended order for scale variables:
1. Check item coding.
2. Recode reverse items.
3. Run reliability analysis if required.
4. Compute sum or mean.
5. Run descriptive statistics for the new variable.

Template:
`在完成反向题重编码后，使用“计算变量”将 q... 合成为新变量 X。该变量代表……，之后对 X 进行均值和标准差描述。`

Traps:
- Reverse items must be recoded before computing.
- Sum and mean are not identical; follow the题目 wording.
- Missing values can make computed results missing; note treatment if relevant.

## 卡方检验

Use when both IV and DV are categorical, including binary or multi-category variables.

Principle:
- 卡方检验比较观察频数和独立性假设下的期望频数。
- 零假设是两个类别变量独立；`Sig. < .05` 表示有证据认为二者有关联。

SPSS:
- `分析 -> 描述统计 -> 交叉表`
- Put IV usually into `行`, DV into `列`.
- Click `统计`, select `卡方`; select `Phi 和 Cramer V` for association strength.
- Click `单元格`, select observed counts, expected counts, row or column percentages.
- OK.

Read:
- Crosstabulation: frequencies and percentages.
- Chi-Square Tests: `Pearson Chi-Square`, `df`, `Asymp. Sig.`.
- Symmetric Measures: `Phi` for 2x2; `Cramer's V` for larger tables.
- Expected Count footnote: check whether expected counts are too small.

Rules:
- `p < 0.05`: significant association.
- `p >= 0.05`: no significant association.
- Rough strength: 0-0.30 weak, 0.31-0.70 medium, 0.71-1 strong.
- Significance is not strength.
- Check expected counts: if more than 20% of cells have expected count below 5, merge categories, increase sample size, or consider Fisher/Yates rules for suitable 2x2 cases.

Template:
`卡方检验结果显示，χ²(df)=..., p=...。因此，变量 A 与变量 B 存在/不存在统计显著关联。Phi/Cramer's V=...，说明关联强度较弱/中等/较强。根据列联表百分比，……组更倾向于……。`

Traps:
- Use chi-square only when both variables are categorical.
- If the题目 asks “关系多强”, report Phi/Cramer's V, not only p.
- For table presentation, include percentages.

## ANOVA

Use when IV is categorical and DV is continuous, especially comparing group means.

Principle:
- 单因素 ANOVA 比较多个组的均值差异，核心是组间变异相对组内变异是否足够大。
- 零假设是各组总体均值相等；显著时只说明“至少有一组不同”，具体哪组不同要看事后检验。

SPSS:
- `分析 -> 比较平均值 -> 单因素 ANOVA 检验`
- Put continuous DV into `因变量列表`.
- Put categorical IV into `因子`.
- Click `选项`, select `描述`, `方差齐性检验`, and `均值图` if needed.
- If more than two groups, click `事后检验`.
  - If variances are homogeneous: common choices include LSD or Scheffe; Scheffe is safer for unequal group sizes.
  - If variances are not homogeneous: read Welch/Brown-Forsythe and use Games-Howell, Dunnett T3, Tamhane T2, or Dunnett C where available.
- OK.

Read:
- Descriptives: group means and SD.
- Test of Homogeneity of Variances: Levene Sig.
- ANOVA: F and Sig.
- Post Hoc Multiple Comparisons: which groups differ.

Rules:
- Levene `p > 0.05`: homogeneity not violated.
- ANOVA `p < 0.05`: group means differ significantly.
- Post-hoc tests explain which groups differ.
- `F` itself is not relationship strength; use eta squared if the题目 asks for effect size.

Template:
`单因素方差分析显示，不同 A 组在 B 上存在/不存在显著差异，F(df1, df2)=..., p=...。方差齐性检验 p=...，说明……。事后检验显示，……组与……组差异显著，而……组与……组差异不显著。`

Traps:
- Do not use ANOVA for two categorical variables; use chi-square.
- ANOVA tells whether at least one group differs; post-hoc tells where.
- Always mention the group means before interpreting the difference.

## 相关和偏相关

Use correlation when variables are continuous/order and the task asks whether they are related.

Principle:
- 相关分析衡量两个变量共同变化的方向和强度。
- 偏相关是在控制变量后估计两个核心变量的净相关。
- 零假设是总体相关系数为 0；相关不等于因果。

SPSS bivariate correlation:
- Optional normality check for Pearson: `分析 -> 描述统计 -> 探索 -> 图 -> 含检验的正态图`.
- Optional linearity check: `图形 -> 旧对话框 -> 散点图/点图 -> 简单散点图`.
- `分析 -> 相关 -> 双变量`
- Put variables into `变量`.
- Choose:
  - Pearson for two continuous variables with approximate normal/linear relationship.
  - Spearman for ordinal variables or non-normal variables.
- OK.

SPSS partial correlation:
- `分析 -> 相关 -> 偏相关`
- Put main variables into `变量`.
- Put controls into `控制变量`.
- OK.

Read:
- Correlation coefficient: Pearson `r` or Spearman `ρ`.
- Sig. (2-tailed).
- N.

Rules:
- `r/ρ > 0`: positive relationship.
- `r/ρ < 0`: negative relationship.
- `p < 0.05`: statistically significant.
- Textbook Pearson strength: `|r| < .30` weak, `.30-.50` low, `.50-.80` strong/significant, `.80+` high.

Template:
`相关分析显示，变量 A 与变量 B 存在显著正/负相关，r/ρ=..., p=...。这说明 A 越高，B 越……。在控制变量 C 后，偏相关系数为 ...，p=...，说明二者关系在控制 C 后仍然存在/不再显著。`

Traps:
- Correlation does not prove causality.
- If p is not significant, do not over-interpret a large coefficient.
- Check scatterplot or linearity if the题目 mentions relationship form.

## 多元线性回归

Use when DV is continuous and several predictors are used to explain or predict it.

Principle:
- 多元线性回归考察多个自变量对连续因变量的共同解释力，以及每个自变量在控制其他变量后的独立预测作用。
- 模型显著不代表每个自变量都显著；单个系数显著也要结合方向、大小和共线性判断。

SPSS:
- `分析 -> 回归 -> 线性`
- Put continuous DV into `因变量`.
- Put predictors into `自变量`.
- Choose method:
  - `Enter`: simultaneous regression; use when theory specifies variables.
  - `Stepwise`: exploratory selection; use when finding strongest predictors.
  - hierarchical/block regression: enter predictors in blocks using `Next`, use when comparing theory/control blocks.
- Click `统计`, select `估计`, `模型拟合`, `共线性诊断`, and optionally confidence intervals.
- OK.

Categorical predictors:
- Binary categorical variables can enter as 0/1.
- Multi-category predictors need dummy variables.
- Use `n-1` dummy variables and leave one category as the reference group.

Read:
- Model Summary: R Square and Adjusted R Square.
- ANOVA: model F and Sig.
- Coefficients: unstandardized B, standardized Beta, t, Sig., Tolerance, VIF.

Rules:
- ANOVA `p < 0.05`: model is statistically significant.
- Adjusted R²: preferred model explanatory power for multiple regression.
- Coefficient `p < 0.05`: predictor has significant effect controlling other predictors.
- B: write equation and interpret unit change.
- Beta: compare relative influence across predictors.
- VIF > 10 or Tolerance < .10: severe collinearity; VIF > 5 or Tolerance < .20 can be concerning.

Templates:
`多元线性回归结果显示，模型整体显著，F=..., p=...，调整后 R²=...，说明模型可以解释因变量约 ...% 的变异。`

`系数表显示，在控制其他变量后，X1 对 Y 有显著正/负向影响，B=..., Beta=..., p=...；X2 的影响不显著，p=...。`

`根据未标准化系数，回归方程为：Y = 常量 + B1X1 + B2X2 + ...。`

Traps:
- Do not compare raw B values across variables with different units; use Beta.
- Always report Adjusted R², not only R².
- Mention collinearity diagnostics when the题目 asks for regression operation or model reliability.
- Stepwise is exploratory; Enter/hierarchical is better when theory is clear.
