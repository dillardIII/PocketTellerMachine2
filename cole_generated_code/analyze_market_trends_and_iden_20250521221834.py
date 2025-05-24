Analyzing market trends and identifying potential profitable trades involves complex algorithms and requires real-time data. Here is a simple example of how you can analyze historical data using Python with the help of pandas, yfinance and matplotlib libraries.

```python
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Download historical data for desired ticker symbol
ticker = 'AAPL'
tickerData = yf.Ticker(ticker)
tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2020-1-25')

# Calculate moving averages
tickerDf['MA10'] = tickerDf['Close'].rolling(10).mean()
tickerDf['MA50'] = tickerDf['Close'].rolling(50).mean()

# Create a function to signal when to buy and sell an asset
def buy_sell(signal):
    Buy = []
    Sell = []
    flag = -1

    for i in range(len(signal)):
        if signal['MA10'][i] > signal['MA50'][i]:
            if flag != 1:
                Buy.append(signal['Close'][i])
                Sell.append(np.nan)
                flag = 1
            else:
                Buy.append(np.nan)
                Sell.append(np.nan)
        elif signal['MA10'][i] < signal['MA50'][i]:
            if flag != 0:
                Sell.append(signal['Close'][i])
                Buy.append(np.nan)
                flag = 0
            else:
                Buy.append(np.nan)
                Sell.append(np.nan)
        else:
            Buy.append(np.nan)
            Sell.append(np.nan)

    return (Buy, Sell)

# Create buy and sell column
tickerDf['Buy_Signal_Price'] = buy_sell(tickerDf)[0]
tickerDf['Sell_Signal_Price'] = buy_sell(tickerDf)[1]

# Plot data
plt.figure(figsize=(12.2, 4.5))
plt.plot(tickerDf['Close'], label='Close Price', alpha=0.35)
plt.plot(tickerDf['MA10'], label='MA10', alpha=0.35)
plt.plot(tickerDf['MA50'], label='MA50', alpha=0.35)
plt.scatter(tickerDf.index, tickerDf['Buy_Signal_Price'], color='green', label='Buy Signal', marker='^', alpha=1)
plt.scatter(tickerDf.index, tickerDf['Sell_Signal_Price'], color='red', label='Sell Signal', marker='v', alpha=1)
plt.title('Stock Buy And Sell Signals')
plt.xlabel('Years')
plt.ylabel('Price USD ($)')
plt.legend(loc='upper left')
plt.show()
```

This script downloads the historical data for the specified ticker symbol, calculates the moving averages, and generates buy and sell signals based on the moving averages. It then plots the closing prices, moving averages, and buy/sell signals on a graph.

Please note that this is a very basic strategy and is not guaranteed to be profitable. It's always recommended to use more sophisticated algorithms and consider more factors for real trading.