from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple Python code that uses the pandas library to calculate the Exponential Moving Average (EMA) and analyze the EMA crossover.

```python
import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt

# Fetch the data
df = web.DataReader('AAPL', data_source='yahoo', start='2012-01-01', end='2021-12-31')

# Calculate the Short/Fast EMA
ShortEMA = df.Close.ewm(span=12, adjust=False).mean() # 12 period span

# Calculate the Long/Slow EMA
LongEMA = df.Close.ewm(span=26, adjust=False).mean() # 26 period span

# Visualize the closing price and both EMAs
plt.figure(figsize=(12,5))
plt.title('Close Price and EMA Crossover', fontsize=18)
plt.plot(df['Close'], label='Close Price', color='blue')
plt.plot(ShortEMA, label='Short/Fast EMA', color='red')
plt.plot(LongEMA, label='Long/Slow EMA', color='green')
plt.xlabel('Date', fontsize=18)
plt.ylabel('Close Price USD ($)', fontsize=18)
plt.legend(loc='upper left')
plt.show()

# Create a function to signal when to buy and sell an asset
def EMA_Crossover(data):
    buy_list = []
    sell_list = []
    flag_long = False
    flag_short = False

    for i in range(0,len(data)):
        if ShortEMA[i] > LongEMA[i]:
            if flag_long == False:
                buy_list.append(data[i])
                sell_list.append(np.nan)
                flag_short = False
                flag_long = True
            else:
                buy_list.append(np.nan)
                sell_list.append(np.nan)
        elif ShortEMA[i] < LongEMA[i]:
            if flag_short == False:
                sell_list.append(data[i])
                buy_list.append(np.nan)
                flag_short = True
                flag_long = False
            else:
                buy_list.append(np.nan)
                sell_list.append(np.nan)
        else:
            buy_list.append(np.nan)
            sell_list.append(np.nan)
            
    return (buy_list, sell_list)

# Add the buy and sell signals to the data frame
df['Buy_Signal_Price'] = EMA_Crossover(df['Close'])[0]
df['Sell_Signal_Price'] = EMA_Crossover(df['Close'])[1]

# Visualize the stock buy and sell signals
plt.figure(figsize=(12,5))
plt.title('Buy and Sell Plot', fontsize=18)
plt.plot(df['Close'], label='Close Price', color='blue', alpha=0.35)
plt.plot(ShortEMA, label='Short/Fast EMA', color='red', alpha=0.35)
plt.plot(LongEMA, label='Long/Slow EMA', color='green', alpha=0.35)
plt.scatter(df.index, df['Buy_Signal_Price'], color='green', marker='^', alpha=1)
plt.scatter(df.index, df['Sell_Signal_Price'], color='red', marker='v', alpha=1)
plt.xlabel('Date', fontsize=18)
plt.ylabel('Close Price USD ($)', fontsize=18)
plt.legend(loc='upper left')
plt.show()
```

Please note that this code uses Yahoo Finance to fetch the data for Apple Inc. (AAPL) and calculates the EMA crossover for the same. You can replace 'AAPL' with the ticker symbol of your choice. Also, this is a simple EMA crossover strategy and might not work well in all market conditions. Always use trading strategies with caution and discretion.