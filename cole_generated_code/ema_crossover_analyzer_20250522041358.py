from ghost_env import INFURA_KEY, VAULT_ADDRESS
The Exponential Moving Average (EMA) Crossover is a popular tool among traders because it can indicate potential buying or selling opportunities. Here is a simple Python code using pandas library to analyze EMA crossover.

```python
import pandas as pd
import pandas_datareader as web
import datetime as dt

# Define the ticker symbol
tickerSymbol = 'AAPL'

# Gather data from Yahoo finance
start = dt.datetime(2020,1,1)
end = dt.datetime.now()
data = web.DataReader(tickerSymbol, 'yahoo', start, end)

# Calculate the Short Term EMA
ShortEMA = data.Close.ewm(span=12, adjust=False).mean()

# Calculate the Long Term EMA
LongEMA = data.Close.ewm(span=26, adjust=False).mean()

# Calculate and store the MACD Line and Signal Line indicators
data['Short EMA'] = ShortEMA
data['Long EMA'] = LongEMA

# Create a function to signal when to buy and sell an asset
def EMA_Crossover(data):
    Buy_Signal = []
    Sell_Signal = []

    for i in range(len(data)):
        if ShortEMA[i] > LongEMA[i]:
            Buy_Signal.append(data['Close'][i])
            Sell_Signal.append(np.nan)
        elif ShortEMA[i] < LongEMA[i]:
            Sell_Signal.append(data['Close'][i])
            Buy_Signal.append(np.nan)
        else:
            Buy_Signal.append(np.nan)
            Sell_Signal.append(np.nan)

    return (Buy_Signal, Sell_Signal)

# Create buy and sell columns
data['Buy_Signal_Price'] = EMA_Crossover(data)[0]
data['Sell_Signal_Price'] = EMA_Crossover(data)[1]

print(data)
```

This code will print out the dataframe with 'Buy_Signal_Price' and 'Sell_Signal_Price' columns. When the short-term EMA crosses above the long-term EMA, it's a buy signal, and when it crosses below, it's a sell signal. The buy and sell prices are the closing prices of the days when these crossovers occur.