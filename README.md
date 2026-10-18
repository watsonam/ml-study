# ML study

Twelve weeks of classical machine learning and forecasting at 10 hours a week, organised around one problem: forecasting the GB imbalance price for tomorrow.

## Objectives

1. Understand classical ML and forecasting well enough to explain and derive the core methods.
2. Work the way an ML engineer does: evaluation first, baselines, leakage checks, one change per experiment, error analysis, and a decision on whether to ship.
3. Produce a backtested imbalance price forecast that could be deployed next to the balancing-services platform.

Writing ML code fluently in PyTorch, without AI, supports all three. Every week uses PyTorch, from tensors in week 1 to `nn.Module` and `DataLoader` in week 10.

## Success criteria at week 12

| Objective | Check |
|---|---|
| Understanding | You can explain each week's method in five sentences and redo its from-scratch piece from a blank file |
| Engineering habits | `experiments.md` holds about 12 logged experiments, each with one change and its numbers |
| Useful output | One table compares every model against the baseline on months the models never saw, with MAE, pinball loss and interval coverage |
| Coding fluency | You pass the three timed 45-minute drills in weeks 4, 8 and 12 without AI |

## The problem

At 12:00 UTC on day D-1, forecast the GB imbalance price for each of the 48 half-hour settlement periods of day D. Score the forecast on days the model has never seen.

## Weekly loop

| Part | Hours | Output |
|---|---|---|
| Reading | 3 | `week-NN/notes.md`, in your own words |
| Experiment | 3.5 | One change against last week's best, logged in `experiments.md` |
| From scratch | 1.5 | The method you used, in PyTorch or numpy, with AI off, passing the week's tests |
| Write-up | 2 | `week-NN/writeup.md`, posted to watsonam.github.io on Sunday |

Reading, the Bishop maths sections and flashcards suit the Monday and Wednesday commute on the iPad or phone. Bishop's Pattern Recognition and Machine Learning is on Google Drive. Coding needs the laptop. Watch a Karpathy video once without coding, then write the code from memory later.

## Rules

- Do the from-scratch piece and the drills with AI assistance turned off.
- Change one thing per experiment, and log every experiment, including the ones that made things worse.
- Never look at the test months while choosing a model.
- If a week slips, do the from-scratch piece only. Never two weeks in a row with no commits.

## The twelve questions

| Week | Question | Reading | From scratch | PyTorch skills |
|---|---|---|---|---|
| 01 | How will I know a forecast is good? | Hyndman ch 5; Bishop 1.1 | Rolling-origin backtest, MAE and RMSE, and three naive baselines | Tensors, dtypes, indexing, `view` a year as days by 48 periods, broadcasting |
| 02 | What is known at forecast time? | ISLP ch 2; Bishop 1.2 | Lag features that respect the 12:00 cut-off, and a leakage test that fails on purpose | Slicing and shifting tensors; why `torch.roll` leaks |
| 03 | Can a linear model beat the baseline? | ISLP ch 3 and 6; Bishop 3.1 | Least squares, then ridge by gradient descent | `torch.linalg.lstsq`, `requires_grad`, `backward()`, a manual update, then `torch.optim.SGD` |
| 04 | Where does it fail? | none | Error slices by period, weekday, month and price spikes; timed drill 1 | Boolean masks, `index_add_` for group means |
| 05 | Can trees catch the spikes, and can I predict a spike? | ISLP ch 4.3 and 8; Bishop 4.3 | Logistic regression for "will D have a spike?", and one decision tree split | Sigmoid, binary cross-entropy against `F.binary_cross_entropy_with_logits`, `cumsum` for split search |
| 06 | How sure is the forecast? | Hyndman 5.9 | Pinball loss, quantile regression trained on it, and split-conformal intervals | A custom loss function, several outputs from one model |
| 07 | Is the ML model better than classical statistics? | Hyndman ch 8 and 9 | Holt-Winters exponential smoothing with parameters fitted by autograd | A recursive forward pass, `torch.optim.Adam`, constraining parameters with `sigmoid` |
| 08 | How does a neural net learn? | Karpathy video 1, CS231n backprop notes; Bishop 5.3 | Micrograd in numpy, with gradients checked against PyTorch autograd; timed drill 2 | Autograd internals, `torch.autograd.grad`, gradient checking |
| 09 | Does a neural net help here? | Karpathy videos 2 and 3 | MLP training loop without `nn.Module`; SGD with momentum and Adam written by hand | Weight tensors, `no_grad`, writing an optimiser, learning rate schedules |
| 10 | Why won't it train? | Karpathy video 4 | BatchNorm, three broken runs to diagnose, then a rewrite with `nn.Module` | `nn.Module`, `Dataset`, `DataLoader`, `train()` and `eval()`, `state_dict` save and load |
| 11 | Does a pretrained model beat mine without training? | Hyndman ch 15 | Chronos's scaling and binning of a series into tokens | Loading a pretrained model, inference on a batch, `torch.inference_mode` |
| 12 | Would I ship it? | none | Model card, drift check, three earlier pieces redone from blank; timed drill 3 | Loading the saved model in a fresh process and serving one forecast |

## After week 12

Deploy the best model next to the platform. Sit the AWS Certified Machine Learning Engineer Associate exam in week 14, and enter a Kaggle time series competition with the week 12 model.

## Setup

```bash
uv sync
```

```bash
uv run python fetch.py
```

```bash
uv run jupyter lab
```

`fetch.py` downloads a year of GB imbalance prices from Elexon into `data/gb_imbalance.parquet`. Elexon's API needs no key.

## Sources

- ISLP: https://www.statlearning.com
- Hyndman et al., Forecasting: Principles and Practice, the Pythonic Way: https://otexts.com/fpppy/
- Karpathy, Neural Networks: Zero to Hero: https://karpathy.ai/zero-to-hero.html
- Bishop, Pattern Recognition and Machine Learning (on Google Drive)
- CS231n backprop notes: https://cs231n.github.io/optimization-2/
- Alisa Liu, job search: https://alisawuffles.github.io/blog/job-search/
