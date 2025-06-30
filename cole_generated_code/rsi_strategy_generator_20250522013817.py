from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple implementation of a Relative Strength Index (RSI) strategy generator in Python using the pandas library for data manipulation and the yfinance library to get the stock data:

```python
import pandas as pd
import yfinance as yf

def calculate_rsi(data, window):
    delta = data.diff()
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0

    average_gain = up.rolling(window=window).mean()
    average_loss = abs(down.rolling(window=window).mean())

    rs = average_gain / average_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def rsi_strategy(ticker, start_date, end_date, rsi_window, upper_threshold, lower_threshold):
    data = yf.download(ticker, start=start_date, end=end_date)
    data['RSI'] = calculate_rsi(data['Close'], rsi_window)
    data['Buy_Signal'] = (data['RSI'] < lower_threshold)
    data['Sell_Signal'] = (data['RSI'] > upper_threshold)
    return data[['Close', 'RSI', 'Buy_Signal', 'Sell_Signal']]

# Example usage:
df = rsi_strategy('AAPL', '2020-01-01', '2021-12-31', 14, 70, 30)
print(df)
```

In this code, the `calculate_rsi` function calculates the RSI for the given data and window size. The `rsi_strategy` function downloads the stock data for the given ticker and date range, calculates the RSI, and then generates buy signals when the RSI is below the lower threshold and sell signals when the RSI is above the upper threshold.

Please note that this is a very basic implementation of an RSI strategy and may not be suitable for actual trading. It does not take into account transaction costs, slippage, or risk management. Also, the choice of RSI window size and thresholds can greatly affect the performance of the strategy.