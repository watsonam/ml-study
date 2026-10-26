import marimo

__generated_with = "0.25.1"
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


    return


@app.cell
def _():
    from backtest import rolling_origin_splits
    rolling_origin_splits(30, initial=10, horizon=2, step=3)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
