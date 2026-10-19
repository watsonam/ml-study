# Handover

This repo is Adam's twelve-week study of statistics, time series and machine learning basics, from a quant and data science point of view. It started on 2026-10-18 in a session in the balancing-services-analytics repo. Week 1 runs from Monday 19 to Sunday 25 October 2026.

## How to help

Act as a tutor. Explain, ask questions, review Adam's code and notes, and point to the right section of a book. Do not write the from-scratch pieces, the baselines or the exercise answers: those are done with AI off, and the week's tests check them. Hints are fine when Adam asks for one, smallest first.

Write in plain sentences, with no emojis and no code comments. Prefer a table when comparing things.

## Who and why

Adam builds a European power balancing-market data platform (balancing-services-analytics). He took the AWS Machine Learning Specialty years ago and lost the notes. He wants the basics, not an ML engineering career: statistics, probability, regression, time series and classical ML, with PyTorch as the tool. LLM material is out of scope, except foundation models used for forecasting (Chronos, week 11).

## The plan

The full plan is in `README.md`, and each week's brief is in `week-NN/README.md`. Every week works on one problem: at 12:00 UTC on day D-1, forecast the GB imbalance price for the 48 half-hours of day D. The last 61 days of the data are locked as the test set until week 12.

Each week has 10 hours: 3 reading, 3.5 experiment, 1.5 from scratch in PyTorch, 2 write-up. Reading suits the Monday and Wednesday commute on the iPad or phone. Problem sets from Blitzstein and Hwang come in weeks 4, 8 and 12.

## State on 2026-10-19

- `fetch.py` downloads a year of Elexon system prices to `data/gb_imbalance.parquet` (17,520 rows, 18 Oct 2025 to 17 Oct 2026). `data/` is ignored by git.
- Week 1 tests (`week-01/test_backtest.py`, `week-01/test_curve_fit.py`, 14 tests) fail until Adam writes `backtest.py` and `curve_fit.py`. They were checked against a reference version that was then deleted.
- `experiments.md` is empty.
- The repo is public at https://github.com/watsonam/ml-study as an accountability log. Commits use the GitHub noreply address. Secret scanning and push protection are on; Adam chose to leave the wiki and Dependabot settings as they are.

## Decisions made

- Quant and data science focus. BatchNorm, `DataLoader`, deployment and timed ML coding drills were dropped.
- PyTorch from day one; pandas only loads files.
- Week 1 builds the scorer before any model, plus Bishop 1.1's curve fit to show fitting and overfitting.
- Weekly write-ups go on the blog at https://watsonam.github.io, copied from `week-NN/writeup.md`.

## Open items

| Item | State |
|---|---|
| Hyndman chapters 1 and 2 in week 1 | Proposed: read chapter 1 (skim) and chapter 2 in week 1, move Bishop 1.1 to week 2, keep chapters 3 and 9 in week 4. Adam has not decided |
| Sunday check | A scheduled weekly check of commits against the week's brief. Needs a time from Adam, for example Sunday 20:00 |
| Commute length | Unknown; it decides how much reading moves to Monday and Wednesday |
| Blog tidy-up | `power_research` moved to the private repo watsonam/power-research (PR watsonam/watsonam.github.io#1, merged 2026-10-18). Still open: new tagline, About page (still says S&P Global; Adam to supply the text), keep or hide the GB dashboard, exclude `DECISIONS.md`, `SPEC.md` and `Makefile` from the site, an ML study tag page |
| After week 12 | A Kaggle time series competition; a possible second block on Bayesian methods, panel data across all 21 areas, and deep learning |

## Resources

| Resource | Where |
|---|---|
| Hyndman et al., Forecasting: Principles and Practice, the Pythonic Way | https://otexts.com/fpppy/ (free; save chapters to Safari's Reading List for offline) |
| James et al., ISLP | https://www.statlearning.com (free PDF) |
| Bishop, Pattern Recognition and Machine Learning | Adam's Google Drive (make it available offline in the Drive app) |
| Blitzstein and Hwang, Introduction to Probability | https://www.probabilitybook.net |
| PyTorch Learn the Basics | https://pytorch.org/tutorials/beginner/basics/intro.html |
| Tensor Puzzles | https://github.com/srush/Tensor-Puzzles (one or two per laptop session) |
| Raschka, Machine Learning with PyTorch and Scikit-Learn | Paid book, the closest fit to the plan |
| Karpathy, Neural Networks: Zero to Hero | https://karpathy.ai/zero-to-hero.html (week 10) |
| Alisa Liu's job search post | https://alisawuffles.github.io/blog/job-search/ (the source of the from-scratch, AI-off habit) |

## Commands

```bash
uv sync
```

```bash
uv run python fetch.py
```

```bash
uv run pytest week-01
```
