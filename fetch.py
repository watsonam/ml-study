import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import date, timedelta
from pathlib import Path

import pandas as pd
import requests

URL = "https://data.elexon.co.uk/bmrs/api/v1/balancing/settlement/system-prices/{}"
OUT = Path(__file__).parent / "data" / "gb_imbalance.parquet"


def fetch_day(day: date) -> list[dict]:
    resp = requests.get(URL.format(day.isoformat()), params={"format": "json"}, timeout=30)
    resp.raise_for_status()
    return resp.json()["data"]


def main(days: int = 365) -> None:
    end = date.today() - timedelta(days=1)
    dates = [end - timedelta(days=i) for i in range(days)]
    with ThreadPoolExecutor(max_workers=8) as pool:
        rows = [row for day in pool.map(fetch_day, dates) for row in day]
    df = pd.DataFrame(rows)[["startTime", "settlementDate", "settlementPeriod", "systemSellPrice", "netImbalanceVolume"]]
    df = df.rename(columns={"startTime": "start_utc", "settlementDate": "settlement_date", "settlementPeriod": "period", "systemSellPrice": "price", "netImbalanceVolume": "niv"})
    df["start_utc"] = pd.to_datetime(df["start_utc"], utc=True)
    df = df.drop_duplicates("start_utc").sort_values("start_utc").reset_index(drop=True)
    OUT.parent.mkdir(exist_ok=True)
    df.to_parquet(OUT, index=False)
    print(f"{len(df)} rows, {df.start_utc.min()} to {df.start_utc.max()}, written to {OUT}")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 365)
