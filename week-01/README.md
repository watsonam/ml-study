# Week 01: How will I know a forecast is good?

This week builds the code that scores every later model, and shows the core idea of fitting a model to data.

## Reading (3 hours)

Hyndman, Forecasting: Principles and Practice, the Pythonic Way, chapter 5 (the forecaster's toolbox): https://otexts.com/fpppy/05-toolbox.html

Focus on the simple methods (5.2), residuals (5.3 and 5.4), forecast accuracy measures (5.8) and time series cross-validation (5.10). Leave 5.9 (distributional accuracy) for week 8.

Bishop 1.1 (polynomial curve fitting), about 30 minutes. It explains fitting by minimising squared error, and overfitting, in ten pages.

## The setup

Run `uv run python fetch.py` from the repo root. It writes `data/gb_imbalance.parquet`: one row per half-hour, with `start_utc`, `settlement_date`, `period` (1 to 48), `price` (GBP/MWh) and `niv` (net imbalance volume, MWh).

The forecast is made at 12:00 UTC on day D-1, for all periods of day D.

Split the year once, now, and do not change it:

- Validation: everything before the last 61 days. Backtest and compare models here.
- Test: the last 61 days. Do not score anything on it until week 12.

## From scratch (1.5 hours, AI off)

Write two files in PyTorch only, with no pandas or numpy, so that `uv run pytest week-01` passes.

`week-01/backtest.py`:

- `rolling_origin_splits(n_days, initial, horizon=1, step=1)` returns a list of `(train_idx, test_idx)` pairs of day indices. Training always ends before testing starts, and the training window grows by `step` each fold.
- `mae(y, y_hat)` and `rmse(y, y_hat)` take tensors and return a float.

`week-01/curve_fit.py`:

- `fit_polynomial(x, y, degree)` returns the coefficients that minimise squared error. Build the design matrix (columns 1, x, x squared, up to the degree) and solve it with `torch.linalg.lstsq`.
- `predict_polynomial(coefs, x)` returns the fitted values.

The PyTorch skills this week are `torch.tensor` and `torch.arange`, dtypes (`float32` against `float64`), indexing and slicing, stacking columns into a matrix, and `.item()`.

## Experiment (3.5 hours)

First, reproduce Bishop's figure 1.5 (about 1 hour). Take 10 points of sin(2 pi x) plus noise for training and 100 for testing. Fit polynomials of degree 0 to 9 with your `fit_polynomial`, and plot training and test RMSE against degree. The test error rising while the training error falls is overfitting, and it is the reason the test months stay locked.

Then build three baselines and score each one with your backtest over the validation period:

- Last known: every period of D gets the last price published before 12:00 on D-1.
- Same period two days back: period p of D gets period p of D-2.
- Same period a week back: period p of D gets period p of D-7.

Load the parquet file with pandas, then move the prices into a tensor and `view` it as days by 48 periods. Each baseline is then one line of tensor indexing, and broadcasting scores all days at once.

Log each baseline as a row in `experiments.md`. The best of the three is the number every model must beat from now on.

## Write-up (2 hours)

Fill in `writeup.md`. Include the overfitting chart and one chart of a validation week with the actual price and the best baseline.

## The fiddly bit

Two days a year do not have 48 periods. In this year of data, 26 October 2025 has 50 and 29 March 2026 has 46, because of the clock changes. They break the days-by-48 view, so decide how your backtest and the "same period" baselines handle them, and write the decision down. Also work out why "same period one day back" is missing from the list above, and what the 12:00 cut-off means for it.
