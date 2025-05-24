The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It is used to identify overbought or oversold conditions in a market. Here is a simple Python code that uses the `pandas` and `yfinance` libraries to generate an RSI strategy for a particular stock.

```python
import pandas as pd
import yfinance as yf

def calculate_RSI(data, period=14):
    delta = data.diff()
    delta = delta[1:]
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    average_gain = up.rolling(window=period).mean()
    average_loss = abs(down.rolling(window=period).mean())
    rs = average_gain / average_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def RSI_Strategy(stock, start_date, end_date):
    data = yf.download(stock, start=start_date, end=end_date)
    data['RSI'] = calculate_RSI(data['Close'])
    buy_list = []
    sell_list = []
    flag = -1
    for i in range(len(data)):
        if data['RSI'][i] < 30:
            if flag != 1:
                buy_list.append(data['Close'][i])
                sell_list.append(np.nan)
                flag = 1
            else:
                buy_list.append(np.nan)
                sell_list.append(np.nan)
        elif data['RSI'][i] > 70:
            if flag != 0:
                sell_list.append(data['Close'][i])
                buy_list.append(np.nan)
                flag = 0
            else:
                buy_list.append(np.nan)
                sell_list.append(np.nan)
        else:
            buy_list.append(np.nan)
            sell_list.append(np.nan)
    return buy_list, sell_list

stock = 'AAPL'
start_date = '2020-01-01'
end_date = '2022-01-01'
buy, sell = RSI_Strategy(stock, start_date, end_date)
```

This code first defines a function to calculate the RSI based on the closing prices of a stock over a certain period (default is 14 days). Then it defines a strategy function that downloads the historical data for a given stock from Yahoo Finance, calculates the RSI, and generates buy and sell signals based on the RSI values. If the RSI is below 30, it's a buy signal, and if it's above 70, it's a sell signal. The function returns two lists of buy and sell prices.