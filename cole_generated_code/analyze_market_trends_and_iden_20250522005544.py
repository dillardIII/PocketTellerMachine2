This task requires a complex solution and a lot of data, which is usually provided by APIs such as Alpha Vantage, Yahoo Finance, etc. Here is a simplified example of how you could use Python and the pandas library to analyze market trends. This example uses the pandas_datareader library to fetch data from Yahoo Finance.

```python
import pandas as pd
import pandas_datareader as web
from datetime import datetime, timedelta

# Define the ticker list
tickers_list = ['AAPL', 'WMT', 'IBM', 'GOOG']

# Fetch the data
data = web.get_data_yahoo(tickers_list, start=datetime.now()-timedelta(days=365), end=datetime.now())

# Print first 5 rows of the data
print(data.head())

# Calculate the moving average
data['MA_50'] = data['Adj Close'].rolling(window=50).mean()
data['MA_200'] = data['Adj Close'].rolling(window=200).mean()

# Identify potential profitable trades
# A common strategy is to buy when the 50-day moving average is above the 200-day moving average
data['Buy_Signal'] = (data['MA_50'] > data['MA_200'])

# Print data
print(data)

# Filter out the potential profitable trades
potential_trades = data[data['Buy_Signal'] == True]

# Print potential trades
print(potential_trades)
```

Please note that this is a very basic strategy and real-world trading involves a lot more factors and complex algorithms. Also, this code won't run as-is because it's just a simplified example. You need to handle exceptions, missing data, and API limitations in a real-world scenario.