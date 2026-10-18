# Week 08: How does a neural net learn?

## Reading (3 hours)

Karpathy, Neural Networks: Zero to Hero, video 1 (micrograd), with the CS231n backprop notes.

## From scratch (1.5 hours, AI off)

Micrograd in numpy from memory: a scalar value class with add, multiply, tanh and backward. Then timed drill 2.

## Experiment (3.5 hours)

Train your micrograd MLP on a small slice of the price data, and compare it with PyTorch on the same slice.

## Write-up (2 hours)

`writeup.md`, using the same headings as week 1.

## The fiddly bit

Gradients add up when a value is used twice. Forgetting `+=` is the classic micrograd bug.
