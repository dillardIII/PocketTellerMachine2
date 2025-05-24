Sure, I can provide you with a simple example of a trading strategy using Python. In this example, we will use a simple moving average crossover strategy. This strategy is a basic one where we buy when the short-term average crosses above the long-term average and sell when the short-term average crosses below the long-term average.

Please note that this is a very simplified example and real trading strategies would require much more complex analysis and risk management.

```python
import pandas as pd
import numpy as np
import yfinance as yf

# Download historical data for desired ticker symbol
def download_data(stock, start, end):
    data = {}
    ticker = yf.download(stock, start, end)
    data['Price'] = ticker['Adj Close']
    return pd.DataFrame(data)

# Calculate short-term and long-term moving averages
def calculate_averages(data, short, long):
    data["ShortAverage"] = data['Price'].rolling(window=short).mean()
    data["LongAverage"] = data['Price'].rolling(window=long).mean()
    return data

# Implement the trading strategy
def implement_strategy(data):
    buy_signals = (data['ShortAverage'] > data['LongAverage']) & (data['ShortAverage'].shift(1) < data['LongAverage'].shift(1))
    sell_signals = (data['ShortAverage'] < data['LongAverage']) & (data['ShortAverage'].shift(1) > data['LongAverage'].shift(1))
    
    data.loc[buy_signals, 'Order'] = 'Buy'
    data.loc[sell_signals, 'Order'] = 'Sell'
    
    data['Position'] = data['Order'].eq('Buy').cumsum() - data['Order'].eq('Sell').cumsum()
    return data

# Define the ticker symbol and the start and end dates
stock = 'AAPL'
start_date = '2020-01-01'
end_date = '2021-12-31'

# Define the short-term and long-term windows for the moving averages
short_window = 50
long_window = 200

# Download the data, calculate the averages and implement the strategy
data = download_data(stock, start_date, end_date)
data = calculate_averages(data, short_window, long_window)
data = implement_strategy(data)

print(data)
```

This script downloads historical price data for a specific stock, calculates short-term and long-term moving averages, and generates buy and sell signals based on these averages. The script then calculates the position, which indicates how many shares of the stock should be held at each point in time.