import pandas as pd

FILE_PATH = "data/trades.csv"

def load_trades():
    return pd.read_csv(FILE_PATH)

def win_rate(df):
    wins = df[df["profit"] > 0]
    return round(len(wins) / len(df) * 100, 2) if len(df) > 0 else 0

def equity_curve(df, starting_balance=10000):
    equity = [starting_balance]
    for p in df["profit"]:
        equity.append(equity[-1] + p)
    return equity[1:]

def max_drawdown(equity):
    peak = equity[0]
    max_dd = 0
    for value in equity:
        peak = max(peak, value)
        dd = (peak - value)
        max_dd = max(max_dd, dd)
    return round(max_dd, 2)

def risk_reward(df):
    avg_win = df[df["profit"] > 0]["profit"].mean()
    avg_loss = abs(df[df["profit"] < 0]["profit"].mean())
    if avg_loss == 0:
        return 0
    return round(avg_win / avg_loss, 2)

def summary():
    df = load_trades()
    if df.empty:
        print("No trades yet.")
        return

    equity = equity_curve(df)

    print("\n=== TRADING JOURNAL STATS ===")
    print(f"Total Trades: {len(df)}")
    print(f"Win Rate: {win_rate(df)}%")
    print(f"Net Profit: ${round(df['profit'].sum(), 2)}")
    print(f"Risk/Reward: {risk_reward(df)}")
    print(f"Max Drawdown: ${max_drawdown(equity)}")

