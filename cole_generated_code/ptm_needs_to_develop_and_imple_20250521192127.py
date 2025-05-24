Sure, I can provide a simple example of a Python code that could be used for a basic trading strategy. This strategy will be based on a simple moving average (SMA). Please note that this is a very basic strategy and real-world trading strategies can be much more complex.

```python
import pandas as pd
import yfinance as yf

def calculate_sma(data, window):
    return data.rolling(window=window).mean()

def trading_strategy(data, short_window, long_window):
    # Calculate the short and long window simple moving averages
    data['short_sma'] = calculate_sma(data['Close'], short_window)
    data['long_sma'] = calculate_sma(data['Close'], long_window)

    # Create a column 'Signal' such that if the short window SMA is greater than the long window SMA, then set 'Signal' as 1 else 0
    data['Signal'] = 0.0  
    data['Signal'][short_window:] = np.where(data['short_sma'][short_window:] > data['long_sma'][short_window:], 1.0, 0.0)   

    # Create a column 'Position' which is the difference of the 'Signal' column
    data['Position'] = data['Signal'].diff()

def main():
    # Download historical data as dataframe
    data = yf.download('AAPL', start='2020-01-01', end='2022-12-31')

    # Implement the trading strategy
    trading_strategy(data, 50, 200)

    # Print data
    print(data)

if __name__ == "__main__":
    main()
```

In this code, we first download the historical data for a specific stock (in this case, Apple Inc.) using the `yfinance` library. Then, we calculate the short and long window simple moving averages (SMA) and create a 'Signal' column in our dataframe. If the short window SMA is greater than the long window SMA, we set 'Signal' as 1, else 0. Finally, we create a 'Position' column which is the difference of the 'Signal' column. This 'Position' column can be used to decide when to buy or sell the stock.

Please note that you need to install `pandas`, `yfinance` and `numpy` to run this code. You can install them using pip:

```
pip install pandas yfinance numpy
```

Also, this is a very basic trading strategy and might not be profitable in real-world trading. It's always recommended to thoroughly backtest any trading strategy before live trading.