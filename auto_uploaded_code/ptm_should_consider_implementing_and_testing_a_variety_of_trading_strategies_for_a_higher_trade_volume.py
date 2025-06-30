from ghost_env import INFURA_KEY, VAULT_ADDRESS
Your request is very broad and it's hard to know what specifically you want as trading strategies can vary a lot. But here's a basic example of backtesting the simple moving average crossover strategy using Python. This is just a simple strategy for demonstration and might not be effective in actual trading. We'll use the pandas and yfinance libraries to get historical price data and to manipulate it:

```python
import pandas as pd
import yfinance as yf

# Define the ticker symbol
tickerSymbol = 'AAPL'

# Collect data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2020-12-31')

# Calculate simple moving average with 20-day window
tickerDf['SMA20'] = tickerDf['Close'].rolling(window=20).mean()

# Calculate simple moving average with 50-day window
tickerDf['SMA50'] = tickerDf['Close'].rolling(window=50).mean()

# Create a new column 'Signal' such that if 20-day SMA is greater than 50-day SMA then set Signal as 1 else 0
tickerDf['Signal'] = 0.0  
tickerDf['Signal'][tickerDf['SMA20'] > tickerDf['SMA50']] = 1.0

# Create a new column 'Position' which is a day-to-day difference of the 'Signal' column
tickerDf['Position'] = tickerDf['Signal'].diff()

# Print the DataFrame
print(tickerDf)
```

Please modify the above code as needed. For instance, you might want to add a part where to sell/buy orders are executed depending on the signal. Note however that this code does not actually perform any trades, it just backtests the described strategy.

Remember that live trading using strategies like this requires careful consideration and measures to manage risk. It is highly recommended to consult with a knowledgeable individual or organization before proceeding with real trades.