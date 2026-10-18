# Week 02: What do imbalance prices look like as a distribution?

## Reading (3 hours)

ISLP chapter 2 (statistical learning), sections 2.1 to 2.3, including the lab. Bishop 1.2 (probability theory) and 2.3 (the Gaussian distribution, including the Student-t in 2.3.7), about 1 hour.

## From scratch (1.5 hours, AI off)

In PyTorch, fit a normal and a Student-t distribution to the prices by maximum likelihood: write each negative log-likelihood, and minimise it with autograd and `torch.optim.Adam`. Keep the scale positive with `exp` and the degrees of freedom above 2 with `softplus`. Then write a bootstrap that resamples days and returns a confidence interval for any statistic.

## Experiment (3.5 hours)

Plot a histogram of prices and a QQ plot against the normal. Compare the two fitted log-likelihoods. Give bootstrap 95% intervals for the mean price and the 95th percentile, overall and for the evening peak. ISLP conceptual exercises 1, 2, 3, 5 and 7 go in `notes.md`; applied exercise 8 starts from `applied.py`.

## Write-up (2 hours)

`writeup.md`, using the same headings as week 1.

## The fiddly bit

Prices go negative, so a log transform is impossible. The bootstrap also assumes independent draws, and half-hours on the same day are not independent, which is why it resamples whole days.
