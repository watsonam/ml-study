import torch


def fit_polynomial(x: torch.Tensor, y: torch.Tensor, degree: int) -> torch.Tensor:
    poly_matrix = torch.vander(x, increasing=True, N=degree+1)
    solution = torch.Tensor(torch.linalg.lstsq(poly_matrix, y).solution)
    return solution


def predict_polynomial(coefs: torch.Tensor, x: torch.Tensor) -> torch.Tensor:
    poly_matrix = torch.vander(x, increasing=True, N=coefs.shape[0])
    return poly_matrix @ coefs




