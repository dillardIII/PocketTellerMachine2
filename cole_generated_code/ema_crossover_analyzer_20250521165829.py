from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, in order to implement this, we're going to use the `pandas` library for data manipulation and the `yfinance` library to fetch historical stock price data from Yahoo Finance. We'll write a program to calculate the Exponential Moving Average (EMA) for two different periods and then find the points at which these averages cross over.

Please install the libraries if they aren't installed yet, you can do it using pip:

```sh
pip install pandas yfinance
```
Once you've installed the necessary libraries, you can use the Python code below:

```python
import pandas as pd
import yfinance as yf

def calculate_ema(data, window):
    return data.ewm(span=window, adjust=False).mean()

def ema_crossover_analyzer(ticker_symbol, short_window, long_window):
    # Fetch the data
    data = yf.download(ticker_symbol, start='2020-01-01', end='2022-12-31')

    # Print the data
    print("The original data: ")
    print(data)

    # Calculate short and long EMA
    data['Short_EMA'] = calculate_ema(data['Close'], short_window)
    data['Long_EMA'] = calculate_ema(data['Close'], long_window)

    # Create signals
    data['Buy_Signal'] = (data['Short_EMA'] > data['Long_EMA'])
    data['Sell_Signal'] = (data['Short_EMA'] < data['Long_EMA'])

    # Print the data with signals
    print("Data with EMA and trading signals: ")
    print(data)
    
    return data

# Run the function
ema_crossover_analyzer('AAPL', 20, 100)
```

This code performs the following actions:
1. It fetches historical price data for a given ticker symbol (replace 'AAPL' with the symbol of the stock for which you want to perform the analysis).
2. It calculates the short-term and long-term EMA for the given window periods.
3. It then generates trading signals. A Buy_Signal is indicated when the short EMA crosses above the long EMA and a Sell_Signal is indicated when the short EMA crosses below the long EMA.
4. The function then returns the data with the calculated EMAs and trading signals.