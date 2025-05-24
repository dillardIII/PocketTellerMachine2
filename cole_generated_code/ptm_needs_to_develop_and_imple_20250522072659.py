As an AI model, I can provide a basic example of a trading strategy using Python. However, please note that this is a simple example and real-world trading strategies can be quite complex and should be developed by professionals. 

Here's a simple moving average crossover strategy using the `pandas` library:

```python
import pandas as pd
import pandas_datareader as web

# Define the stock symbol and the time period
symbol = 'AAPL'
start_date = '2020-01-01'
end_date = '2021-12-31'

# Download the stock prices from Yahoo Finance
df = web.DataReader(symbol, 'yahoo', start_date, end_date)

# Calculate the short-term simple moving average
short_sma = df['Close'].rolling(window=20).mean()

# Calculate the long-term simple moving average
long_sma = df['Close'].rolling(window=100).mean()

# Create a column 'Signal' such that if the short-term SMA is greater than the long-term SMA then buy else sell
df['Signal'] = 0.0  
df['Signal'][short_sma > long_sma] = 1.0
df['Signal'][short_sma < long_sma] = -1.0

# Create a column 'Position' which is the difference of the 'Signal' column and its previous row
df['Position'] = df['Signal'].diff()

# Print the DataFrame
print(df)
```

In this script, we first download the historical prices of a stock (in this case, Apple Inc.). Then, we calculate the short-term and long-term simple moving averages (SMA). If the short-term SMA is greater than the long-term SMA, it means that the stock price is increasing, so we should buy the stock (Signal = 1). If the short-term SMA is less than the long-term SMA, it means that the stock price is decreasing, so we should sell the stock (Signal = -1). The 'Position' column indicates whether we should buy or sell the stock.

Please note that this is a very basic trading strategy and in real-world scenarios, trading strategies can be much more complex involving multiple indicators and complex algorithms. Also, this strategy does not take into account trading fees or other factors that could impact the profitability of the strategy. Always consult with a financial advisor or a professional before making trading decisions.