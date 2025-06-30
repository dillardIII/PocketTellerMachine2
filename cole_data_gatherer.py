from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: cole_data_gatherer.py ===

import yfinance as yf
import pandas as pd
import numpy as np

# === Pull historical price data ===
def get_price_data(symbol="AAPL", period="6mo", interval="1d"):
    print(f"[DataGatherer] Pulling data for {symbol}...")
    data = yf.download(symbol, period=period, interval=interval)
    data.dropna(inplace=True)
    return data

# === Calculate RSI ===
def calc_rsi(data, window=14):
    delta = data['Close'].diff().to_numpy().flatten()
    gain = np.where(delta > 0, delta, 0)
    loss = np.where(delta < 0, -delta, 0)
    avg_gain = pd.Series(gain).rolling(window=window).mean()
    avg_loss = pd.Series(loss).rolling(window=window).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    data['RSI'] = rsi
    return data

# === Calculate MACD ===
def calc_macd(data):
    ema12 = data['Close'].ewm(span=12, adjust=False).mean()
    ema26 = data['Close'].ewm(span=26, adjust=False).mean()
    macd_line = ema12 - ema26
    signal_line = macd_line.ewm(span=9, adjust=False).mean()
    data['MACD'] = macd_line
    data['Signal'] = signal_line
    return data

# === Calculate Bollinger Bands ===
def calc_bollinger(data, window=20):
    sma = data['Close'].rolling(window=window).mean()
    std = data['Close'].rolling(window=window).std()
    data['UpperBand'] = sma + (2 * std)
    data['LowerBand'] = sma - (2 * std)
    return data

# === Full Data Prep Pipeline ===
def gather_and_enrich(symbol="AAPL"):
    df = get_price_data(symbol)
    if df.empty:
        print(f"[DataGatherer] ⚠️ No data returned for {symbol}")
        return None
    df = calc_rsi(df)
    df = calc_macd(df)
    df = calc_bollinger(df)
    return df

# === Example Usage ===
if __name__ == "__main__":
    enriched_data = gather_and_enrich("AAPL")
    if enriched_data is not None:
        print(enriched_data.tail(5))

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():