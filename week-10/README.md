# Week 10: How does a neural net learn?

## Reading (3 hours)

Karpathy, Neural Networks: Zero to Hero, video 1 (micrograd) and video 2 (makemore, bigrams). The CS231n backprop notes help with video 1: https://cs231n.github.io/optimization-2/

## From scratch (1.5 hours, AI off)

Micrograd from memory: a scalar value class with add, multiply, tanh and backward, with gradients checked against PyTorch autograd. Then a small MLP in PyTorch: weight tensors, a forward pass, `loss.backward()` and an optimiser step.

## Experiment (3.5 hours)

Train the MLP on `features.py` to predict day D's 48 prices, and compare it with LightGBM and ridge in the backtest.

## Write-up (2 hours)

`writeup.md`, using the same headings as week 1.

## The fiddly bit

Gradients add up when a value is used twice, so forgetting `+=` is the classic micrograd bug. Scale inputs and targets for the MLP, and undo the scaling before scoring.
