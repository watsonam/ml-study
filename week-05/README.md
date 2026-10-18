# Week 05: Can trees catch the spikes?

## Reading (3 hours)

ISLP chapter 8 (trees, bagging, random forests, boosting).

## From scratch (1.5 hours, AI off)

One decision tree split: given a feature column and targets, find the threshold that most reduces squared error.

## Experiment (3.5 hours)

Gradient boosting with LightGBM on the same features. Compare its spike slice from week 4 against ridge.

## Write-up (2 hours)

`writeup.md`, using the same headings as week 1.

## The fiddly bit

Trees cannot predict outside the range of prices they were trained on. Check what happens on the highest-priced days.
