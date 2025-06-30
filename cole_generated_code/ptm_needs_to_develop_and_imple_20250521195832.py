from ghost_env import INFURA_KEY, VAULT_ADDRESS
Developing a trading strategy involves a lot of factors and it's a complex task. However, I can provide a simple example of a trading strategy using Python. This strategy will be based on a simple moving average (SMA) crossover, which is a common trading strategy. 

In this strategy, we will use two moving averages: a fast one (e.g., 50 days) and a slow one (e.g., 200 days). When the fast moving average crosses above the slow moving average, it's a signal to buy. When the fast moving average crosses below the slow moving average, it's a signal to sell.

Here is a simple implementation using Python and pandas:

```python
import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt

# Define the ticker symbol
tickerSymbol = 'AAPL'

# Get data on this ticker
df = web.DataReader(tickerSymbol, 'yahoo', start='2010-1-1', end='2020-12-31')

# Calculate the moving averages
df['SMA_50'] = df['Close'].rolling(window=50).mean()
df['SMA_200'] = df['Close'].rolling(window=200).mean()

# Create a function to signal when to buy and sell an asset
def buy_sell(signal):
    Buy = []
    Sell = []
    flag = -1

    for i in range(0, len(signal)):
        if signal['SMA_50'][i] > signal['SMA_200'][i]:
            if flag != 1:
                Buy.append(signal['Close'][i])
                Sell.append(np.nan)
                flag = 1
            else:
                Buy.append(np.nan)
                Sell.append(np.nan)
        elif signal['SMA_50'][i] < signal['SMA_200'][i]:
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
df['Buy_Signal_Price'] = buy_sell(df)[0]
df['Sell_Signal_Price'] = buy_sell(df)[1]

# Plot the data
plt.figure(figsize=(12.5, 4.5))
plt.plot(df['Close'], label='Close Price', alpha=0.35)
plt.plot(df['SMA_50'], label='SMA_50', alpha=0.35)
plt.plot(df['SMA_200'], label='SMA_200', alpha=0.35)
plt.scatter(df.index, df['Buy_Signal_Price'], color='green', label='Buy Signal', marker='^', alpha=1)
plt.scatter(df.index, df['Sell_Signal_Price'], color='red', label='Sell Signal', marker='v', alpha=1)
plt.title('Apple Close Price with Buy & Sell Signals')
plt.xlabel('2010-01-01 to 2020-12-31')
plt.ylabel('Close Price USD ($)')
plt.legend(loc='upper left')
plt.show()
```

Please note that this is a very simple trading strategy and it's not recommended to use it for real trading without further improvements and testing. Also, the stock market is highly unpredictable and involves a lot of risks. Always do your own research before making any trading decisions.