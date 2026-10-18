# Week 09: Does a neural net help here?

## Reading (3 hours)

Karpathy videos 2 (makemore, bigrams) and 3 (MLP).

## From scratch (1.5 hours, AI off)

An MLP training loop in PyTorch without `nn.Module`: tensors for the weights, a manual forward pass, `loss.backward()` and an optimiser step.

## Experiment (3.5 hours)

Train an MLP that takes the last week of known prices and outputs 48 prices for day D. Compare it with LightGBM.

## Write-up (2 hours)

`writeup.md`, using the same headings as week 1.

## The fiddly bit

Neural nets need scaled inputs and targets. Undo the scaling before scoring, or the MAE is meaningless.
