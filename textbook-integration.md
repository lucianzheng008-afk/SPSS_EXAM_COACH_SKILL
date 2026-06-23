# Textbook Integration

Source textbook registered for this skill:

- Title: 《国际关系量化研究方法》
- Editor/Author shown in PDF: 庞琴 编著
- Publisher shown in PDF: 北京大学出版社
- ISBN shown in PDF: 978-7-301-36808-4
- Local PDF: `/Users/zhengsiyuan/Library/Containers/com.tencent.xinWeChat/Data/Documents/xwechat_files/wxid_yzhwccdh3wro22_519e/msg/file/2026-06/国际关系量化研究方法-庞琴.pdf`
- OCR Markdown: `/Users/zhengsiyuan/Desktop/资料/定量课件/国际关系量化研究方法-庞琴-20260613183536/国际关系量化研究方法-庞琴.md`
- OCR images: `/Users/zhengsiyuan/Desktop/资料/定量课件/国际关系量化研究方法-庞琴-20260613183536/images`
- PDF status: scanned/image-only PDF; `pypdf` text extraction returns empty pages. Do not claim to have full searchable textbook text unless OCR or user-provided page screenshots/text are available.
- OCR status: user provided a full OCR Markdown export on 2026-06-13. Exam-relevant points have been summarized in `textbook-ocr-notes.md`. Chapter 10 linear-regression OCR is incomplete/noisy, so use `spss-operation-map.md` for regression operation details.
- PDF metadata checked: 435 pages, not encrypted, produced by iOS Quartz PDFContext.

## How To Use This Source

Use this file when the user asks for textbook-aligned SPSS exam answers or mentions 庞琴/教材/课本. Prefer the operational rules in `spss-operation-map.md` for exact exam responses, use `textbook-ocr-notes.md` for OCR-confirmed textbook points, and use the table-of-contents anchors below to align terminology and chapter scope.

If the user gives a page number or asks for a precise textbook passage:

1. Use the OCR Markdown path above if exact textbook context is needed.
2. Use the known chapter anchor if it matches the topic.
3. Ask for a screenshot or page image only if the Markdown OCR is too noisy for the exact wording needed.
4. Do not quote long textbook passages. Summarize into exam-operation guidance.

## Relevant Table Of Contents Anchors

These anchors were read visually from rendered PDF pages. Page numbers below are printed book page numbers from the table of contents, not guaranteed PDF page indices.

### Chapter 5: 概率、假设检验与变量描述

- starts p.92
- 概率: p.93
- 如何用概率进行假设检验: p.100
- 假设推论检验: p.104
- SPSS 简介: p.107
- 使用 SPSS 进行推论统计: p.107

Use for: p 值、显著性、零假设/备择假设、为什么 `Sig. < .05` 才能拒绝零假设。

### Chapter 6: SPSS 基本操作介绍

- starts p.112
- 什么是 SPSS: p.112
- SPSS 主界面: p.113
- SPSS 的结果在哪里查看: p.114
- 如何录入数据: p.115
- 用 SPSS 做简单描述性统计: p.127
- SPSS 程序和语法编辑器: p.139
- 描述性统计 AI 辅助: p.144
- 用 SPSS 对数据库数据进行转换: p.144

Use for: 描述性统计、结果窗口、数据录入、语法、变量转换/再编码的基础说明。

### Chapter 7: 卡方分析

- starts p.152
- 什么是卡方检验: p.153
- 卡方检验主要看哪些值及数理原理: p.158
- 用 SPSS 做卡方检验: p.163
- 如何阅读卡方检验结果: p.166
- 卡方检验 AI 辅助: p.167

Use for: 两个类别变量、交叉表、Pearson Chi-Square、df、Sig.、Phi/Cramer's V、列联表百分比。

### Chapter 8: 方差分析

- starts p.172
- 什么是方差分析: p.174
- 方差分析主要看哪些值: p.182
- 用 SPSS 做方差分析: p.184
- 如何阅读方差分析结果: p.189
- 方差分析 AI 辅助: p.190

Use for: 类别自变量 + 连续因变量、组间均值比较、Levene 方差齐性、ANOVA 的 F 和 Sig.、事后检验。

### Chapter 9: 相关分析

- starts p.194
- 什么是相关分析及使用条件: p.195
- 相关系数及数理原理: p.198
- 用 SPSS 做相关分析: p.204
- 如何阅读相关分析结果: p.210
- 相关分析 AI 辅助: p.210

Use for: Pearson、Spearman、点二列相关、偏相关/净相关的前置理解、r/ρ、Sig.、方向和强度。

### Chapter 10: 线性回归

- starts p.217
- 什么是线性回归: p.218
- 如何计算回归线、回归分析主要看哪些值: p.221
- 线性回归使用条件: p.224
- 多元线性回归模型: p.228
- 用 SPSS 做一元线性回归: p.233
- 如何阅读一元线性回归结果: p.235
- 用 SPSS 做多元线性回归: p.240
- 如何阅读多元线性回归结果: p.242
- 线性回归 AI 辅助: p.246

Use for: 回归方程、R²/调整 R²、ANOVA 模型显著性、B、Beta、t、Sig.、VIF/容差、同时/逐步/分层回归的考试解释。

### Chapter 11: 逻辑回归

- starts p.253
- 用 SPSS 做逻辑回归: p.265

Use only if a题目 clearly has a binary/categorical dependent variable and asks for logistic regression. This is outside the user's current main exam list unless explicitly mentioned.

## Textbook-Aligned Answer Style

When aligning with this textbook, prefer wording like:

- `本题首先根据自变量和因变量的测量层次选择统计方法。`
- `在 SPSS 输出中，主要阅读 ... 表。`
- `若 Sig. 小于 0.05，则拒绝零假设，认为二者存在统计显著关系/差异/影响。`
- `需要注意，统计显著不等于关系强，关系强度还要看 ...。`
- `在考试操作中，先完成变量处理，再进行统计检验，最后根据输出表写结论。`

Keep the final response operational. Do not turn a操作题 into a textbook summary unless the user asks for theory.
