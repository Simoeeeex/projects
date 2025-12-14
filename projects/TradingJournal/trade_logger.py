import csv
from datetime import datetime
import os

FILE_PATH = "data/trades.csv"

HEADERS = [
    "date_time",
    "symbol",
    "side",
    "entry",
    "exit",
    "qty",
    "strategy",
    "bias",
    "risked",
    "profit"
]

def init_journal():
    if not os.path.exists(FILE_PATH) or os.stat(FILE_PATH).st_size == 0:
        with open(FILE_PATH, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(HEADERS)

def log_trade(symbol, side, entry, exit_price, qty, strategy, bias, risked):
    profit = (
        (exit_price - entry) * qty
        if side.upper() == "BUY"
        else (entry - exit_price) * qty
    )

    row = [
        datetime.now().strftime("%Y-%m-%d %H:%M"),
        symbol,
        side.upper(),
        entry,
        exit_price,
        qty,
        strategy,
        bias,
        risked,
        round(profit, 2)
    ]

    with open(FILE_PATH, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(row)

    print("✅ Trade logged:", row)

