from ghost_env import INFURA_KEY, VAULT_ADDRESS
To engage in active trading, we need to create a trading strategy. Here's a simple example of a Python code using a moving average crossover strategy. This strategy is one of the most commonly used strategies in trading. It involves two moving averages, one short and one long. When the short moving average crosses above the long moving average, it's a signal to buy. When it crosses below, it's a signal to sell.

This code uses the `yfinance` package to download stock price data, and `pandas` to calculate moving averages and generate trading signals. 

Please note that this is a very simplified example and real trading involves many more factors.

```python
import yfinance as yf
import pandas as pd

# Download historical data for desired ticker symbol
def download_data(stock, start_date, end_date):
    data = yf.download(stock, start_date, end_date)
    return data

# Calculate short-term and long-term moving averages
def calculate_moving_averages(data, short_window, long_window):
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0

    # Short moving average
    signals['short_mavg'] = data['Close'].rolling(window=short_window, min_periods=1, center=False).mean()

    # Long moving average
    signals['long_mavg'] = data['Close'].rolling(window=long_window, min_periods=1, center=False).mean()

    # Create signals
    signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] 
                                                > signals['long_mavg'][short_window:], 1.0, 0.0)   
    signals['positions'] = signals['signal'].diff()

    return signals

# Execute the trading strategy
def execute_trading_strategy(stock, start_date, end_date, short_window, long_window):
    data = download_data(stock, start_date, end_date)
    signals = calculate_moving_averages(data, short_window, long_window)

    # Print the DataFrame
    print(signals)

# Define the parameters
stock = 'AAPL'
start_date = '2020-01-01'
end_date = '2021-12-31'
short_window = 40
long_window = 100

execute_trading_strategy(stock, start_date, end_date, short_window, long_window)
```

This code will print a DataFrame where a 1 in the 'positions' column indicates a buy signal and a -1 indicates a sell signal. The 'signal' column will be 1 when the system is in the 'long' position (i.e., after a buy signal and before a sell signal) and 0 otherwise.

Please note that this code is for illustrative purposes only and should not be used for real trading without proper risk management.