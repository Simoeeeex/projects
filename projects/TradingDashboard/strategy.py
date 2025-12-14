def generate_signals(df):
    """
    Generate buy/sell/hold signals based on EMA + RSI
    df: DataFrame with columns ema_50, ema_200, rsi
    Returns df with new column: signal
    """
    df = df.copy()
    signals = []

    for i, row in df.iterrows():
        if row["ema_50"] > row["ema_200"] and row["rsi"] < 30:
            signals.append("BUY")
        elif row["ema_50"] < row["ema_200"] and row["rsi"] > 70:
            signals.append("SELL")
        else:
            signals.append("HOLD")

    df["signal"] = signals
    return df

