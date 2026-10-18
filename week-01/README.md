# Week 01: How will I know a forecast is good?

Before any model, build the thing that scores models. Every later week plugs into it.

## Reading (3 hours)

Hyndman, Forecasting: Principles and Practice, the Pythonic Way, chapter 5 (the forecaster's toolbox): https://otexts.com/fpppy/

Focus on the simple methods (5.2), residuals (5.3 and 5.4), forecast accuracy measures (5.8) and time series cross-validation (5.10). Leave 5.9 (distributional accuracy) for week 6.

## The setup

Run `uv run python fetch.py` from the repo root. It writes `data/gb_imbalance.parquet`: one row per half-hour, with `start_utc`, `settlement_date`, `period` (1 to 48), `price` (GBP/MWh) and `niv` (net imbalance volume, MWh).

The forecast is made at 12:00 UTC on day D-1, for all periods of day D.

Split the year once, now, and do not change it:

- Validation: everything before the last 61 days. Backtest and compare models here.
- Test: the last 61 days. Do not score anything on it until week 12.

## From scratch (1.5 hours, AI off)

Write `week-01/backtest.py` so that `uv run pytest week-01` passes. It needs:

- `rolling_origin_splits(n_days, initial, horizon=1, step=1)` returns a list of `(train_idx, test_idx)` pairs of day indices. Training always ends before testing starts, and the training window grows by `step` each fold.
- `mae(y, y_hat)` and `rmse(y, y_hat)` take PyTorch tensors and return a float.

Use PyTorch tensors throughout, so the syntax becomes familiar from week 1.

## Experiment (3.5 hours)

Build three baselines and score each one with your backtest over the validation period:

- Last known: every period of D gets the last price published before 12:00 on D-1.
- Same period two days back: period p of D gets period p of D-2.
- Same period a week back: period p of D gets period p of D-7.

Log each one as a row in `experiments.md`. The best of the three is the number every model must beat from now on.

## Write-up (2 hours)

Fill in `writeup.md`. Include one chart of a validation week with the actual price and the best baseline.

## The fiddly bit

Two days a year do not have 48 periods. In this year of data, 26 October 2025 has 50 and 29 March 2026 has 46, because of the clock changes. Decide how your backtest and the "same period" baselines handle them, and write the decision down. Also check why "same period one day back" is missing from the list above, and what a 12:00 cut-off means for it.
