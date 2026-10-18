# Week 04: How does today's price depend on yesterday's?

## Reading (3 hours)

Hyndman chapter 2 (time series graphics), chapter 3 (decomposition) and chapter 9 (ARIMA): stationarity, differencing, ACF and PACF.

## From scratch (1.5 hours, AI off)

The autocorrelation function in PyTorch, checked against statsmodels' `acf`. Then an autoregressive model fitted by least squares on lagged values.

## Experiment (3.5 hours)

Plot the ACF of half-hourly prices out to 7 days (336 lags), and of daily mean prices out to 30 days. Fit AutoARIMA from statsforecast to daily means and compare it with your AR model in the backtest. Then do problem set 1: two hours on paper, AI off, from Blitzstein and Hwang chapters 1 to 4 (counting, conditional probability, random variables, expectation).

## Write-up (2 hours)

`writeup.md`, using the same headings as week 1.

## The fiddly bit

The forecast for D is made at 12:00 on D-1, so period 1 of D is 11 hours ahead and period 48 is 35 hours ahead. A one-step AR model has to be run forward many steps, and its errors grow with the horizon.
