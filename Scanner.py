import yfinance as yf
import pandas as pd
from ta.momentum import RSIIndicator

def fetch_data(symbol):
    df = yf.download(symbol, period="5d", interval="5m")
    if len(df) < 50:
        return None

    df['EMA20'] = df['Close'].ewm(span=20).mean()
    df['EMA50'] = df['Close'].ewm(span=50).mean()
    df['RSI'] = RSIIndicator(df['Close'], 14).rsi()
    df['VolAvg'] = df['Volume'].rolling(20).mean()

    return df
