from ghost_env import INFURA_KEY, VAULT_ADDRESS
The Relative Strength Index (RSI) is a popular technical analysis tool in trading which is primarily used for generating potential buy and sell signals.

Below is a Python implementation of a basic RSI Strategy generator using pandas and yfinance to get historical price data.

Please Note: This is a simple strategy, and real-world trading would require a lot more consideration and features.

```python
import pandas as pd
import yfinance as yf
import numpy as np

def calculate_RSI(data, period):
    delta = data.diff()
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    
    average_gain = up.rolling(window=period).mean()
    average_loss = abs(down.rolling(window=period).mean())
    
    rs = average_gain / average_loss
    rsi = 100 - (100/(1+rs))
    
    return rsi


def RSI_Strategy(ticker, start_date, end_date, rsi_period, rsi_upper=70, rsi_lower=30):
    data = yf.download(ticker, start=start_date, end=end_date)
    data['RSI'] = calculate_RSI(data['Adj Close'], rsi_period)
    
    buy_signals = (data['RSI'] < rsi_lower)
    sell_signals = (data['RSI'] > rsi_upper)

    data['Buy_Signal_Price'] = np.where(buy_signals, data['Adj Close'], np.nan)
    data['Sell_Signal_Price'] = np.where(sell_signals, data['Adj Close'], np.nan)

    return data


# Example usage:
df = RSI_Strategy('AAPL', '2020-01-01', '2020-12-31', 14)
df.plot(y=['Adj Close', 'Buy_Signal_Price', 'Sell_Signal_Price'], title='RSI Strategy buy and sell signals')
```
In the code above, we first calculate the Relative Strength Index (RSI) for each day, and save it in the RSI column. Then we indicate the trading signals: a buy signal is marked when the RSI value is below the specified lower threshold (traditionally 30), and a sell signal is marked by an RSI value above the upper threshold (traditionally 70). The results are then plotted for visual analysis.