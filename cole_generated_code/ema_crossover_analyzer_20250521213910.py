from ghost_env import INFURA_KEY, VAULT_ADDRESS
To complete this task, we need to define what an EMA Crossover is. An EMA Crossover is a point on the trading chart where the short-term Exponential Moving Average (EMA) crosses the long-term EMA. It's a popular tool among traders as it may indicate a potential change in the trend, either upwards (bullish) or downwards (bearish).

Here is a simple Python code using pandas library to calculate EMA crossover:

```python
import pandas as pd
import yfinance as yf

# Download historical data for desired ticker symbol
def download_data(stock, start, end):
    data = {}
    ticker = yf.download(stock, start, end)
    data['Price'] = ticker['Adj Close']
    return pd.DataFrame(data)

# Calculate EMA
def calculate_ema(data, window):
    return data['Price'].ewm(span=window, adjust=False).mean()

# Determine when the EMA short crosses the EMA long
def ema_crossover(data, short_window, long_window):
    ShortEMA = calculate_ema(data, short_window)
    LongEMA = calculate_ema(data, long_window)

    data['Short'] = ShortEMA
    data['Long'] = LongEMA
    data['Crossover'] = ShortEMA - LongEMA

    return data

# Define the ticker symbol and the start and end dates
ticker = 'AAPL'
start_date = '2020-01-01'
end_date = '2021-12-31'

# Download the data
data = download_data(ticker, start_date, end_date)

# Calculate the EMA crossover
crossover_data = ema_crossover(data, 50, 200)

# Print the data
print(crossover_data)
```

This script downloads historical data for a given ticker symbol, calculates the short and long EMA (50 and 200 days in this case), and then determines when the short EMA crosses the long EMA. The crossover points are indicated by a change in sign of the 'Crossover' column in the dataframe.

Please note that you need to install `yfinance` and `pandas` libraries to run this script. You can install these libraries using pip:

```shell
pip install yfinance pandas
```