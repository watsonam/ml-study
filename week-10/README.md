# Week 10: Why won't it train?

## Reading (3 hours)

Karpathy video 4 (activations, gradients, BatchNorm).

## From scratch (1.5 hours, AI off)

BatchNorm forward and backward in numpy, checked against PyTorch. Then rewrite the week 9 model with `nn.Module`, a `Dataset` and a `DataLoader`, and save and reload it with `state_dict`.

## Experiment (3.5 hours)

Break your week 9 model three ways (learning rate too high, bad initialisation, no scaling). Diagnose each from the loss curve and activation statistics alone.

## Write-up (2 hours)

`writeup.md`, using the same headings as week 1.

## The fiddly bit

BatchNorm behaves differently in training and evaluation. Scoring in training mode gives the wrong numbers.
