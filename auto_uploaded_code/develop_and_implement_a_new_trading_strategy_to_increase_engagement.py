from ghost_env import INFURA_KEY, VAULT_ADDRESS
To develop and implement a new trading strategy, we can use Python's pandas library for data manipulation and analysis. We'll also use yfinance to download historical market data from Yahoo finance. The trading strategy we'll implement is a simple moving average crossover strategy. This strategy is based on the idea that if the short term moving average crosses the long term moving average, it may be a signal of future price movement.

Here is a simple Python code to implement this strategy:

```python
import pandas as pd
import yfinance as yf

def calculate_sma(data, window):
    return data.rolling(window=window).mean()

def calculate_ema(data, window):
    return data.ewm(span=window, adjust=False).mean()

def trading_strategy(data, short_window, long_window):
    # Calculate the short and long window simple moving averages
    data['short_sma'] = calculate_sma(data['Close'], short_window)
    data['long_sma'] = calculate_sma(data['Close'], long_window)

    # Create a column 'Signal' such that if the short window SMA is greater than the long window SMA, 
    # then set Signal as 1 else 0
    data['Signal'] = 0.0  
    data['Signal'][short_window:] = np.where(data['short_sma'][short_window:] > data['long_sma'][short_window:], 1.0, 0.0)   

    # Generate trading orders using the 'Signal' column. If Signal value changes from 1 to 0, generate a sell order, 
    # and if it changes from 0 to 1, then generate a buy order
    data['Position'] = data['Signal'].diff()

    return data

# Download historical data as dataframe
data = yf.download('AAPL', start='2020-01-01', end='2022-12-31')

# Implement the trading strategy
trading_data = trading_strategy(data, 50, 200)

# Print the DataFrame
print(trading_data)
```

In this code, we first calculate the short and long window simple moving averages (SMA). Then, we create a 'Signal' column that indicates when to buy and sell. If the short window SMA is greater than the long window SMA, we set the 'Signal' as 1 (indicating a buy order), otherwise, we set it as 0 (indicating a sell order). Finally, we generate trading orders based on the 'Signal' column.

Please note that this is a simple trading strategy and may not necessarily lead to profits. It's important to consider other factors and strategies when trading in the stock market. Also, this code doesn't take into account transaction costs.