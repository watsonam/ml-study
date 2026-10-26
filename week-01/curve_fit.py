import torch


def fit_polynomial(x: torch.Tensor, y: torch.Tensor, degree: int) -> torch.Tensor:
    ...


def predict_polynomial(coefs: torch.Tensor, x: torch.Tensor) -> torch.Tensor:
    ...
