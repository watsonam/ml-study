import math

import pytest
import torch
from sklearn.metrics import mean_absolute_error, mean_squared_error

from backtest import mae, rmse, rolling_origin_splits


def test_training_always_ends_before_testing():
    for train, test in rolling_origin_splits(30, initial=10, horizon=2, step=3):
        assert max(train) < min(test)


def test_first_fold_uses_initial_days():
    train, test = rolling_origin_splits(30, initial=10)[0]
    assert list(train) == list(range(10))
    assert list(test) == [10]


def test_training_window_grows_by_step():
    folds = rolling_origin_splits(30, initial=10, step=5)
    sizes = [len(train) for train, _ in folds]
    assert all(b - a == 5 for a, b in zip(sizes, sizes[1:]))


def test_no_fold_runs_past_the_end():
    folds = rolling_origin_splits(30, initial=10, horizon=3)
    assert max(max(test) for _, test in folds) == 29
    assert all(len(test) == 3 for _, test in folds)


def test_fold_count():
    assert len(rolling_origin_splits(30, initial=10)) == 20


@pytest.mark.parametrize("seed", [0, 1, 2])
def test_metrics_match_sklearn(seed):
    g = torch.Generator().manual_seed(seed)
    y, y_hat = torch.randn(100, generator=g) * 50, torch.randn(100, generator=g) * 50
    assert math.isclose(mae(y, y_hat), mean_absolute_error(y, y_hat), rel_tol=1e-5)
    assert math.isclose(rmse(y, y_hat), mean_squared_error(y, y_hat) ** 0.5, rel_tol=1e-5)
