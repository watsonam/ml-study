# Week 05: Can I predict a spike?

## Reading (3 hours)

ISLP chapter 4 (classification): logistic regression, discriminant analysis, and how to judge a classifier.

## From scratch (1.5 hours, AI off)

Logistic regression in PyTorch: weights as tensors, sigmoid, and binary cross-entropy written by hand, checked against `F.binary_cross_entropy_with_logits` and scikit-learn's `LogisticRegression`. Then an ROC curve and its area, computed by sorting the scores.

## Experiment (3.5 hours)

Define a spike day as one with any period above the 95th percentile of the training fold. Predict it from inputs known at 12:00 on D-1. Report the area under the ROC curve, and a calibration table (predicted probability against observed rate, in ten bins).

## Write-up (2 hours)

`writeup.md`, using the same headings as week 1.

## The fiddly bit

Computing the 95th percentile on the whole year leaks the future into the label. Compute it on each training fold. Spike days are rare, so accuracy alone says little: always predicting "no spike" is right most of the time.
