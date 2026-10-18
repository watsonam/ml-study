# Week 03: Can a linear model beat the baseline?

## Reading (3 hours)

ISLP chapter 3 (linear regression) and chapter 6, sections 6.1 and 6.2 (ridge and lasso). Maths: Bishop 3.1 (linear basis function models), about 30 minutes.

## From scratch (1.5 hours, AI off)

Solve least squares with `torch.linalg.lstsq`. Then fit the same model by gradient descent: weights with `requires_grad=True`, `loss.backward()`, a manual update inside `torch.no_grad()`, and `grad.zero_()`. Finally swap the manual update for `torch.optim.SGD` and add the ridge penalty. Check all three against scikit-learn's `Ridge`.

## Experiment (3.5 hours)

Fit linear regression, then ridge, on week 2's features. Score both in the backtest against the best baseline.

## Write-up (2 hours)

`writeup.md`, using the same headings as week 1.

## The fiddly bit

Ridge penalises large weights, so features on bigger scales are penalised less. Standardise using statistics from the training fold only.
