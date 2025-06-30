from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here's a simple example of a Python code that implements and tests a basic moving average crossover trading strategy using the pandas library. This strategy generates a buy signal when the short-term moving average crosses above the long-term moving average, and a sell signal when the short-term moving average crosses below the long-term moving average.

```python
import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt

# Define the stock symbol and the time period
stock = 'AAPL'
start_date = '01-01-2020'
end_date = '12-31-2020'

# Download the stock price data
df = web.DataReader(stock, 'yahoo', start_date, end_date)

# Calculate the short-term and long-term moving averages
short_window = 50
long_window = 200
signals = pd.DataFrame(index=df.index)
signals['signal'] = 0.0
signals['short_mavg'] = df['Close'].rolling(window=short_window, min_periods=1, center=False).mean()
signals['long_mavg'] = df['Close'].rolling(window=long_window, min_periods=1, center=False).mean()

# Generate trading signals
signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] 
                                            > signals['long_mavg'][short_window:], 1.0, 0.0)   
signals['positions'] = signals['signal'].diff()

# Plot the data
fig = plt.figure()
ax1 = fig.add_subplot(111, ylabel='Price in $')
df['Close'].plot(ax=ax1, color='r', lw=2.)
signals[['short_mavg', 'long_mavg']].plot(ax=ax1, lw=2.)
ax1.plot(signals.loc[signals.positions == 1.0].index, 
         signals.short_mavg[signals.positions == 1.0],
         '^', markersize=10, color='m')
ax1.plot(signals.loc[signals.positions == -1.0].index, 
         signals.short_mavg[signals.positions == -1.0],
         'v', markersize=10, color='k')
plt.show()
```

This code will plot the stock's closing price, the short-term moving average, the long-term moving average, and the buy and sell signals. Please note that this is a simple trading strategy for illustrative purposes only and may not be profitable in actual trading. Always do your own research and consider consulting with a financial advisor before trading.