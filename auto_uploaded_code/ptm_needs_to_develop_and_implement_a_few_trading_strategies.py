Sure, I can help you write a basic Python code for a simple trading strategy. However, please note that trading involves risks and this code is just a simple example and should not be used for real trading without proper modifications and understanding.

Here is an example of a simple moving average crossover strategy using Python and pandas. This strategy buys when the short term moving average crosses above the long term moving average, and sells when the short term moving average crosses below the long term moving average.

```python
import pandas as pd
import pandas_datareader as pdr
import datetime

# Define the ticker symbol
tickerSymbol = 'AAPL'

# Gather the data
start = datetime.datetime(2020,1,1)
end = datetime.datetime(2021,1,1)
df = pdr.get_data_yahoo(tickerSymbol, start, end)

# Calculate the short term and long term moving averages
short_window = 40
long_window = 100
signals = pd.DataFrame(index=df.index)
signals['signal'] = 0.0
signals['short_mavg'] = df['Close'].rolling(window=short_window, min_periods=1, center=False).mean()
signals['long_mavg'] = df['Close'].rolling(window=long_window, min_periods=1, center=False).mean()

# Create signals
signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] 
                                            > signals['long_mavg'][short_window:], 1.0, 0.0)   
signals['positions'] = signals['signal'].diff()

# Print the DataFrame
print(signals)
```

This code first fetches historical data for a specific ticker symbol (in this case, AAPL for Apple Inc.) from Yahoo Finance. Then it calculates the short term (40 days) and long term (100 days) moving averages. It generates a buy signal when the short term moving average crosses above the long term moving average, and a sell signal when the short term moving average crosses below the long term moving average.

Please note that you need to install pandas_datareader library to run this code. You can install it via pip:

```python
pip install pandas_datareader
```

Also, this is a very basic strategy and doesn't take into account transaction costs, slippage, risk management, etc. It's important to thoroughly backtest any strategy before live trading.