# Week 06: Am I fooling myself?

## Reading (3 hours)

ISLP chapter 5 (resampling methods): cross-validation and the bootstrap.

## From scratch (1.5 hours, AI off)

`features.py`: lag features for day D built only from data published before 12:00 UTC on D-1. Write a test that builds a feature from the D-1 afternoon on purpose and fails. Then a function that slices backtest errors by period of day, weekday, month and spike days.

## Experiment (3.5 hours)

Rebuild weeks 3 and 5 on `features.py`, and check whether any score drops. Find the three slices where the best model is worst, and write one hypothesis for each.

## Write-up (2 hours)

`writeup.md`, using the same headings as week 1.

## The fiddly bit

Elexon revises imbalance prices after first publishing them. The price you train on may not be the price that was visible at 12:00 on D-1.
