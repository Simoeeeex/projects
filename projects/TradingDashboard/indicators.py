import pandas as pd
import numpy as np

def add_ema_rsi(df, ema_short=50, ema_long=200, rsi_period=14):
    """
    Add EMA (short & long) and RSI to the dataframe
    df: DataFrame with 'close' column
    Returns df with new columns: ema_short, ema_long, rsi
    """
    df = df.copy()
    
    # EMA
    df[f"ema_{ema_short}"] = df["close"].ewm(span=ema_short, adjust=False).mean()
    df[f"ema_{ema_long}"] = df["close"].ewm(span=ema_long, adjust=False).mean()
    
    # RSI
    delta = df["close"].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    
    avg_gain = gain.rolling(window=rsi_period, min_periods=1).mean()
    avg_loss = loss.rolling(window=rsi_period, min_periods=1).mean()
    
    rs = avg_gain / avg_loss
    df["rsi"] = 100 - (100 / (1 + rs))
    
    return df

