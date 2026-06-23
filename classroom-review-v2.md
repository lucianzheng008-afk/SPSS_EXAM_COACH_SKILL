# Classroom Review V2

Source integrated from the user's uploaded PDF: `国际关系量化研究方法_SPSS上机复习大纲_V2(1).pdf`, generated 2026-06-23. Use this reference for open-book review notes, course-case transfer, last-minute checks, and exam-style synthesis. Keep answers operational rather than turning them into a textbook summary.

## Universal Exam Chain

Every SPSS上机 answer should follow:

`研究问题 -> 变量结构 -> 数据质量 -> 方法前提 -> SPSS操作 -> 输出定位 -> 统计结论 -> 国际关系解释`

Minimum acceptable interpretation:

1. Identify the independent variable, dependent variable, and measurement level.
2. Explain why the method fits.
3. Check valid N, missing values, and key assumptions.
4. Read `Sig.` plus the relevant statistic/effect size.
5. Separate sample description, statistical inference, substantive meaning, and limitation.

## Method Decision Snapshot

| Task | Variables | Method |
|---|---|---|
| frequency, percentage, mean, SD, histogram, boxplot | one categorical or continuous variable | 描述性统计 |
| reverse item, merge categories, remove "don't know/refused/other" | original variable -> new variable | 重新编码 |
| build scale score from items | multiple items -> new score | 信度分析 then 计算变量 |
| missing values or outliers | one or more variables | 频率, 箱图, 直方图, 替换缺失值 |
| category vs category | categorical IV + categorical DV | 卡方检验 |
| group mean comparison | categorical IV + continuous DV | 单因素 ANOVA |
| association between continuous/order variables | continuous/order variables | 相关分析 |
| association after controls | two main variables + controls | 偏相关 |
| explain/predict continuous Y | continuous DV + multiple predictors | 多元线性回归 |

Mnemonic:

- 类别对类别: 卡方.
- 类别看均值: ANOVA.
- 连续对连续: 相关.
- 连续因变量 plus multiple predictors: 回归.
- 反向题先重编码; 量表题先信度, then compute sum/mean.

## Global SPSS State Checklist

Before running analysis and before submission, check:

- `数据 -> 选择个案` is not accidentally filtering cases.
- `数据 -> 拆分文件` is not accidentally splitting output.
- `数据 -> 加权个案` is not accidentally weighting cases.
- The original variables were not overwritten by recoding.
- The active data window is the intended dataset.
- Output, syntax, and data files are saved.
- SPSS status bar/log does not show unexpected filter, weight, or split states.

## Output Location Quick Table

| Method | First read | Then read | Finally read |
|---|---|---|---|
| 描述统计 | N and missing | mean/percentage/SD | charts, skewness, outliers |
| 信度 | item direction | overall alpha | item-total correlation, alpha if item deleted |
| 卡方 | crosstab direction | Pearson χ² and expected counts | Cramer's V/Phi, residuals if needed |
| ANOVA | group descriptives | Levene and overall F | planned/post-hoc comparisons, eta squared |
| 相关 | scatterplot and N | coefficient direction/size | p value, outliers |
| 回归 | model setup and diagnostics | Model Summary and F | coefficients, CI, collinearity |

## Significance And Effect Size Rules

- `p < .05`: reject the null hypothesis.
- `p >= .05`: fail to reject the null; do not say "prove no relationship".
- SPSS `.000` should be written as `p < .001`.
- Significance is not strength. Also report `r`, `Phi`, `Cramer's V`, `eta squared`, `R²`, `Adjusted R²`, `B`, or `Beta` when relevant.
- Sample size can make very small effects significant; comment on substantive importance separately.
- Avoid causal wording for observational data. Prefer `相关`, `关联`, `预测`, `解释`, or `控制后仍相关`.

## Scale Construction And Reliability

Use this order for q-style item batteries:

1. Check legal coding and missing codes.
2. Reverse-code items when necessary.
3. Run reliability analysis: `分析 -> 标度 -> 可靠性分析`.
4. Read `Cronbach's Alpha`, item-total correlations, and alpha if item deleted.
5. Compute sum or mean score: `转换 -> 计算变量`.
6. Describe the new variable and use it in later tests.

Rules:

- Reverse items not recoded can lower alpha and invert interpretation.
- `α >= .70` is a common acceptable threshold, but `α > .90` may indicate repetitive items.
- Do not combine `q1-q6` or `q7-q19` before checking coding, direction, missing values, and reliability.

## Method Distinctions

### Chi-Square vs ANOVA

| Point | Chi-square | One-way ANOVA |
|---|---|---|
| DV | categorical | continuous |
| IV | categorical | categorical group variable |
| Compares | frequencies/proportions | group means |
| Statistic | χ² | F |
| Key assumption | expected counts, independence | normality, homogeneity, independence |
| After significance | percentages, strength | planned/post-hoc comparisons |

### Correlation vs Regression

| Point | Correlation | Regression |
|---|---|---|
| Goal | describe co-movement | conditional explanation/prediction of Y |
| Variable roles | usually symmetric | clear DV and IVs |
| Main output | r/ρ/τ, p, N | B, Beta, R², F, diagnostics |
| Unit interpretation | standardized/no original unit | B keeps original units |
| Controls | partial correlation can control | multiple regression systematically controls |
| Causality | not automatic | still not automatic with observational data |

## Course Cases

Use these examples for analogy and exam wording.

### 1. P5 UN Voting Behavior

- Data: 1945-2019 annual voting records for the five permanent members.
- Coding: yes `1`, abstain `0`, no `-1`.
- IV: country, five categories.
- DV: voting behavior score, treated as numeric tendency.
- Method: one-way ANOVA.
- Classroom result: `F=394.66`, `p<.001`.
- Wording: 五个常任理事国的联合国投票行为均值存在统计显著差异. The overall F only shows at least two countries differ; use post-hoc comparisons for specific pairs.
- Trap: if each vote is treated as a nominal category rather than a numeric tendency, the method may become chi-square.

### 2. Residence And Perceived China Influence

- IV: residence `ir13`, capital, big city, town, rural.
- DV: China influence perception `q161`, recoded as continuous score.
- Method: one-way ANOVA.
- Classroom values: means `3.9067`, `3.8038`, `3.8948`, `4.1507`; total mean `3.9320`; Levene `p=.101`; `F=46.551`, `p<.001`.
- Post-hoc: Scheffe was used because group sizes differed. Rural group was significantly higher than capital, big city, and town; the other three groups were not significantly different.
- Wording: 不同居住地区受访者对中国影响力的平均评价存在显著差异, with rural highest.

### 3. UN Ideal Point Distance IPDUS

- Question: compare North America, Africa, and Europe on IPDUS mean.
- Method: region categorical IV + IPDUS continuous DV -> one-way ANOVA.
- Route: descriptives/boxplot -> Levene -> overall F -> Scheffe or Games-Howell -> pair differences.
- Trap: course material says higher IPDUS means more similar to the United States; verify variable label before writing direction.

### 4. Party Participation And Initial Trust

- IV: party participation, binary.
- DV: initial trust score, 1-4.
- Method: independent-samples t-test or one-way ANOVA; for two groups `F=t²`.
- If the course section requires ANOVA, answer with ANOVA. If the题目 emphasizes two independent means, t-test is more direct.
- Do not infer the direction from stereotypes; read group means and p.

### 5. Bride Price And Global Peace Index

- IV: whether bride price exists, binary.
- DV: Global Peace Index, continuous.
- Classroom result: between SS `7.021`, within SS `35.999`, `F=31.398`, `p<.0001`.
- Conclusion: the two groups differ significantly in mean GPI.
- Trap: verify whether higher GPI means more peaceful or less peaceful before giving substantive direction. Difference is not causation.

### 6. Wealth And Corruption

- Hypothesis: richer countries have lower corruption.
- X: GDP per capita.
- Y: corruption index.
- Route: decode index direction -> scatterplot -> Pearson if linear/approximately normal, Spearman otherwise -> report r, p, N, direction.
- Trap: if high score means clean, wealth and corruption may appear positive with cleanliness; if high score means corrupt, relationship may be negative.

### 7. China-Philippines Mutual Favorability

- Data: 2013-2021 annual observations.
- Method: Pearson correlation.
- Classroom result: `r=.978`, `p<.001`, `N=9`.
- Wording: the two favorability series move together strongly, but only nine yearly observations and common bilateral events mean this cannot prove one public's attitude caused the other's.

### 8. Ideology And Nuclear Use Willingness

- Variables: ideology `LR`, education, country, gender, age, and `scenario1-scenario4`.
- Question: after controlling education, is ideology still related to nuclear use willingness?
- Method: partial correlation.
- SPSS: `分析 -> 相关 -> 偏相关`.
- Classroom result: `r_partial=.232`, `p<.001`.
- Wording: controlling education, ideology has a low positive partial correlation with nuclear use willingness. If larger `LR` means more right-leaning, right-leaning respondents show higher support. Only education is controlled.

### 9. Third Countries Choosing The United States In 1955

- DV: UN voting agreement with the United States.
- IVs: GNP per capita, power rank, regime stability, opposition-party freedom, etc.
- Method: multiple linear regression.
- Classroom result: `R²=.746`, Adjusted `R²=.564`, overall model `p=.046`.
- Reminders:
  - State each `x` and dummy-variable reference group.
  - The classroom used `.10` as a loose threshold; if the exam default is `.05`, do not call `p<.10` significant.
  - Non-significant negative coefficients describe sample direction only.
  - Compare relative influence with standardized Beta, not raw B across different units.

### 10. Brazil Consumer Inflation Expectation

- Data: 2005-2018 macro data.
- Method: multiple linear regression.
- Classroom model 5: `F=383.124`, `p<.001`.
- Course equation uses the data spelling `consumer_inflation_expection`; keep dataset variable names exactly in syntax even if spelling looks wrong.
- To claim the strongest influence, check standardized Beta. Also check VIF/Tolerance and residual plots; large F alone does not prove the model is reliable.

### 11. Public Judgment Of China's Influence Size q160

- Task: examine whether age, gender, education, nationalism, family income, and political participation relate to `q160`.
- If `q160` is treated as a continuous score, use multiple linear regression.
- Route: descriptives and correlation matrix -> define categorical reference groups -> Enter regression -> collinearity -> Adjusted R², F, B/Beta/p/CI -> diagnostics.
- Non-significant variables should not be described as having "no effect at all".

### 12. Political Trust q7-q19

This is the comprehensive practice route:

1. Check legal codes and missing codes for `q7-q19`.
2. Reverse-code required items and update value labels.
3. Run reliability analysis.
4. Compute political trust sum or mean.
5. Output overall mean, SD, histogram, and boxplot.
6. Output grouped mean, SD, and plots by East Asian country/region.
7. If asked for group differences, run one-way ANOVA.
8. Save data, syntax, and output.

## Copyable Result Language

Distribution:

`有效样本中, ___类占比最高(___%), 其次为___(___%); 变量存在___个缺失观测.`

Mean:

`Y 的平均值为___(SD=___), 取值范围为___至___.`

Significant:

`结果达到统计显著, ___=___, p=___; 效应方向为___, 大小为___.`

Not significant:

`在当前样本和模型下, 未发现足够证据表明___, ___=___, p=___.`

Conditional relationship:

`在其他变量保持不变时, X 每增加一个单位, Y 的预测值平均增加/减少___个单位.`

Limitation:

`该分析显示统计关联, 但由于数据为观察性数据, 仍可能存在反向因果、遗漏变量或测量误差, 不能单独建立因果关系.`

## 90-Second Submission Checklist

- Question number and output table match.
- IV and DV are not reversed.
- Valid N and missing values were checked.
- Assumption checks were read.
- Statistic, df, p, direction, and effect size were reported.
- `p=.000` was changed to `p<.001`.
- Correlation/regression was not written as causation.
- Filter, weight, and split-file status are correct.
- `.sav`, `.sps`, and `.spv` are saved to the required location.
