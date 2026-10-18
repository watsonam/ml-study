# ML study

Twelve weeks of classical machine learning and forecasting at 10 hours a week. Each week has 6 hours of book and exercises, 3 hours of project work on balancing data, and 1 hour of notes.

## Rules

- Do exercises with AI assistance turned off. Check answers afterwards.
- Write notes in your own words, one `notes.md` per week.
- Redo one old exercise each week from memory.

## Plan

| Week | Study | Project |
|---|---|---|
| 01 | ISLP chapter 2: statistical learning | Pick one area and pull a year of imbalance prices |
| 02 | ISLP chapter 3: linear regression | Naive baseline and linear regression forecast |
| 03 | ISLP chapters 4 and 5: classification, resampling | Time-ordered cross-validation for the forecast |
| 04 | ISLP chapters 6 and 8: regularisation, trees | Gradient boosting forecast |
| 05 | Hyndman chapters 1 to 5: graphics, decomposition, toolbox | Plot and decompose the price series |
| 06 | Hyndman chapters 7 and 8: regression, exponential smoothing | Exponential smoothing against the boosting model |
| 07 | Hyndman chapter 9: ARIMA | Prediction intervals, scored on held-out months |
| 08 | Karpathy video 1: micrograd, with CS231n backprop notes | Write micrograd from memory |
| 09 | Karpathy video 2: makemore bigrams | Small neural network forecast |
| 10 | Karpathy videos 3 and 4: MLP, activations | Tune the neural network |
| 11 | Karpathy video 5: backprop by hand; Chronos | Chronos forecast on the same data |
| 12 | Review | Deploy the best model next to the app |

## Setup

```bash
uv sync
```

```bash
uv run jupyter lab
```

## Sources

- ISLP: https://www.statlearning.com
- Hyndman, Forecasting: Principles and Practice: https://otexts.com/fpp3/
- Karpathy, Neural Networks: Zero to Hero: https://karpathy.ai/zero-to-hero.html
- CS231n backprop notes: https://cs231n.github.io/optimization-2/
- Alisa Liu, job search: https://alisawuffles.github.io/blog/job-search/
