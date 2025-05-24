To analyze market trends and patterns, we need to have access to historical market data. This data can be obtained from various sources like Yahoo Finance, Google Finance, etc. Here is a simple Python code using Pandas and yfinance library to download historical market data and analyze it.

Please note that this is a very basic example. In real-world scenarios, you would need to use more sophisticated statistical and machine learning techniques to analyze market trends and patterns.

```python
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Download historical data for desired ticker symbol
ticker = "AAPL"
tickerData = yf.Ticker(ticker)
df = tickerData.history(period='1d', start='2010-1-1', end='2020-12-31')

# Plot the closing price
df['Close'].plot(title="Closing price of "+ticker)
plt.show()

# Decompose the time series data to observe trends and seasonality
result = seasonal_decompose(df['Close'], model='multiplicative', freq = 30)
result.plot()
plt.show()

# Identify potential trading opportunities by finding significant increases/decreases in closing price
df['PriceDiff'] = df['Close'].shift(-1) - df['Close']

# Create a column 'Profit' assuming we buy a stock today and sell it the next day
df['Profit'] = df['PriceDiff'].shift(1)

# Create a column 'Return' using profit and closing price of the stock for the day
df['Return'] = df['Profit']/df['Close']

# Print the total profit made from the stock assuming we buy on day 1 and sell on day 2
total_profit = df['Profit'].sum()
print("Total profit from "+ticker+" : ", total_profit)
```

This code will download the historical data for the given ticker symbol, plot the closing price, decompose the time series to observe trends and seasonality, and calculate the potential profit if we buy the stock on one day and sell it on the next day.