# Week 04: Where does it fail?

## Reading (3 hours)

None. This week is error analysis.

## From scratch (1.5 hours, AI off)

Compute the error slices with boolean masks and `index_add_` for the group means. Then timed drill 1: 45 minutes, no AI, for example the backward pass of a linear layer.

## Experiment (3.5 hours)

Find the three slices where the best model is worst. Write one hypothesis for each, and pick the one to test next.

## Write-up (2 hours)

`writeup.md`, using the same headings as week 1.

## The fiddly bit

The average error can improve while spike errors get worse. Decide now which matters more for the platform.
