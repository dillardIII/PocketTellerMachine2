Python code below designs a simple moving average crossover trading strategy. We make an assumption that if the short term average crosses above the long term average then it's a signal to buy and vice versa. It's important to mention that this is a simplified version and in practice, more complexities have to be tackled.

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr

# Function to calculate moving average
def calculate_moving_average(data, window):
    return data.rolling(window=window).mean()

def trading_strategy(data, short_window, long_window):
    # Create a "signals" DataFrame to store the buy and sell signals
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0

    # Calculate short and long moving averages
    signals['short_mavg'] = calculate_moving_average(data['Close'], short_window)
    signals['long_mavg'] = calculate_moving_average(data['Close'], long_window)

    # Create signals: when short MA crosses above long MA, we buy (signal=1); when short MA crosses below long MA, we sell (signal=-1)
    signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] > signals['long_mavg'][short_window:], 1.0, -1.0)   

    # Generate trading orders: difference between consecutive signals. A change from 1 to -1 implies sell, a change from -1 to 1 implies buy
    signals['positions'] = signals['signal'].diff()
    
    return signals

# Fetch data
ticker = 'AAPL'
data = pdr.get_data_yahoo(ticker, start='2020-01-01', end='2021-12-31')

# Define short and long window
short_window = 50
long_window = 200

# Run trading strategy
signals = trading_strategy(data, short_window, long_window)

buy_signals = signals[signals.positions==1]
sell_signals = signals[signals.positions==-1]
print("Buy Signals:")
print(buy_signals)
print("Sell Signals:")
print(sell_signals)
```

This strategy will tell you when to buy and sell the chosen stock based on moving averages crossover. But note that real-world trading is much more complicated and involves factors not considered in this simple approach.

Also, you have to install pandas_datareader module to get the financial data, use following command to install it:

    pip install pandas_datareader
   
Make sure the start and end dates, ticker symbols, and moving average windows fit your needs.