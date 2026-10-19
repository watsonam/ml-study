# Week 01: How will I know a forecast is good?

## The ask

By Sunday you will have forecast tomorrow's GB imbalance price with three simple rules, and measured how wrong each rule is over about ten months. You will not build a model yet. The best rule's error becomes the number every model has to beat from week 3 onward.

On the way you write two small pieces of PyTorch: a scorer for forecasts, and a curve fit that shows what fitting and overfitting look like.

## The problem in one line

At 12:00 UTC on day D-1, forecast the price for each of the 48 half-hours of day D.

## The steps, in order

### Step 0: set up (15 minutes, Sunday or Monday morning)

From the repo root:

```bash
uv sync
```

```bash
uv run python fetch.py
```

```bash
uv run pytest week-01
```

The tests fail with "No module named backtest". That is expected: steps 3 and 4 make them pass.

### Step 1: read on the Monday commute (1.5 hours)

- Hyndman chapter 1, skimmed: https://otexts.com/fpppy/01-intro.html
- Hyndman 5.1 to 5.4 (simple forecasting methods, residuals): https://otexts.com/fpppy/05-toolbox.html

Write the first headings of `notes.md` in your own words.

### Step 2: read on the Wednesday commute (1.5 hours)

- Hyndman 5.8 (accuracy measures) and 5.10 (time series cross-validation). Skip 5.9.
- Bishop 1.1, pages 4 to 10, stopping where regularisation starts. It is on your Google Drive.

Finish `notes.md`, including the five-sentence explanation at the bottom.

### Step 3: write `backtest.py` (45 minutes, laptop, AI off)

In PyTorch only:

- `rolling_origin_splits(n_days, initial, horizon=1, step=1)` returns a list of `(train_idx, test_idx)` pairs of day indices. Training always ends before testing starts, and the training window grows by `step` each fold.
- `mae(y, y_hat)` and `rmse(y, y_hat)` take tensors and return a float.

Done when `uv run pytest week-01/test_backtest.py` passes.

### Step 4: write `curve_fit.py` (45 minutes, laptop, AI off)

In PyTorch only:

- `fit_polynomial(x, y, degree)` returns the coefficients that minimise squared error. Build a matrix with columns 1, x, x squared, up to the degree, and solve it with `torch.linalg.lstsq`.
- `predict_polynomial(coefs, x)` returns the fitted values.

Done when `uv run pytest week-01` passes in full (14 tests).

### Step 5: the overfitting chart (1 hour, laptop)

Reproduce Bishop's figure 1.5. Make 10 training points and 100 test points of sin(2 pi x) plus noise. Fit degrees 0 to 9 with your `fit_polynomial`, and plot training and test RMSE against degree. Save the chart in `week-01/`.

Done when the chart shows test error rising at high degree while training error keeps falling.

### Step 6: the three forecasts (2.5 hours, laptop)

1. Load `data/gb_imbalance.parquet` with pandas, and put the prices in a PyTorch tensor.
2. Split it once: the last 61 days are the test set and stay unscored until week 12. Everything before is validation.
3. Decide how to handle the two days without 48 periods (26 October 2025 has 50, 29 March 2026 has 46). Write the decision in `notes.md`.
4. Forecast every validation day three ways:
   - Last known: all 48 periods of D get the last price published before 12:00 UTC on D-1.
   - Two days back: period p of D gets period p of D-2.
   - A week back: period p of D gets period p of D-7.
5. Score each with your `mae` and `rmse`, and add one row per rule to `experiments.md`.

Done when `experiments.md` has three rows and you know which rule is best.

### Step 7: write up and publish (2 hours, Sunday)

Fill in `writeup.md` with the overfitting chart, a chart of one validation week (actual price against the best rule), and the three scores. Then commit and push:

```bash
git add -A && git commit -m "Week 1: backtest, curve fit and baselines" && git push
```

## Done by Sunday 25 October

| Check | Where |
|---|---|
| 14 tests pass | `uv run pytest week-01` |
| Overfitting chart saved | `week-01/` |
| Three baselines scored | `experiments.md` |
| Notes, with the clock-change decision | `week-01/notes.md` |
| Write-up with both charts | `week-01/writeup.md` |
| Everything pushed | github.com/watsonam/ml-study |

If the week goes badly, do steps 0 and 3 only.

## Questions to answer in your notes

- Why is "same period one day back" not one of the three rules? Think about what is published by 12:00 UTC on D-1.
- 12:00 UTC is 13:00 UK time in summer. Which settlement period is the last one known at the cut-off, and does it change with the season?
