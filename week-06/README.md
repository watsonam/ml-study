# Week 06: How sure is the forecast?

## Reading (3 hours)

Hyndman chapter 5.9 (distributional accuracy: quantile scores, Winkler score, CRPS).

## From scratch (1.5 hours, AI off)

Pinball loss for a given quantile, and split-conformal intervals around any point forecast.

## Experiment (3.5 hours)

Train LightGBM with a quantile objective for the 10th, 50th and 90th percentiles. Report pinball loss and the share of actual prices inside the 80% interval.

## Write-up (2 hours)

`writeup.md`, using the same headings as week 1.

## The fiddly bit

Conformal intervals assume the calibration days look like the test days. Price regimes shift, so check coverage month by month.
