# Week 03: Can a linear model beat the baseline, and which inputs matter?

## Reading (3 hours)

ISLP chapter 3 (linear regression) and section 6.2 (ridge and lasso).

## From scratch (1.5 hours, AI off)

Least squares in PyTorch with `torch.linalg.lstsq`, plus standard errors from the residual variance and the inverse of X transpose X. Check the coefficients and standard errors against statsmodels' `OLS`. Then ridge, solved in closed form.

## Experiment (3.5 hours)

Regress day D's price on same period D-2, same period D-7, period of day and weekday, using only training folds. Read the coefficient table: which inputs matter, and by how much? Score linear regression and ridge in the backtest against the best baseline.

## Write-up (2 hours)

`writeup.md`, using the same headings as week 1.

## The fiddly bit

The residuals are autocorrelated, so the textbook standard errors are too small. Compare them with statsmodels' heteroskedasticity and autocorrelation consistent (HAC) standard errors, and note which conclusions change.
