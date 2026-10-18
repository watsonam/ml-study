# Week 09: What shapes do daily prices take?

## Reading (3 hours)

ISLP chapter 12 (unsupervised learning): principal components analysis and clustering.

## From scratch (1.5 hours, AI off)

PCA in PyTorch with `torch.linalg.svd` on the centred days-by-48 price matrix, checked against scikit-learn's `PCA`. Then k-means from scratch.

## Experiment (3.5 hours)

Plot the first three components as 48-period curves and name what each one describes (for example level, or the evening peak). Cluster the days into four to six groups, and compare the clusters with weekday and season. Try the component scores as features in your best model.

## Write-up (2 hours)

`writeup.md`, using the same headings as week 1.

## The fiddly bit

PCA is sensitive to scale and to outliers, and a few spike days can take over the first component. Compare the components with and without the top 1% of days.
