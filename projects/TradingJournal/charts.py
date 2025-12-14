import matplotlib.pyplot as plt
from analyzer import load_trades, equity_curve

def plot_equity():
    df = load_trades()
    equity = equity_curve(df)

    plt.figure(figsize=(10,5))
    plt.plot(equity)
    plt.title("Equity Curve")
    plt.xlabel("Trades")
    plt.ylabel("Balance")
    plt.grid(True)
    plt.show()

def plot_profit_distribution():
    df = load_trades()

    plt.figure(figsize=(8,4))
    plt.hist(df["profit"], bins=20)
    plt.title("Profit Distribution")
    plt.xlabel("Profit")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()

