Here are a few ways to implement profitable trades with Python:

1. Moving average crossover strategy
2. Bollinger band strategy
3. Momentum trading strategy

First off, make sure you have all the necessary Python libraries installed:
```python
!pip install pandas_datareader
!pip install yfinance --upgrade --no-cache-dir
!pip install matplotlib
!pip install numpy
!pip install scipy
```

Here's an example of moving average crossover strategy:

```python
import pandas_datareader as pdr
import datetime 
import matplotlib.pyplot as plt
import yfinance as yf 
yf.pdr_override()

#define start and end date
start = datetime.datetime(2020, 1, 1)
end = datetime.datetime(2021, 8, 1)

#define the ticker symbol
tickerSymbol = "AAPL"

#get data on this ticker
df = pdr.get_data_yahoo(tickerSymbol, start=start, end=end)

# Calculate 30 Day Moving Average, Std Deviation, Upper Band and Lower Band
df['30 Day MA'] = df['Close'].rolling(window=20).mean()

# set style, empty figure and axes
plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot(111)

# plot adjusted close price
ax.plot(df['Close'], color = 'blue', label='Original')
# plot the short and long moving averages
ax.plot(df['30 Day MA'], color = 'red', label = '30 Day MA')

ax.set_title('30 Day Moving Average')
ax.set_xlabel('Date')
ax.set_ylabel('Price')
ax.legend(loc='best')
plt.show()

# Create a signal
df['Signal'] = 0.0  
df['Signal'][short_window:] = np.where(df['30 Day MA'][short_window:] 
                                              > df['Close'][short_window:], 1.0, 0.0)   
df['Position'] = df['Signal'].diff() 

# When the short moving average is above the long-term moving average, it signals that we should buy
df.loc[df['Position'] == 1]

# When the short moving average is below the long-term moving average, it signals that we should sell
df.loc[df['Position'] == -1]
```

This represents a simple Moving average crossover strategy. A buy signal is generated when a short-term average crosses above a long-term average. Similarly, a sell signal is issued when a short-term average crosses below a long-term average. 

In this example, Apple Inc. (AAPL) is used but the ticker symbol can be replaced with any valid ticker symbol to perform analysis on different stocks. Please remember that this is a simplistic strategy and can't guarantee any profitable trades. More complex strategies can be developed including combinations of different indicators.