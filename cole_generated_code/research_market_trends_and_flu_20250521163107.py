from ghost_env import INFURA_KEY, VAULT_ADDRESS
As an AI model, I design python codes, but I can't execute or run them. Data from stock markets or financial markets is typically required to investigate market trends and changes. Here's an example of how you'd do it using the 'yfinance' free library to download the stock data, 'pandas' for data manipulation, and 'matplotlib' for data visualization.

```python
# Import Necessary Libraries
import yfinance as yf 
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# Define the ticker symbol
tickerSymbol = 'AAPL'  # Change this to the symbol of the stock you want to research

# Get data for this ticker
tickerData = yf.Ticker(tickerSymbol)

# get the historical prices for this ticker
ticker_df = tickerData.history(period='1d', start='2010-1-1', end=datetime.date.today().isoformat())

# see your data
print(ticker_df)

# Calculate the moving average
ticker_df['MA50'] = ticker_df['Close'].rolling(window=50).mean()
ticker_df['MA200'] = ticker_df['Close'].rolling(window=200).mean()

# Create the graph
plt.figure(figsize=(12,6))
plt.plot(ticker_df['Close'])
plt.plot(ticker_df['MA50'], 'r') # color is red
plt.plot(ticker_df['MA200'], 'g') # color is green
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Market Trend of ' + tickerSymbol)
plt.legend(['Close', 'MA50', 'MA200'])
plt.show()
```

This script will draw a line chart of daily closing prices, a 50 days moving average (short-term trend), and a 200 days moving average (long-term trend) of the selected stock symbol.

Please note that actual market research should consist of a more in-depth analysis with more complex statistical measures and more comprehensive data source, possibly including news sentiment, economic indicators, and other companies' data.