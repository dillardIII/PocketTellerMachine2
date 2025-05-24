Here's a basic example of how one might implement a simple trading strategy using Python. This code will not interact with real world markets, but it should serve as a good starting point for developing more complex strategies. 

This snippet uses a very basic strategy: if the 20 day moving average is greater than the 50 day moving average, we will buy the stock because it is assumed to be in an uptrend. If the 20 day average falls below the 50 day average, it will sell because the stock is assumed to be in a downtrend.

This will require the pandas, yfinance, and numpy libraries for data collection and analysis.

```python
import yfinance as yf
import pandas as pd
import numpy as np

def calculate_moving_average(data, window):
    return data['Close'].rolling(window=window).mean()

def implement_trading_strategy(data):
    # define moving averages
    ma20 = calculate_moving_average(data, 20)
    ma50 = calculate_moving_average(data, 50)

    buy_signals = (ma20 > ma50)
    sell_signals = (ma20 < ma50)

    data['Buy_Signal'] = np.where(buy_signals, 1, 0)
    data['Sell_Signal'] = np.where(sell_signals, 1, 0)

    buy_dates = data[data['Buy_Signal'] == 1].index.tolist()
    sell_dates = data[data['Sell_Signal'] == 1].index.tolist()

    trade_dict = {'buy_dates': buy_dates, 'sell_dates': sell_dates}

    return trade_dict

if __name__ == "__main__":
    # get historical market data
    ticker = 'AAPL'
    history = yf.Ticker(ticker).history(period="1y") 
    trades = implement_trading_strategy(history)
    print(trades)
```
In a real-world scenario, you should also consider transaction fees, bid-ask spread, the impact of your trades on the markets, and various other factor. Also, this is a very basic strategy and needs a lot of improvement before it can be considered a proper trading strategy. Ideally one should backtest any strategy before implementing it.