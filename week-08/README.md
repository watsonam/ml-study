# Week 08: How uncertain is the price?

## Reading (3 hours)

Hyndman section 5.9 (distributional accuracy: quantile scores, Winkler score, CRPS). The arch documentation on univariate volatility models, for GARCH: https://arch.readthedocs.io/en/latest/univariate/introduction.html

## From scratch (1.5 hours, AI off)

Pinball loss as a PyTorch function, and a linear quantile regression trained on it with three outputs (10th, 50th, 90th percentiles). Split-conformal intervals around any point forecast. Then GARCH(1,1) fitted by maximum likelihood with autograd, checked against the `arch` package.

## Experiment (3.5 hours)

Report pinball loss and the share of actual prices inside each 80% interval. Fit GARCH to the residuals of your best point forecast, and check whether high-volatility days cluster. Then do problem set 2: Blitzstein and Hwang chapters 5 to 7 (continuous distributions, moments, joint distributions).

## Write-up (2 hours)

`writeup.md`, using the same headings as week 1.

## The fiddly bit

Conformal intervals assume the calibration days look like the test days. Price regimes shift, so check coverage month by month.
