from ghost_env import INFURA_KEY, VAULT_ADDRESS
To develop and test new trading strategies, we need to use historical data for backtesting. Here's a simple Python code using pandas and yfinance to download historical data and calculate simple moving averages as a trading strategy.

```python
import pandas as pd
import yfinance as yf

# Download historical data for desired ticker symbol
def download_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

# Calculate simple moving average
def calculate_sma(data, window):
    sma = data['Close'].rolling(window=window).mean()
    return sma

# Define a simple trading strategy
def trading_strategy(data, short_window, long_window):
    # Calculate short and long window sma
    short_sma = calculate_sma(data, short_window)
    long_sma = calculate_sma(data, long_window)

    # Create signals
    data['signal'] = 0.0
    data['signal'][short_window:] = np.where(short_sma[short_window:] > long_sma[short_window:], 1.0, 0.0)

    # Generate trading orders
    data['positions'] = data['signal'].diff()

# Test the trading strategy
def test_strategy(ticker, start_date, end_date, short_window, long_window):
    data = download_data(ticker, start_date, end_date)
    trading_strategy(data, short_window, long_window)
    return data

# Example usage
test_strategy('AAPL', '2020-01-01', '2021-12-31', 50, 200)
```

This is a simple moving average crossover strategy where we buy when the short-term average crosses above the long-term average and sell when it crosses below. 

Please note that this is a very basic strategy and in real-life scenarios, trading strategies can get very complex involving multiple indicators and parameters. Also, it's important to remember that past performance is not indicative of future results. 

You should also consider transaction costs, slippage, etc. when designing a trading strategy. Always validate the performance of the strategy using out-of-sample data.