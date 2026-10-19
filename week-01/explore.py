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
    return (imbalance,)


@app.cell
def _(imbalance):
    imbalance
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
