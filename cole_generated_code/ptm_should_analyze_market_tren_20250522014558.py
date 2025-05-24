Creating a Python program to analyze market trends and patterns is a complex task that requires a deep understanding of both financial markets and data analysis. Here's a very basic example of how you might start building such a program using Python. This example uses the pandas library to analyze stock data.

Please note that this is a simplified example and real-world trading algorithms are much more complex.

```python
import pandas as pd
import pandas_datareader as web
import datetime as dt

# Define the ticker symbol
tickerSymbol = 'AAPL'

# Gather data from Yahoo Finance
start = dt.datetime(2020,1,1)
end = dt.datetime.now()
data = web.DataReader(tickerSymbol, 'yahoo', start, end)

# Calculate moving average
data['MA50'] = data['Close'].rolling(window=50).mean()
data['MA200'] = data['Close'].rolling(window=200).mean()

# Create a function to signal when to buy/sell the stock
def buy_sell(data):
    Buy = []
    Sell = []
    flag = -1

    for i in range(len(data)):
        if data['MA50'][i] > data['MA200'][i]:
            if flag != 1:
                Buy.append(data['Close'][i])
                Sell.append(np.nan)
                flag = 1
            else:
                Buy.append(np.nan)
                Sell.append(np.nan)
        elif data['MA50'][i] < data['MA200'][i]:
            if flag != 0:
                Sell.append(data['Close'][i])
                Buy.append(np.nan)
                flag = 0
            else:
                Buy.append(np.nan)
                Sell.append(np.nan)
        else:
            Buy.append(np.nan)
            Sell.append(np.nan)

    return (Buy, Sell)

# Add the buy and sell signals to the data
data['Buy_Signal_Price'] = buy_sell(data)[0]
data['Sell_Signal_Price'] = buy_sell(data)[1]

# Print the data
print(data)
```

This script uses a simple moving average crossover strategy to generate buy and sell signals. When the 50-day moving average crosses above the 200-day moving average, it generates a buy signal. When the 50-day moving average crosses below the 200-day moving average, it generates a sell signal. 

Please note that this is a simplified example and real-world trading algorithms are much more complex. They would take into account many more factors and use much more complex strategies. Also, this script does not take into account trading fees or other costs.