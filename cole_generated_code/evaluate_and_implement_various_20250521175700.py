from ghost_env import INFURA_KEY, VAULT_ADDRESS
Completing this task perfectly requires a comprehensive understanding of trading strategies, data analytics, and financial programming. Here are some simple implementations of trading strategies in Python. These strategies, including Moving Averages crossover, and Relative Strength Index (RSI), can be used in momentum trading. 

Please note that this code is for educational purposes only! Real trading involves a lot of risks that this simple code can't take into account.

Let's make use of the yfinance and pandas libraries. Yfinance library is used to fetch historical market data. 

First, you need to install yfinance and pandas library with pip:

```python
pip install yfinance pandas
```

Here is a simple Python code that implements above mentioned trading strategies:

```python
import pandas as pd
import yfinance as yf
import numpy as np

# Moving Averages Crossover Strategy:
def calculate_SMA(data, window):
    return data.rolling(window=window).mean()

def calculate_EMA(data, window):
    return data.ewm(span=window, adjust=False).mean()

def moving_average_strategy(data, short_window, long_window):
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0
    signals['short_mavg'] = calculate_SMA(data, short_window)
    signals['long_mavg'] = calculate_SMA(data, long_window)
    signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] > signals['long_mavg'][short_window:], 1.0, 0.0)
    signals['orders'] = signals['signal'].diff()
    return signals

# RSI Strategy:
def calculate_RSI(data, window):
    delta = data.diff()
    delta = delta[1:]
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    average_gain = up.rolling(window=window).mean()
    average_loss = abs(down.rolling(window=window).mean())
    relative_strength = average_gain / average_loss
    RSI = 100.0 - (100.0 / (1.0 + relative_strength))
    return RSI

# Fetch data
ticker = 'AAPL'
data = yf.download(ticker, start='2020-01-01', end='2021-12-31', progress=False)
data = data['Close']

# Run strategies
short_window = 40
long_window = 100
signals = moving_average_strategy(data, short_window, long_window)

# Fetch signals
buy_signals = signals.loc[signals.orders== 1]
sell_signals = signals.loc[signals.orders== -1]

print(f"Buy signals:\n {buy_signals}")
print(f"Sell signals:\n {sell_signals}")

# Run RSI
RSI = calculate_RSI(data, 14)
overbought = RSI > 70
oversold = RSI < 30
print(f"RSI overbought:\n {RSI[overbought]}")
print(f"RSI oversold:\n {RSI[oversold]}")
```

This code will produce buy and sell signals for the Moving Averages crossover strategy, and it will also point out possible buy opportunities (RSI below 30) and possible sell opportunities (RSI above 70) for the RSI strategy. 

This is a very basic way to implement these strategies, and this doesn't take into account trading costs, short-selling restrictions, or any financial risk measures. In real trading, one should also consider these points. 

Also, you may want to use more sophisticated Machine Learning algorithms instead of these simple strategies. You might want to make use of the advanced packages such as Keras, TensorFlow, PyTorch for such purposes. 

Keep in mind that investing in the stock market always carries risk, and nothing guarantees that these strategies will be profitable. Make sure to test these strategies extensively on historical data (this is called backtesting) and/or paper trading before live trading with real money.
