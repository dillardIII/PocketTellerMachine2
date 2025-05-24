To develop and implement trading strategies, we can use Python's pandas library for data manipulation and analysis. We will also use yfinance to download the historical market data from Yahoo finance.

Here's a simple Python code for a moving average crossover strategy. This strategy is one of the most commonly used strategies in trading. It's based on two moving averages, one short (fast) and one long (slow). When the short moving average crosses above the long moving average, it's a signal to buy. When the short moving average crosses below the long moving average, it's a signal to sell.

```python
import pandas as pd
import yfinance as yf

def calculate_sma(data, window):
    return data.rolling(window=window).mean()

def calculate_ema(data, window):
    return data.ewm(span=window, adjust=False).mean()

def implement_strategy(data):
    # Calculate the short and long window simple moving averages
    short_sma = calculate_sma(data['Close'], window=20)
    long_sma = calculate_sma(data['Close'], window=50)
    short_ema = calculate_ema(data['Close'], window=12)
    long_ema = calculate_ema(data['Close'], window=26)

    # Create signals based on the crossover of short and long moving average
    data['Buy_Signal'] = ((short_sma > long_sma) & (short_sma.shift() < long_sma.shift()))
    data['Sell_Signal'] = ((short_sma < long_sma) & (short_sma.shift() > long_sma.shift()))

    return data

# Download historical data as dataframe
data = yf.download('AAPL', start='2020-01-01', end='2022-12-31')

# Implement the strategy
trading_signals = implement_strategy(data)

# Print data
print(trading_signals)
```

This is a very basic trading strategy and may not be profitable in real trading. You should consider other factors such as trading fees, slippage, and market impact. Also, it's recommended to use more sophisticated methods for predicting future prices like machine learning algorithms.