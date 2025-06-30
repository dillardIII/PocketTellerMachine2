from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple Python code for EMA Crossover Analyzer using pandas library. This code will analyze the EMA crossover for a given stock data.

```python
import pandas as pd
import pandas_datareader as pdr
import datetime

# Function to calculate EMA
def calculate_EMA(data, window):
    return data.ewm(span=window, adjust=False).mean()

# Function to analyze EMA crossover
def analyze_EMA_crossover(stock, short_window, long_window):
    # Download historical data as dataframe
    start_date = datetime.datetime.now() - datetime.timedelta(days=365)
    end_date = datetime.date.today()
    data = pdr.get_data_yahoo(stock, start=start_date, end=end_date)

    # Calculate short and long EMA
    short_EMA = calculate_EMA(data['Close'], short_window)
    long_EMA = calculate_EMA(data['Close'], long_window)

    # Create signals
    data['short_EMA'] = short_EMA
    data['long_EMA'] = long_EMA
    data['signal'] = 0.0
    data['signal'][short_window:] = np.where(data['short_EMA'][short_window:] > data['long_EMA'][short_window:], 1.0, 0.0)

    # Generate trading orders
    data['positions'] = data['signal'].diff()

    # Print data
    print(data)

# Test the function
analyze_EMA_crossover('AAPL', 12, 26)
```

This script will download the historical data for the given stock (AAPL in this case) and calculate the short and long EMA. It will then generate trading signals based on the crossover of these two EMAs. If the short EMA is greater than the long EMA, it will generate a buy signal (1.0), otherwise it will generate a sell signal (0.0). It will then generate trading orders based on these signals.

Please note that you need to install pandas_datareader library to download the stock data. You can install it using pip:

```bash
pip install pandas_datareader
```

Also, this is a very basic EMA crossover strategy. In a real trading system, you would need to consider many other factors like trading fees, slippage, risk management, etc.