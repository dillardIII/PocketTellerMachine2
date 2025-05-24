To develop and implement new trading strategies, we need to have a clear understanding of the financial market data. Here is a simple Python code using pandas and yfinance libraries to fetch the stock market data. We can then analyze this data to develop new trading strategies.

```python
import pandas as pd
import yfinance as yf

# Define the ticker symbol
tickerSymbol = 'AAPL'

# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2020-1-25')

# See your data
print(tickerDf)
```

This code will fetch the historical data for Apple Inc. from 2010 to 2020. You can replace 'AAPL' with any other company's ticker symbol to fetch its data.

To develop a trading strategy, you might need to analyze this data based on various parameters like moving averages, RSI, MACD, etc. Here is a simple example of a trading strategy based on moving averages:

```python
# Calculate 20 day moving average
tickerDf['20_SMA'] = tickerDf['Close'].rolling(window=20).mean()

# Calculate 50 day moving average
tickerDf['50_SMA'] = tickerDf['Close'].rolling(window=50).mean()

# Create a function to signal when to buy and sell an asset
def implement_strategy(data):
    buy_list = []
    sell_list = []
    flag = False

    for i in range(len(data)):
        if data['20_SMA'][i] > data['50_SMA'][i]:
            if flag != True:
                buy_list.append(data['Close'][i])
                sell_list.append(np.nan)
                flag = True
            else:
                buy_list.append(np.nan)
                sell_list.append(np.nan)
        elif data['20_SMA'][i] < data['50_SMA'][i]:
            if flag != False:
                sell_list.append(data['Close'][i])
                buy_list.append(np.nan)
                flag = False
            else:
                buy_list.append(np.nan)
                sell_list.append(np.nan)
        else:
            buy_list.append(np.nan)
            sell_list.append(np.nan)

    return (buy_list, sell_list)

# Implement the strategy
buy_sell = implement_strategy(tickerDf)
tickerDf['Buy_Signal_Price'] = buy_sell[0]
tickerDf['Sell_Signal_Price'] = buy_sell[1]
```

This strategy will signal to buy the stock when the 20-day moving average is above the 50-day moving average and sell the stock when the 20-day moving average is below the 50-day moving average.

Please note that this is a very basic trading strategy and might not be profitable in the real world. It's always recommended to backtest any strategy before implementing it in live trading.