from ghost_env import INFURA_KEY, VAULT_ADDRESS
Analyzing market trends for potential profitable trades involves a number of factors such as data collection, processing, and implementing trading strategies. For the purpose of this task, let's use Python `pandas` library for data manipulation and `yfinance` to download the stock data from Yahoo finance. 

Please note that actual trading based on this simple script can be risky, for real trading you will need to implement many additional features such as handling transaction costs, managing position sizes, and many more.

```python
import pandas as pd
import yfinance as yf
import datetime as dt
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Input stock symbol 
stock = 'AAPL'

# Download historical data as dataframe
data = yf.download(stock, start='2020-01-01', end=dt.datetime.now())

# Calculate moving averages
short_sma= 20
long_sma = 50
SMAs=[short_sma, long_sma]

for i in SMAs:
    data["SMA_"+str(i)]= data.iloc[:,4].rolling(window=i).mean()

# Define a function to signal when to buy and sell an asset
def buy_sell(signal):
  Buy = []
  Sell = []
  flag = -1

  for i in range(len(signal)):
    if signal['SMA_20'][i] > signal['SMA_50'][i]:
      if flag != 1:
        Buy.append(signal['Close'][i])
        Sell.append(np.nan)
        flag = 1
      else:
        Buy.append(np.nan)
        Sell.append(np.nan)
    elif signal['SMA_20'][i] < signal['SMA_50'][i]:
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

# Create buy and sell signals
data['Buy_Signal_Price'], data['Sell_Signal_Price'] = buy_sell(data)

# Plot data
plt.figure(figsize=(12,5))
plt.plot(data['Close'], label=stock, alpha=0.35)
plt.plot(data['SMA_20'], label='SMA_20', alpha=0.35)
plt.plot(data['SMA_50'], label='SMA_50', alpha=0.35)
plt.scatter(data.index, data['Buy_Signal_Price'], color='green', label='Buy Signal', marker='^', alpha=1)
plt.scatter(data.index, data['Sell_Signal_Price'], color='red', label='Sell Signal', marker='v', alpha=1)
plt.title('Stock Buy And Sell Signals')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(loc='upper left')
plt.show()
```

In the above code, we define two different timescale simple moving averages (SMA) and the buy/sell signals are when these SMAs cross each other. 

Moving averages are used to smooth out noise in the data and to highlight the underlying trend. In general, this strategy would suggest to buy the asset when shorter timescale SMA crosses above longer timescale SMA and sell it when shorter timescale SMA crosses below the longer one.