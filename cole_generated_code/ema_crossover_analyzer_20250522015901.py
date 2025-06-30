from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple example of how you can implement an EMA Crossover Analyzer using Python with the help of pandas library for data manipulation and yfinance library for downloading historical stock price data.

Please note that this is a very basic example and may need to be adjusted based on your specific needs.

```python
import pandas as pd
import yfinance as yf

def calculate_ema(data, window):
    return data.ewm(span=window, adjust=False).mean()

def ema_crossover_analyzer(symbol, short_window, long_window):
    # Download historical data as dataframe
    data = yf.download(symbol, start='2020-01-01', end='2022-12-31')

    # Calculate short and long EMA
    data['short_ema'] = calculate_ema(data['Close'], short_window)
    data['long_ema'] = calculate_ema(data['Close'], long_window)

    # Create signals
    data['signal'] = 0.0
    data['signal'][short_window:] = np.where(data['short_ema'][short_window:] > data['long_ema'][short_window:], 1.0, 0.0)

    # Generate trading orders
    data['positions'] = data['signal'].diff()

    # Print data
    print(data)

# Run the EMA Crossover Analyzer
ema_crossover_analyzer('AAPL', 12, 26)
```

In this code:

- We first download the historical data for a given symbol (stock ticker) using yfinance.
- We then calculate the short and long EMA (Exponential Moving Average) using pandas' ewm function.
- We create a 'signal' column in our dataframe where we mark 1.0 if the short EMA is greater than the long EMA, and 0.0 otherwise.
- We then calculate the 'positions' which is simply the difference in the 'signal' from the previous day. This will give us our trading orders (1 for buy, -1 for sell).
- Finally, we print the data.

Please make sure you have the necessary libraries installed in your Python environment. You can install them using pip:

```bash
pip install pandas yfinance
```