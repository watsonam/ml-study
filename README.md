# ML study

Twelve weeks of classical machine learning and forecasting at 10 hours a week, organised around one problem: forecasting the GB imbalance price for tomorrow.

## Objectives

1. Understand classical ML and forecasting well enough to explain and derive the core methods.
2. Work the way an ML engineer does: evaluation first, baselines, leakage checks, one change per experiment, error analysis, and a decision on whether to ship.
3. Produce a backtested imbalance price forecast that could be deployed next to the balancing-services platform.

Writing ML code fluently in PyTorch, without AI, supports all three.

## Success criteria at week 12

| Objective | Check |
|---|---|
| Understanding | You can explain each week's method in five sentences and redo its from-scratch piece from a blank file |
| Engineering habits | `experiments.md` holds about 12 logged experiments, each with one change and its numbers |
| Useful output | One table compares every model against the baseline on months the models never saw, with MAE, pinball loss and interval coverage |
| Coding fluency | You pass the three timed 45-minute drills in weeks 4, 8 and 12 without AI |

## The problem

At 12:00 UTC on day D-1, forecast the GB imbalance price for each of the 48 half-hour settlement periods of day D. Score the forecast on days the model has never seen.

## Weekly loop

| Part | Hours | Output |
|---|---|---|
| Reading | 3 | `week-NN/notes.md`, in your own words |
| Experiment | 3.5 | One change against last week's best, logged in `experiments.md` |
| From scratch | 1.5 | The method you used, in PyTorch or numpy, with AI off, passing the week's tests |
| Write-up | 2 | `week-NN/writeup.md`, posted to watsonam.github.io on Sunday |

Reading and flashcards suit the Monday and Wednesday commute on the iPad or phone. Coding needs the laptop. Watch a Karpathy video once without coding, then write the code from memory later.

## Rules

- Do the from-scratch piece and the drills with AI assistance turned off.
- Change one thing per experiment, and log every experiment, including the ones that made things worse.
- Never look at the test months while choosing a model.
- If a week slips, do the from-scratch piece only. Never two weeks in a row with no commits.

## The twelve questions

| Week | Question | Reading | From scratch |
|---|---|---|---|
| 01 | How will I know a forecast is good? | Hyndman ch 5 | Rolling-origin backtest, MAE and RMSE, and three naive baselines |
| 02 | What is known at forecast time? | ISLP ch 2 | Lag features that respect the 12:00 cut-off, and a leakage test that fails on purpose |
| 03 | Can a linear model beat the baseline? | ISLP ch 3 and 6 | Ridge regression by gradient descent in PyTorch |
| 04 | Where does it fail? | none | Error slices by hour, weekday, season and price spikes; timed drill 1 |
| 05 | Can trees catch the spikes? | ISLP ch 8 | One decision tree split |
| 06 | How sure is the forecast? | Hyndman 5.9 | Pinball loss and split-conformal intervals |
| 07 | Is the ML model better than classical statistics? | Hyndman ch 8 and 9 | Holt-Winters exponential smoothing |
| 08 | How does a neural net learn? | Karpathy video 1 and CS231n backprop notes | Micrograd in numpy; timed drill 2 |
| 09 | Does a neural net help here? | Karpathy videos 2 and 3 | MLP training loop without `nn.Module` |
| 10 | Why won't it train? | Karpathy video 4 | BatchNorm, and three broken training runs to diagnose |
| 11 | Does a pretrained model beat mine without training? | Hyndman ch 15 | Chronos's scaling and binning of a series into tokens |
| 12 | Would I ship it? | none | Model card, drift check, three earlier pieces redone from blank; timed drill 3 |

## After week 12

Deploy the best model next to the platform. Sit the AWS Certified Machine Learning Engineer Associate exam in week 14, and enter a Kaggle time series competition with the week 12 model.

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

- ISLP: https://www.statlearning.com
- Hyndman et al., Forecasting: Principles and Practice, the Pythonic Way: https://otexts.com/fpppy/
- Karpathy, Neural Networks: Zero to Hero: https://karpathy.ai/zero-to-hero.html
- CS231n backprop notes: https://cs231n.github.io/optimization-2/
- Alisa Liu, job search: https://alisawuffles.github.io/blog/job-search/
