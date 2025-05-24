Sure, I can help you write a simple Python code to simulate a trade. However, please note that this is a very simplified version and real trading involves more factors and complexities. 

We will use `yfinance` library to download stock data, and then simulate a simple trading strategy: Buy when the price goes above the moving average and sell when it goes below.

First, you need to install the necessary library by running: `pip install yfinance pandas`

Here's the Python code:

```python
import yfinance as yf
import pandas as pd

def calculate_sma(data, window):
    return data.rolling(window=window).mean()

def trading_strategy(data, short_window, long_window):
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0

    # Short moving average
    signals['short_mavg'] = calculate_sma(data, short_window)
    # Long moving average
    signals['long_mavg'] = calculate_sma(data, long_window)

    # Create signals
    signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] 
                                                > signals['long_mavg'][short_window:], 1.0, 0.0)   

    # Generate trading orders
    signals['positions'] = signals['signal'].diff()

    return signals

def main():
    # Download historical data as dataframe
    data = yf.download('AAPL','2020-01-01','2021-12-31')

    # Use close price for this example
    close = data['Close']

    # Define the short/long windows
    short_window = 40
    long_window = 100

    # Initialize the signals dataframe
    signals = trading_strategy(close, short_window, long_window)

    # Print the dataframe
    print(signals)

main()
```

This code will print a dataframe where a 1 in the 'positions' column means a 'Buy' signal and a -1 means a 'Sell' signal. Please note that this is a very simple strategy and is not recommended for actual trading. For real trading, you would need to consider transaction costs, risk management, and more sophisticated strategies.