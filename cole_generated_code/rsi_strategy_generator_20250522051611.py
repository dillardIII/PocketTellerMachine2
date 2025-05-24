The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It is used to identify overbought or oversold conditions in a market.

Here is a simple Python code using the `pandas` and `yfinance` libraries to generate an RSI strategy.

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

def rsi_strategy(data, window=14):
    rsi = calculate_rsi(data['Close'], window)
    data['RSI'] = rsi

    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0

    # Generate trading signals (1: Buy, -1: Sell)
    signals['signal'][window:] = np.where(rsi[window:] < 30, 1.0, 0.0) # Buy signal
    signals['signal'][window:] = np.where(rsi[window:] > 70, -1.0, signals['signal']) # Sell signal

    # Generate trading orders
    signals['positions'] = signals['signal'].diff()
    return signals

# Download historical data
data = yf.download('AAPL', start='2020-01-01', end='2022-01-01')

# Generate RSI strategy signals
signals = rsi_strategy(data)

print(signals)
```

In this code, we first calculate the RSI of the closing prices with a specified window (default is 14 days as commonly used). Then we generate trading signals based on the RSI: if RSI < 30, it's a buy signal (we assume the stock is oversold), and if RSI > 70, it's a sell signal (we assume the stock is overbought). The trading orders are the changes of the trading signals.

Please note that this is a very basic RSI strategy. In practice, you may need to adjust the parameters and add more conditions based on your trading goals and risk tolerance.