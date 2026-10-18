# Week 07: Is the ML model better than classical statistics?

## Reading (3 hours)

Hyndman chapter 8 (exponential smoothing) and chapter 9 (ARIMA).

## From scratch (1.5 hours, AI off)

Holt-Winters as a PyTorch recursion over the series. Fit its three smoothing parameters with `torch.optim.Adam`, keeping each between 0 and 1 by passing an unconstrained tensor through `sigmoid`.

## Experiment (3.5 hours)

Fit ETS and ARIMA with statsforecast. Add them to the comparison table with point and interval scores.

## Write-up (2 hours)

`writeup.md`, using the same headings as week 1.

## The fiddly bit

A 48-period season on a year of data is a lot of parameters for ETS. Compare against a model on daily averages.
