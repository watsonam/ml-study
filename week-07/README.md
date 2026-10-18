# Week 07: Do trees do better?

## Reading (3 hours)

ISLP chapter 8 (trees, bagging, random forests, boosting).

## From scratch (1.5 hours, AI off)

One decision tree split in PyTorch: given a feature column and targets, find the threshold that most reduces squared error, using `cumsum` to score every threshold at once.

## Experiment (3.5 hours)

Add LightGBM (`uv add lightgbm`) and train it on `features.py`. Compare it with ridge overall and on the spike slice from week 6, and read its feature importances.

## Write-up (2 hours)

`writeup.md`, using the same headings as week 1.

## The fiddly bit

Trees cannot predict outside the range of prices they were trained on. Check what happens on the highest-priced days.
