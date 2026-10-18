# Week 05: Can trees catch the spikes, and can I predict a spike?

## Reading (3 hours)

ISLP chapter 8 (trees, bagging, random forests, boosting). Maths: ISLP 4.3 (logistic regression) and Bishop 4.3 (probabilistic discriminative models), about 1 hour.

## From scratch (1.5 hours, AI off)

Logistic regression in PyTorch for "will day D have a period above the 95th percentile?": a linear layer as tensors, sigmoid, and binary cross-entropy written by hand, checked against `F.binary_cross_entropy_with_logits`. Then one decision tree split, using `cumsum` to score every threshold at once.

## Experiment (3.5 hours)

Gradient boosting with LightGBM on the same features. Compare its spike slice from week 4 against ridge.

## Write-up (2 hours)

`writeup.md`, using the same headings as week 1.

## The fiddly bit

Trees cannot predict outside the range of prices they were trained on. Check what happens on the highest-priced days.
