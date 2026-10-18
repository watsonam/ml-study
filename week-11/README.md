# Week 11: Does a pretrained model beat mine without training?

## Reading (3 hours)

Hyndman, Pythonic Way, chapter 15 (foundation forecasting models).

## From scratch (1.5 hours, AI off)

Chronos's preprocessing: scale a series by its mean absolute value and bin it into tokens, then turn tokens back into prices.

## Experiment (3.5 hours)

Run Chronos zero-shot through the same backtest. Add it to the comparison table with point and interval scores.

## Write-up (2 hours)

`writeup.md`, using the same headings as week 1.

## The fiddly bit

Chronos was trained on public data that may include GB prices. A strong zero-shot score is less impressive if it has seen the series.
