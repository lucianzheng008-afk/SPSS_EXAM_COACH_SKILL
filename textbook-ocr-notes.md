# Textbook OCR Notes

Source: `/Users/zhengsiyuan/Desktop/资料/定量课件/国际关系量化研究方法-庞琴-20260613183536/国际关系量化研究方法-庞琴.md`

Use this reference only to align SPSS exam answers with 庞琴《国际关系量化研究方法》. Keep answers operational; do not quote long textbook passages.

## OCR Status

- Full OCR Markdown exists and is readable.
- Relevant chapters found: Chapter 6 SPSS basics, Chapter 7 chi-square, Chapter 8 ANOVA, Chapter 9 correlation.
- Chapter 10 linear regression appears incomplete or noisy in the OCR body: the table of contents lists it, but direct searches mainly found later logistic/panel regression material. For multiple linear regression, rely on `spss-operation-map.md` and do not import logistic-regression wording unless the user explicitly asks for logistic regression.
- Images are stored in `/Users/zhengsiyuan/Desktop/资料/定量课件/国际关系量化研究方法-庞琴-20260613183536/images`.

## Descriptive Statistics And Data Cleaning

- Before formal hypothesis testing, describe each main variable's distribution to decide later analysis strategy.
- Continuous variables: report mean, median, mode if useful, quartiles, SD, variance, range, min, max; use histogram for distribution and possible outliers.
- Categorical variables: report frequency and percentage; use bar chart.
- Median is less sensitive than mean to extreme values; if a distribution has outliers or skew, mention median as a more robust center.
- SPSS route for central tendency: `分析 -> 描述统计 -> 频率 -> 统计`, then choose mean, median, mode, quartiles/percentiles as needed.
- SPSS route for dispersion: `分析 -> 描述统计 -> 频率 -> 统计`, then choose standard deviation, variance, range, min, max.
- Histogram route: `图形 -> 旧对话框 -> 直方图`; choose the continuous variable and add title if needed.
- Boxplot route: `图形 -> 旧对话框 -> 箱图 -> 单独变量的摘要`; put the target continuous variable into the boxplot field.
- Missing values can be system missing or user-defined missing. In variable view, define impossible codes such as `8`, `9`, `99`, `999` as missing when they are not substantive answers.
- Missing handling: deletion can be listwise or pairwise; imputation can be used when missingness is limited. The textbook highlights multiple imputation as a principled approach, but exam operations may use the method specified by the question.
- Outliers affect regression and ANOVA; identify them with frequency/histogram or boxplot before final analysis.

## Compute And Recode

- Compute variables: `转换 -> 计算变量`; enter a target variable and a numeric expression. Use it for sums, means, transformations, and derived indicators.
- Recode: `转换 -> 重新编码`. Prefer `重新编码为不同变量` so the original variable remains intact.
- For categorical recoding, map old values into new categories. Example: alliance levels `5,4 -> 2`; `3,2,1 -> 1`.
- For continuous recoding, use ranges. Example age groups: `0-14 -> 1`, `15-64 -> 2`, `65+ -> 3`.
- After recoding, run frequency on the new variable and check value labels.

## Chi-Square

- Use chi-square when both variables are categorical/nominal. The textbook distinguishes goodness-of-fit for one categorical variable and independence chi-square for two categorical variables; the exam focus is usually independence chi-square.
- A contingency/crosstab table shows frequency and percentage combinations of two categorical variables.
- Usually put the independent variable in rows and the dependent variable in columns. Interpret percentages along the independent variable direction.
- SPSS route: `分析 -> 描述统计 -> 交叉表`.
- In `统计`, choose `卡方`; choose `Phi 和 Cramer V` for association strength.
- In `单元格`, select observed count, expected count, row percentage, column percentage, and total percentage as required.
- Output reading order:
  1. Case Processing Summary: valid and missing cases.
  2. Crosstabulation: counts, expected counts, and percentages.
  3. Chi-Square Tests: Pearson Chi-Square, df, and Sig.
  4. Symmetric Measures: Phi for `2 x 2`; Cramer's V when any variable has more than two categories.
- Assumption check: ideally sample size `>= 40`; expected counts should generally be at least 5 in at least 80% of cells. If more than 20% expected counts are below 5, consider merging categories, increasing sample size, Yates correction for eligible `2 x 2`, or Fisher exact test when appropriate.
- Interpretation: `p < 0.05` rejects the null that variables are independent. Then use Phi/Cramer's V for strength. Significance is not strength.
- Strength guide used by the textbook: absolute association coefficient `< .30` weak, `.30-.70` moderate, `> .70` strong.
- Exam wording: "变量 A 与变量 B 存在/不存在统计显著关联；Phi/Cramer's V=...，关联强度为..."

## ANOVA

- Use one-way ANOVA when the independent variable is categorical and the dependent variable is continuous.
- ANOVA compares between-group variation with within-group/error variation. `F = MSB / MSW`.
- The null hypothesis is that group means are not significantly different.
- SPSS route: `分析 -> 比较平均值 -> 单因素 ANOVA 检验`.
- Put the continuous dependent variable into `因变量列表`; put the categorical independent variable into `因子`.
- In `选项`, select `描述`, `方差齐性检验`, Brown-Forsythe, Welch, and mean plot when needed.
- If more than two groups, use `事后检验`. If variance homogeneity holds, textbook examples include LSD and Scheffe; if group sizes differ, Scheffe is safer. If variance homogeneity is violated, use Dunnett T3, Games-Howell, Tamhane T2, or Dunnett C where available.
- Output reading order:
  1. Descriptives: N, mean, SD, SE, min, max for each group.
  2. Test of Homogeneity of Variances: Levene Sig.
  3. ANOVA table: sum of squares, df, mean square, F, Sig.
  4. Robust tests such as Welch/Brown-Forsythe if homogeneity is violated.
  5. Multiple Comparisons: which group pairs differ.
- Interpretation: if ANOVA `p < .05`, at least one group mean differs; use post-hoc tests to say which groups differ.
- Effect size: eta squared can express how much of total variation is explained by the independent variable. Textbook guide: `.01-.059` weak, `.059-.138` moderate, `>= .138` strong.

## Correlation And Partial Correlation

- Use correlation to test whether two variables are associated and to estimate direction and strength. Correlation does not prove causality.
- Before Pearson correlation, check approximate normality and linearity.
- Normality route: `分析 -> 描述统计 -> 探索`; put variables into dependent list; choose plots and tick normality plots with tests.
- Normality judgment: if K-S and Shapiro-Wilk Sig. are both `> .05`, treat as approximately normal. If they conflict, use K-S more for large samples and Shapiro-Wilk more for small samples; also inspect histogram, P-P plot, and Q-Q plot.
- Linearity route: `图形 -> 旧对话框 -> 散点图/点图 -> 简单散点图`; put the two variables into X and Y axes.
- Bivariate route: `分析 -> 相关 -> 双变量`; put variables into `变量`; choose Pearson or Spearman.
- Pearson: use for continuous variables that are approximately normal and linearly related.
- Spearman: use for ordinal variables, rank variables, non-normal data, unknown distribution, or monotonic but not clearly linear relations.
- Point-biserial correlation: use for one binary categorical variable and one continuous variable; it is equivalent to Pearson after coding the binary variable as `0/1`, but interpret direction relative to the reference coding.
- Partial correlation, also called net correlation in the textbook, controls one or more variables and then examines the relationship between two target variables.
- Partial route: `分析 -> 相关 -> 偏相关`; put the two target variables into `变量`; put controls into `控制变量`.
- Output: read correlation coefficient `r` or `ρ`, Sig. (2-tailed), and N.
- Result rule: if `p >= .05`, do not interpret the coefficient as reliable even if its absolute value looks large.
- Textbook strength guide for Pearson: `|r| < .30` weak, `.30-.50` low, `.50-.80` significant/strong, `.80-1` high.

## Multiple Linear Regression

- Because Chapter 10 OCR is incomplete/noisy, use `spss-operation-map.md` for the operation core.
- Keep textbook-aligned theory: linear regression remains association/conditional expectation unless a causal design justifies causal language.
- Use multiple linear regression when the dependent variable is continuous and several predictors explain or predict it.
- Main output reading order: Model Summary (`R Square`, `Adjusted R Square`), ANOVA (`F`, `Sig.`), Coefficients (`B`, `Beta`, `t`, `Sig.`, `Tolerance`, `VIF`).
- Enter/simultaneous regression: all predictors entered at once; use when theory specifies the variables.
- Stepwise regression: exploratory variable selection; use only when the task asks for strongest predictors or stepwise method.
- Hierarchical/block regression: enter predictors by blocks with `Next`; use when comparing controls first, then core explanatory variables.
- Multi-category categorical predictors need dummy variables: use `n-1` dummies and leave one category as reference.
