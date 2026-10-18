import numpy as np
import pytest
import torch

from curve_fit import fit_polynomial, predict_polynomial


@pytest.mark.parametrize("degree", [0, 1, 3, 9])
def test_fit_matches_numpy(degree):
    g = torch.Generator().manual_seed(degree)
    x = torch.linspace(0, 1, 10, dtype=torch.float64)
    y = torch.sin(2 * torch.pi * x) + 0.3 * torch.randn(10, generator=g, dtype=torch.float64)
    ours = predict_polynomial(fit_polynomial(x, y, degree), x)
    theirs = np.polyval(np.polyfit(x.numpy(), y.numpy(), degree), x.numpy())
    assert np.allclose(ours.numpy(), theirs, atol=1e-6)


def test_degree_nine_passes_through_ten_points():
    x = torch.linspace(0, 1, 10, dtype=torch.float64)
    y = torch.sin(2 * torch.pi * x)
    fitted = predict_polynomial(fit_polynomial(x, y, 9), x)
    assert torch.allclose(fitted, y, atol=1e-6)


def test_training_error_never_rises_with_degree():
    g = torch.Generator().manual_seed(0)
    x = torch.linspace(0, 1, 10, dtype=torch.float64)
    y = torch.sin(2 * torch.pi * x) + 0.3 * torch.randn(10, generator=g, dtype=torch.float64)
    errors = [((predict_polynomial(fit_polynomial(x, y, d), x) - y) ** 2).mean().item() for d in range(10)]
    assert all(b <= a + 1e-9 for a, b in zip(errors, errors[1:]))
