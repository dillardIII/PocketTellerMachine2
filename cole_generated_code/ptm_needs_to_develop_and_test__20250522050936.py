from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I will provide a simple Python code for a basic trading strategy. This strategy is called Moving Average Crossover, which is used to identify changes in the trend of a stock price.

Please note that this is a very basic strategy and may not be profitable without further modifications and optimizations. The code uses the `pandas` library for data manipulation and `yfinance` to download the stock price data.

```python
import pandas as pd
import yfinance as yf

def calculate_sma(data, window):
    return data.rolling(window=window).mean()

def calculate_ema(data, window):
    return data.ewm(span=window, adjust=False).mean()

def trading_strategy(data, short_window, long_window):
    # Calculate the short and long window simple moving averages
    data['short_sma'] = calculate_sma(data['Adj Close'], short_window)
    data['long_sma'] = calculate_sma(data['Adj Close'], long_window)

    # Create a column 'Signal' such that if the short window SMA is greater than long window SMA then buy else sell
    data['Signal'] = 0.0  
    data['Signal'][short_window:] = np.where(data['short_sma'][short_window:] > data['long_sma'][short_window:], 1.0, 0.0)   

    # Create a column 'Position' which is the difference of the 'Signal' column. This column indicates the actual position of the trading strategy
    data['Position'] = data['Signal'].diff()
    
    return data

# Define the ticker symbol
tickerSymbol = 'AAPL'

# Get the data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2020-12-31')

# Use the trading strategy
trading_data = trading_strategy(tickerDf, 50, 200)

# Print the data
print(trading_data)
```

This script downloads the historical price data for the Apple Inc. stock and applies the Moving Average Crossover strategy with a short window of 50 days and a long window of 200 days. The 'Position' column in the resulting DataFrame indicates whether to buy (1) or sell (-1) the stock at a given date.

Please replace 'AAPL' with the ticker symbol of the stock you want to test the trading strategy on. Also, you can adjust the short and long window lengths according to your needs.