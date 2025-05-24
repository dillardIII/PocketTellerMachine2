Sure, here is a simple Python script using the `pandas` library to analyze market trends. This script will calculate the moving average of a stock price over a certain period of time, which is a common method used to identify potential trading opportunities.

Please note that this is a very basic example and real-world trading algorithms are much more complex and take many more factors into account.

```python
import pandas as pd
import pandas_datareader as web
import datetime

# Define the stock to analyse and the time period
stock = 'AAPL'
start_date = datetime.datetime(2020, 1, 1)
end_date = datetime.datetime(2021, 12, 31)

# Download the stock price data
df = web.DataReader(stock, 'yahoo', start_date, end_date)

# Calculate the 20 day moving average
df['20 Day MA'] = df['Close'].rolling(window=20).mean()

# Calculate the 200 day moving average
df['200 Day MA'] = df['Close'].rolling(window=200).mean()

# Create a column to hold the buy/sell signals
df['Buy Signal'] = (df['20 Day MA'] > df['200 Day MA']).astype(int).diff()

# Print the dataframe
print(df)
```

This script will print a dataframe with the stock's closing price, the 20 day moving average, the 200 day moving average, and a column for buy signals. A buy signal is generated when the 20 day moving average crosses above the 200 day moving average.

Please note that you will need to install the `pandas_datareader` library if you haven't already. You can do this with the following command:

```python
pip install pandas_datareader
```

Also, please be aware that this script uses Yahoo Finance to download stock price data, which may not always be available due to changes in Yahoo's API. There are many other sources of stock price data available, some free and some paid.