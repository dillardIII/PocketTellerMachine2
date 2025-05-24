Analyzing market trends and patterns to identify potential trading opportunities involves complex data analysis and machine learning algorithms. Here's a simple Python code using pandas and yfinance to download historical data, calculate simple moving averages and identify potential trading opportunities based on crossover strategy.

Please note that this is a very basic strategy and real-world trading involves more complex strategies and risk management.

```python
import pandas as pd
import yfinance as yf

# Download historical data for desired ticker symbol
def download_data(stock, start, end):
    data = yf.download(stock, start, end)
    return data

# Calculate Simple Moving Average (SMA)
def calculate_SMA(data, window):
    sma = data['Close'].rolling(window=window).mean()
    return sma

# Identify potential trading opportunities based on SMA crossover
def identify_trades(data, short_sma, long_sma):
    # Create a column 'Signal' such that if short-term SMA is greater than long-term SMA then buy else sell
    data['Signal'] = 0.0  
    data['Signal'][short_sma > long_sma] = 1.0   
    data['Signal'][short_sma < long_sma] = -1.0   

    # Create a column 'Position' which is the difference of two consecutive signals. This column will give actual trading actions
    data['Position'] = data['Signal'].diff()

    return data

# Define the ticker symbol and the start and end dates
ticker = 'AAPL'
start_date = '2020-01-01'
end_date = '2021-12-31'

# Download the data
data = download_data(ticker, start_date, end_date)

# Calculate short-term and long-term SMAs
short_sma = calculate_SMA(data, window=20)
long_sma = calculate_SMA(data, window=50)

# Identify potential trades
trades = identify_trades(data, short_sma, long_sma)

# Print the dataframe
print(trades)
```

This code will print a dataframe where 'Position' column will tell you when to buy (Position = 1) and when to sell (Position = -1). Please note that this is a very simplistic trading strategy and should not be used for actual trading without proper risk management and strategy validation.