from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple implementation of an EMA Crossover Analyzer using Python and the pandas library. This script will calculate the EMA for two different periods and then determine when the EMAs cross over each other.

```python
import pandas as pd
import pandas_datareader as pdr
import datetime

# Define the stock symbol and the start and end dates for the data
symbol = 'AAPL'
start_date = datetime.datetime(2020, 1, 1)
end_date = datetime.datetime(2021, 12, 31)

# Download the data from Yahoo Finance
df = pdr.get_data_yahoo(symbol, start=start_date, end=end_date)

# Calculate the short and long EMA
short_ema = df['Close'].ewm(span=12, adjust=False).mean()
long_ema = df['Close'].ewm(span=26, adjust=False).mean()

# Create a new DataFrame to store the data
data = pd.DataFrame()
data['Close'] = df['Close']
data['Short EMA'] = short_ema
data['Long EMA'] = long_ema

# Create a function to signal when to buy and sell the asset/stock
def ema_crossover(data):
    buy_signal = []
    sell_signal = []
    flag = -1

    for i in range(len(data)):
        if data['Short EMA'][i] > data['Long EMA'][i]:
            if flag != 1:
                buy_signal.append(data['Close'][i])
                sell_signal.append(np.nan)
                flag = 1
            else:
                buy_signal.append(np.nan)
                sell_signal.append(np.nan)
        elif data['Short EMA'][i] < data['Long EMA'][i]:
            if flag != 0:
                sell_signal.append(data['Close'][i])
                buy_signal.append(np.nan)
                flag = 0
            else:
                buy_signal.append(np.nan)
                sell_signal.append(np.nan)
        else:
            buy_signal.append(np.nan)
            sell_signal.append(np.nan)

    return (buy_signal, sell_signal)

# Add the buy and sell signals to the data DataFrame
data['Buy Signal'], data['Sell Signal'] = ema_crossover(data)

# Print the data DataFrame
print(data)
```

This script will print a DataFrame with the closing prices, the short and long EMA, and the buy and sell signals. Please replace 'AAPL' with the symbol of the stock you want to analyze, and adjust the start and end dates as needed. Also, you can adjust the span parameters in the ewm() function calls to change the periods for the EMAs.