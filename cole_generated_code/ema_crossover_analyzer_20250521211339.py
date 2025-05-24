Sure, here's a simple implementation of an EMA crossover analyzer using Python and the pandas library. This script will calculate the EMA for two different periods and then determine when the EMAs cross over each other.

```python
import pandas as pd
import pandas_datareader as web
import datetime

# Define the symbols to download. We would like to see Apple, Microsoft and the S&P500 index.
symbol = 'AAPL'

# Define which online source one should use
data_source = 'yahoo'

# We would like all available data from 01/01/2000 until 12/31/2016.
start_date = '2000-01-01'
end_date = '2016-12-31'

# User pandas_reader.data.DataReader to load the desired data. As simple as that.
df = web.DataReader(symbol, data_source, start_date, end_date)

# Calculate the short and long window simple moving averages
short_window = 40
long_window = 100

signals = pd.DataFrame(index=df.index)
signals['signal'] = 0.0

# Short moving average
signals['short_mavg'] = df['Close'].ewm(span=short_window, adjust=False).mean()

# Long moving average
signals['long_mavg'] = df['Close'].ewm(span=long_window, adjust=False).mean()

# Create signals
signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] 
                                            > signals['long_mavg'][short_window:], 1.0, 0.0)   

# Generate trading orders
signals['positions'] = signals['signal'].diff()

# Print `signals`
print(signals)
```

This script will print a DataFrame that shows the short and long EMA for each day, as well as the trading signals generated when the short EMA crosses the long EMA. A signal of 1.0 means that the short EMA has crossed above the long EMA (indicating a potential buy signal), while a signal of -1.0 means that the short EMA has crossed below the long EMA (indicating a potential sell signal).