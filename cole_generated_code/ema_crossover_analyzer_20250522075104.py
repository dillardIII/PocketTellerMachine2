from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here's a simple Python code using pandas library to analyze Exponential Moving Average (EMA) crossover.

```python
import pandas as pd
import pandas_datareader as pdr
import datetime

# Define the instrument to download
ticker = 'AAPL'

# Define which online source to use
data_source = 'yahoo'

# Define the start and end dates
start_date = datetime.datetime.now() - datetime.timedelta(days=365)
end_date = datetime.datetime.now()

# Use pandas_datareader to load the desired data
df = pdr.DataReader(ticker, data_source, start_date, end_date)

# Calculate short-term EMA (e.g., 9 days)
short_EMA = df['Close'].ewm(span=9, adjust=False).mean()

# Calculate long-term EMA (e.g., 21 days)
long_EMA = df['Close'].ewm(span=21, adjust=False).mean()

# Create signals based on crossover
df['Buy_Signal'] = (short_EMA > long_EMA)
df['Sell_Signal'] = (short_EMA < long_EMA)

# Print the DataFrame
print(df)
```

This script will download the historical data for the specified ticker symbol, calculate the short-term and long-term EMA, and then create two new columns in the DataFrame: 'Buy_Signal' and 'Sell_Signal'. These columns will contain boolean values indicating whether a buy or sell signal has been triggered based on the EMA crossover.

Please note that you need to install pandas_datareader library if it's not already installed. You can install it using pip:

```bash
pip install pandas_datareader
```

Also, this is a very basic EMA crossover strategy. In real trading scenarios, you would need to consider many other factors and use more sophisticated algorithms.