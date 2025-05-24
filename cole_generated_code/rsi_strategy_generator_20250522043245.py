Here is a simple implementation of a Relative Strength Index (RSI) strategy generator in Python using the pandas and yfinance libraries. This code fetches historical price data, calculates the RSI, and generates a trading strategy based on the RSI.

```python
import pandas as pd
import yfinance as yf
from pandas_datareader import data as pdr

yf.pdr_override()

# Fetch historical data
def fetch_data(stock, start, end):
    df = pdr.get_data_yahoo(stock, start, end)
    return df

# Calculate RSI
def calculate_rsi(data, window):
    delta = data['Adj Close'].diff()
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    avg_gain = up.rolling(window).mean()
    avg_loss = abs(down.rolling(window).mean())
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

# Generate RSI strategy
def generate_rsi_strategy(data, rsi, buy_threshold, sell_threshold):
    data['Buy_Signal'] = (rsi < buy_threshold)
    data['Sell_Signal'] = (rsi > sell_threshold)
    return data

# Main function
def main():
    stock = 'AAPL'
    start = '2020-01-01'
    end = '2022-12-31'
    window = 14
    buy_threshold = 30
    sell_threshold = 70

    data = fetch_data(stock, start, end)
    rsi = calculate_rsi(data, window)
    strategy = generate_rsi_strategy(data, rsi, buy_threshold, sell_threshold)

    print(strategy)

if __name__ == "__main__":
    main()
```

This script fetches historical price data for a given stock (in this case, 'AAPL') from Yahoo Finance, calculates the RSI with a specified window (14 days in this case), and generates a trading strategy based on the RSI. The strategy is to buy when the RSI is below a certain threshold (30 in this case) and sell when the RSI is above a certain threshold (70 in this case). The resulting DataFrame includes columns for the buy and sell signals.