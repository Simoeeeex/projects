import yfinance as yf
import pandas as pd

def fetch_data(symbol, interval="1h", period="30d"):
    """
    Fetch OHLC data for crypto or forex using yfinance
    """
    try:
        df = yf.download(
            symbol,
            interval=interval,
            period=period,
            progress=False
        )

        if df.empty:
            return None

        df.reset_index(inplace=True)
        df = df[["Datetime", "Open", "High", "Low", "Close", "Volume"]]
        df.columns = ["time", "open", "high", "low", "close", "volume"]

        return df

    except Exception as e:
        print("Error fetching data:", e)
        return None

