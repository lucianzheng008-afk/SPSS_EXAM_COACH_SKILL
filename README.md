# SPSS Exam Coach

Codex skill for SPSS operation exams in Chinese quantitative methods courses. It helps with method choice, SPSS menu paths, output-table reading, direct data calculation, exam-ready conclusions, and textbook/classroom-aligned review for 庞琴《国际关系量化研究方法》.

## Install

This repository uses a flat skill layout: `SKILL.md` is at the repository root. Install it with `$skill-installer` using `--path .` and `--name spss-exam-coach`:

```bash
python /Users/zhengsiyuan/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo lucianzheng008-afk/SPSS_EXAM_COACH_SKILL \
  --path . \
  --name spss-exam-coach

## Contents

- `spss-exam-coach/SKILL.md`: main routing and response contract.
- `spss-exam-coach/references/`: SPSS operation maps, interpretation principles, data-execution mode, textbook notes, and classroom review V2.
- `spss-exam-coach/scripts/spss_exam_analyzer.py`: helper for auditing and computing common analyses from `.sav`, `.csv`, and Excel files.

## Typical Prompt

```text
Use $spss-exam-coach to analyze this SPSS操作考试题目 or dataset, compute/check the needed statistics, and give the method choice, principle, exact menu steps, output interpretation, inference, and exam-ready conclusion.
```
