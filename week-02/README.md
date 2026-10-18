# Week 02: What is known at forecast time?

## Reading (3 hours)

ISLP chapter 2, sections 2.1 to 2.3 (lab). Conceptual exercises 1, 2, 3, 5 and 7 go in `notes.md`; applied exercises 8 and 9 start from `applied.py`. Maths: Bishop 1.2 (probability theory), about 30 minutes.

## From scratch (1.5 hours, AI off)

Build the lag features as tensor slices. `torch.roll` wraps the end of the series round to the start, so try it once and watch the leakage test catch it.

## Experiment (3.5 hours)

List every input you could use (lagged prices, NIV, day of week, period, holidays) and mark each as known or not known at the cut-off. Add the known ones to the baseline table as features for next week.

## Write-up (2 hours)

`writeup.md`, using the same headings as week 1.

## The fiddly bit

Elexon publishes the imbalance price shortly after each period, but it is revised later. The price you trained on may not be the price that was visible at 12:00.
