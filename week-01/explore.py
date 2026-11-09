import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    import polars as pl
    from pathlib import Path
    DATA_FOLDER = Path(__file__).parent.parent / "data"
    if not DATA_FOLDER.exists():
        raise FileNotFoundError(f"Data folder not found: {DATA_FOLDER}")
    return DATA_FOLDER, pl


@app.cell
def _(DATA_FOLDER, pl):
    imbalance = pl.read_parquet(DATA_FOLDER / "gb_imbalance.parquet")
    return


@app.cell
def _():
    ## if (n_days: int, initial: int, horizon: int = 1, step: int = 1)
    import torch
    n_days = 30
    initial = 10
    horizon = 2
    step = 3

    cv_splits = [torch.arange(0, initial), torch.arange(initial,initial+ horizon)]
    print(cv_splits)
    fold_start = initial
    while fold_start < (n_days - 1) - horizon:
        split = [torch.arange(0, fold_start + step), torch.arange(fold_start + step,fold_start + step + horizon)]
        cv_splits.append(split)
        print(split)
        fold_start += step
    return (torch,)


@app.cell
def _():
    from backtest import rolling_origin_splits
    rolling_origin_splits(30, initial=10, horizon=2, step=3)
    return


@app.cell
def _(torch):
    x = torch.linspace(0, 1, 10, dtype=torch.float64)
    y = torch.sin(2 * torch.pi * x)

    # fit_polynomial(x, y, degree) returns the coefficients that minimise squared error. Build a matrix with columns 1, x, x squared, up to the degree, and solve it with torch.linalg.lstsq.
    # for x in range(1,degree)
    return x, y


@app.cell
def _(torch, x):

    degree = 0
    degree += 1
    poly_matrix = torch.vander(x, increasing=True, N=degree)
    return (poly_matrix,)


@app.cell
def _(poly_matrix, torch, y):
    coefs = torch.linalg.lstsq(poly_matrix, y).solution
    return (coefs,)


@app.cell
def _(poly_matrix, torch, y):
    new_degree = torch.Tensor(torch.linalg.lstsq(poly_matrix, y).solution).shape[0]
    return


@app.cell
def _(coefs, torch, x):
    torch.vander(x, increasing=True, N=coefs.shape[0]) @ coefs
    return


@app.cell
def _(poly_matrix):
    poly_matrix
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
