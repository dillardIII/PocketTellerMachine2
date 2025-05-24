Sure, here is a simple Python code using pandas library to analyze EMA (Exponential Moving Average) crossover.

```python
import pandas as pd
import pandas_datareader as web
import datetime

def calculate_ema(data, window):
    return data.ewm(span=window, adjust=False).mean()

def ema_crossover_analyzer(stock, short_window, long_window):
    end = datetime.datetime.now()
    start = datetime.date(end.year - 5, end.month, end.day)
    
    data = web.DataReader(stock, 'yahoo', start, end)
    close = data['Close']
    
    short_ema = calculate_ema(close, short_window)
    long_ema = calculate_ema(close, long_window)
    
    crossover = pd.DataFrame(index=close.index)
    crossover['signal'] = 0.0
    crossover['short_ema'] = short_ema
    crossover['long_ema'] = long_ema
    crossover['signal'][short_window:] = np.where(crossover['short_ema'][short_window:] > crossover['long_ema'][short_window:], 1.0, 0.0)
    crossover['positions'] = crossover['signal'].diff()
    
    return crossover

# Test the function
crossover = ema_crossover_analyzer('AAPL', 50, 200)
print(crossover)
```

This code first fetches the historical data of the specified stock from Yahoo Finance. Then it calculates the short-term and long-term EMA of the closing prices. A buy signal is generated when the short-term EMA crosses above the long-term EMA, and a sell signal is generated when the short-term EMA crosses below the long-term EMA.

Please note that you need to install `pandas_datareader` library to fetch data from Yahoo Finance. You can install it using pip:

```bash
pip install pandas_datareader
```

Also, please replace `'AAPL'` with the symbol of the stock you want to analyze, and replace `50` and `200` with the lengths of the short-term and long-term windows you want to use.