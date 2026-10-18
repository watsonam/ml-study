# Week 11: Does a neural net or Chronos beat the rest, really?

## Reading (3 hours)

Hyndman chapter 15 (foundation forecasting models): https://otexts.com/fpppy/15-foundation-models.html. Diebold and Mariano (1995), Comparing Predictive Accuracy, or a summary of it.

## From scratch (1.5 hours, AI off)

The Diebold-Mariano test in PyTorch: the loss difference between two forecasts, its mean, and an autocorrelation-robust variance.

## Experiment (3.5 hours)

Run Chronos zero-shot through the same backtest (`uv add chronos-forecasting`). Test every pair of models with Diebold-Mariano, and mark which differences are real.

## Write-up (2 hours)

`writeup.md`, using the same headings as week 1.

## The fiddly bit

The 48 periods of a day are correlated, so testing on half-hourly losses overstates confidence. Test on daily mean losses. Chronos may also have been trained on public data that includes GB prices.
