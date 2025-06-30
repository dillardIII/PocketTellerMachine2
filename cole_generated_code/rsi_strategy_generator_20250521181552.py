from ghost_env import INFURA_KEY, VAULT_ADDRESS
The Relative Strength Index (RSI) is a momentum indicator used in technical analysis that measures the magnitude of recent price changes to evaluate overbought or oversold conditions in the price of a stock or other asset.

Below is a simple Python code to generate an RSI strategy:

```python
import pandas as pd
import yfinance as yf
from datetime import datetime
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Define the ticker symbol
tickerSymbol = 'AAPL'
tickerData = yf.Ticker(tickerSymbol)

# Get historical data
tickerDf = tickerData.history(period='1d', start='2010-1-1', end=datetime.today().strftime('%Y-%m-%d'))

# Calculate 14 day RSI
delta = tickerDf['Close'].diff()
delta = delta[1:]
gain = delta.copy()
loss = delta.copy()
gain[gain < 0] = 0
loss[loss > 0 = 0]
average_gain = gain.rolling(window=14).mean()
average_loss = abs(loss.rolling(window=14).mean())
rs = average_gain / average_loss
rsi = 100 - (100/(1+rs))

tickerDf['RSI'] = rsi

# Generate RSI Strategy
tickerDf['Buy_Signal_Flag'] = 0
tickerDf['Sell_Signal_Flag'] = 0
tickerDf.loc[(tickerDf['RSI'] < 30), 'Buy_Signal_Flag'] = 1
tickerDf.loc[(tickerDf['RSI'] > 70), 'Sell_Signal_Flag'] = 1

# Plot RSI Strategy
plt.figure(figsize=(14,7))
plt.plot(tickerDf.index, tickerDf['RSI'])
plt.axhline(0, linestyle='--', alpha=0.1)
plt.axhline(20, linestyle='--', alpha=0.5)
plt.axhline(30, linestyle='--')
plt.axhline(70, linestyle='--')
plt.axhline(80, linestyle='--', alpha=0.5)
plt.axhline(100, linestyle='--', alpha=0.1)
plt.fill_between(tickerDf.index, tickerDf['RSI'], 30, where=(tickerDf['RSI'] <= 30), color='blue', alpha=0.3)
plt.fill_between(tickerDf.index, tickerDf['RSI'], 70, where=(tickerDf['RSI'] >= 70), color='red', alpha=0.3)
plt.legend(['RSI via EWMA'])
plt.show()
```

This script will calculate the RSI for the past 14 days and plot the graph of RSI strategy for Apple Inc 'AAPL'. When the RSI is less than 30, it indicates a buying signal, and when the RSI is bigger than 70, it signals a selling signal.