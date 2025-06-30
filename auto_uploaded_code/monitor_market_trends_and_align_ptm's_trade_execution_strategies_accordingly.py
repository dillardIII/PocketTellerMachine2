from ghost_env import INFURA_KEY, VAULT_ADDRESS
This kind of task requires extensive coding and is only exposed via certain API's, usually provided from Brokerage firms. There are many approaches to this task, so below I've outlined a very simplified layout of what the architecture of such a program might look like.

The script below uses the yfinance library (Yahoo Finance's API) to retrieve market data, and pandas library to manipulate the data.

It doesn't implement the trade execution or the strategy parts. Because these tasks are highly personalized and depend on your specific requirements. You can implement them using a broker API, such as Interactive Brokers or Alpaca.

Remember that this simple Python script does not have any real trading implementation and it's for educational purposes only. Actual trading involves far more complexities and considerations.

```python
import yfinance as yf
import pandas as pd

# Download historical data for required stocks
tickers = ["AAPL", "MSFT", "GOOG", "AMZN"]

# The interval and period for which we'll get data: daily data for the past 5 years
interval, period = '1d', '5y'
data = yf.download(tickers, interval=interval, period=period, group_by='ticker')

# Calculate the moving average
def calculate_moving_average(data, window):
    return data['Close'].rolling(window=window).mean()

# Strategy: if the short moving average is above the long moving average, then we'll buy, else we'll sell
def align_strategy(data, short_window, long_window):
    short_mavg = calculate_moving_average(data, short_window)
    long_mavg = calculate_moving_average(data, long_window)
  
    buy_signals = short_mavg > long_mavg
    sell_signals = short_mavg < long_mavg

    return buy_signals, sell_signals

# For each stock, print out if we should currently buy or sell according to our strategy
for ticker in tickers:
    data_ticker = data[ticker]
  
    buy_signals, sell_signals = align_strategy(data_ticker, 50, 200)

    if buy_signals.iloc[-1]:
        decision = 'buy'
    else:
        decision = 'sell'
    
    print("For stock {} we should {}".format(ticker, decision))
```

As mentioned before: This is an oversimplified example meant to illustrate the primary ideas about how one might structure this type of program. Real trading systems consider a lot more factors (bid-ask spread, order book depth, portfolio diversification and risk management etc.) and have much more complex conditions for buying/selling. Furthermore, backtesting on historical data is absolutely essential before considering live deployment of any trading algorithm. For this purpose, you should learn about backtrader, zipline, pyalgotrade, etc. Python libraries.