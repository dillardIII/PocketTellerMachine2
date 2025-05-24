Sure, here is a simple Python code implementing a basic moving average crossover strategy using pandas library. This strategy buys a stock when the short term moving average crosses above the long term moving average and sells when the short term moving average crosses below the long term moving average.

```python
import pandas as pd
import yfinance as yf

# Download historical data for desired ticker symbol
def download_data(stock, start, end):
    data = {}
    ticker = yf.download(stock, start, end)
    data['Price'] = ticker['Adj Close']
    return pd.DataFrame(data)

# Calculate moving averages
def calculate_MA(data, short_window, long_window):
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0

    # Short moving average
    signals['short_mavg'] = data['Price'].rolling(window=short_window, min_periods=1, center=False).mean()

    # Long moving average
    signals['long_mavg'] = data['Price'].rolling(window=long_window, min_periods=1, center=False).mean()

    # Create signals
    signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] 
                                                > signals['long_mavg'][short_window:], 1.0, 0.0)   
    signals['positions'] = signals['signal'].diff()

    return signals

# Implement the strategy
def implement_strategy(signals, data):
    initial_capital= float(100000.0)
    positions = pd.DataFrame(index=signals.index).fillna(0.0)
    portfolio = pd.DataFrame(index=signals.index).fillna(0.0)

    positions['Stock'] = signals['signal']
    portfolio['positions'] = (positions.multiply(data['Price'], axis=0))
    portfolio['cash'] = initial_capital - (positions.diff().multiply(data['Price'], axis=0)).cumsum()   
    portfolio['total'] = portfolio['positions'] + portfolio['cash']

    return portfolio

if __name__ == "__main__":
    data = download_data('AAPL', '01-01-2010', '01-01-2022')
    signals = calculate_MA(data, 40, 100)
    portfolio = implement_strategy(signals, data)
    print(portfolio)
```

This code uses yfinance to download historical stock data, pandas to handle data and calculate moving averages, and numpy to generate trading signals. Please note that this is a very simple strategy and may not be profitable in real trading. Always backtest your strategies before live trading.