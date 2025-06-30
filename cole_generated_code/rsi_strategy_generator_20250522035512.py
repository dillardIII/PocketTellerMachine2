from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here's a simple implementation of an RSI (Relative Strength Index) strategy generator in Python using the `pandas` and `yfinance` libraries. This code will generate a trading strategy based on the RSI indicator for a given stock.

```python
import pandas as pd
import yfinance as yf
from pandas_datareader import data as pdr

# Download historical data for desired ticker symbol
def download_data(stock, start, end):
    data = {}
    ticker = yf.download(stock, start, end)
    data['Price'] = ticker['Adj Close']
    return pd.DataFrame(data)

# Calculate the RSI
def calculate_RSI(data, window_length=14):
    delta = data['Price'].diff()
    delta = delta[1:] 

    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0

    roll_up = up.rolling(window_length).mean()
    roll_down = down.abs().rolling(window_length).mean()

    RS = roll_up / roll_down
    RSI = 100.0 - (100.0 / (1.0 + RS))

    data['RSI'] = RSI

    return data

# Generate the trading strategy
def generate_strategy(data):
    buy_price = []
    sell_price = []
    RSI_signal = []
    signal = 0

    for i in range(len(data)):
        if data['RSI'][i] < 30:   # if RSI < 30, it's a buy signal
            if signal != 1:
                buy_price.append(data['Price'][i])
                sell_price.append(np.nan)
                signal = 1
                RSI_signal.append(signal)
            else:
                buy_price.append(np.nan)
                sell_price.append(np.nan)
                RSI_signal.append(0)
        elif data['RSI'][i] > 70:   # if RSI > 70, it's a sell signal
            if signal != -1:
                sell_price.append(data['Price'][i])
                buy_price.append(np.nan)
                signal = -1
                RSI_signal.append(signal)
            else:
                buy_price.append(np.nan)
                sell_price.append(np.nan)
                RSI_signal.append(0)
        else:
                buy_price.append(np.nan)
                sell_price.append(np.nan)
                RSI_signal.append(0)
                
    return buy_price, sell_price, RSI_signal

# Example usage:
data = download_data('AAPL', '2020-01-01', '2022-01-01')
data = calculate_RSI(data)
buy_price, sell_price, RSI_signal = generate_strategy(data)
```

This code will download the historical data for the specified stock (in this case, Apple), calculate the RSI, and then generate a trading strategy based on the RSI. The strategy is to buy when the RSI is below 30 (indicating the stock is oversold) and sell when the RSI is above 70 (indicating the stock is overbought).