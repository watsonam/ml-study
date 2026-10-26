import torch


def rolling_origin_splits(
    n_days: int, initial: int, horizon: int = 1, step: int = 1
) -> list[tuple[torch.Tensor, torch.Tensor]]:
    origins = range(initial, n_days - horizon + 1, step)
    return [(torch.arange(origin), torch.arange(origin, origin + horizon)) for origin in origins]


def mae(y: torch.Tensor, y_hat: torch.Tensor) -> float:
    y_error = abs(y - y_hat)
    return y_error.mean().item()


def rmse(y: torch.Tensor, y_hat: torch.Tensor) -> float:
    y_error = (y-y_hat)**2
    return (y_error.mean().item())**0.5
