# ML study

Twelve weeks of statistics, time series and machine learning basics, from a quant and data science point of view, at 10 hours a week. Every week works on one problem: forecasting the GB imbalance price for tomorrow.

## Objectives

1. Understand the statistics and machine learning that quant and data science work rests on, well enough to explain and derive the core methods.
2. Work carefully with data: a locked test set, honest baselines, leakage checks, one change per experiment, and a test of whether an improvement is real.
3. Finish with a backtested imbalance price forecast, compared fairly against simple baselines, that could later feed the balancing-services platform.

PyTorch is the tool for writing each method from scratch, from tensors in week 1 to a small neural network in week 10.

## Success criteria at week 12

| Objective | Check |
|---|---|
| Understanding | You can explain each week's method in five sentences and redo its from-scratch piece from a blank file |
| Careful work | `experiments.md` holds about 12 logged experiments, each with one change and its numbers |
| Useful output | One table compares every model against the best baseline on the locked test months, with MAE, pinball loss, interval coverage and a Diebold-Mariano test |
| Statistics fluency | You complete the three probability and statistics problem sets in weeks 4, 8 and 12 without AI |

## The problem

At 12:00 UTC on day D-1, forecast the GB imbalance price for each of the 48 half-hour settlement periods of day D. Score the forecast on days the model has never seen.

## Weekly loop

| Part | Hours | Output |
|---|---|---|
| Reading | 3 | `week-NN/notes.md`, in your own words |
| Experiment | 3.5 | One change against last week's best, logged in `experiments.md` |
| From scratch | 1.5 | The week's method in PyTorch, with AI off, passing the week's tests where there are any |
| Write-up | 2 | `week-NN/writeup.md`, posted to watsonam.github.io on Sunday |

Reading, the Bishop sections and flashcards suit the Monday and Wednesday commute on the iPad or phone. Bishop's Pattern Recognition and Machine Learning is on Google Drive. Coding needs the laptop. Watch a Karpathy video once without coding, then write the code from memory later.

## Rules

- Do the from-scratch piece and the problem sets with AI assistance turned off.
- Change one thing per experiment, and log every experiment, including the ones that made things worse.
- Never look at the test months while choosing a model.
- If a week slips, do the from-scratch piece only. Never two weeks in a row with no commits.

## The twelve questions

| Week | Question | Reading | From scratch in PyTorch |
|---|---|---|---|
| 01 | How will I know a forecast is good? | Hyndman ch 5; Bishop 1.1 | Rolling-origin backtest, MAE and RMSE, three naive baselines, and Bishop's polynomial curve fit showing overfitting |
| 02 | What do imbalance prices look like as a distribution? | ISLP ch 2; Bishop 1.2 and 2.3 | Normal and Student-t distributions fitted by maximum likelihood with autograd, and a bootstrap confidence interval |
| 03 | Can a linear model beat the baseline, and which inputs matter? | ISLP ch 3 and 6.2 | Least squares with standard errors, checked against statsmodels, then ridge |
| 04 | How does today's price depend on yesterday's? | Hyndman ch 2, 3 and 9 | Autocorrelation function and an autoregressive model by least squares; problem set 1 |
| 05 | Can I predict a spike? | ISLP ch 4 | Logistic regression with binary cross-entropy, an ROC curve and a calibration check |
| 06 | Am I fooling myself? | ISLP ch 5 | Lag features that respect the 12:00 cut-off, a leakage test that fails on purpose, and error slices by hour, season and spike |
| 07 | Do trees do better? | ISLP ch 8 | One decision tree split, then LightGBM |
| 08 | How uncertain is the price? | Hyndman 5.9; arch documentation | Quantile regression with pinball loss, split-conformal intervals, and a GARCH(1,1) volatility model; problem set 2 |
| 09 | What shapes do daily prices take? | ISLP ch 12 | PCA on the 48-period daily price curves, and k-means on days |
| 10 | How does a neural net learn? | Karpathy videos 1 and 2 | Micrograd, with gradients checked against PyTorch, then a small MLP |
| 11 | Does a neural net or Chronos beat the rest, really? | Hyndman ch 15; Diebold and Mariano | MLP forecast, Chronos zero-shot, and a Diebold-Mariano test on every pair of models |
| 12 | What did I learn? | none | Score everything once on the test months, redo three earlier pieces from blank, and write the final comparison; problem set 3 |

## Problem sets

Weeks 4, 8 and 12 each end with a two-hour probability and statistics problem set, done on paper with AI off. Take the problems from Blitzstein and Hwang's Introduction to Probability, which is free. Zhou's A Practical Guide to Quantitative Finance Interviews (the "green book") is a paid alternative with quant interview problems.

## After week 12

Enter a Kaggle time series competition with the week 12 model. A second block can cover the topics left out here: Bayesian methods, panel data across all 21 areas, and deep learning beyond an MLP.

## Setup

```bash
uv sync
```

```bash
uv run python fetch.py
```

```bash
uv run jupyter lab
```

`fetch.py` downloads a year of GB imbalance prices from Elexon into `data/gb_imbalance.parquet`. Elexon's API needs no key.

## Sources

- James et al., An Introduction to Statistical Learning with Python (ISLP): https://www.statlearning.com
- Hyndman et al., Forecasting: Principles and Practice, the Pythonic Way: https://otexts.com/fpppy/
- Bishop, Pattern Recognition and Machine Learning (on Google Drive)
- Karpathy, Neural Networks: Zero to Hero: https://karpathy.ai/zero-to-hero.html
- arch, univariate volatility models: https://arch.readthedocs.io/en/latest/univariate/introduction.html
- Diebold and Mariano (1995), Comparing Predictive Accuracy, Journal of Business and Economic Statistics
- Blitzstein and Hwang, Introduction to Probability: https://www.probabilitybook.net
- Alisa Liu, job search: https://alisawuffles.github.io/blog/job-search/
