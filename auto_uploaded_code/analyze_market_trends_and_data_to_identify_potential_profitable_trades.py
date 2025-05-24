Analyzing market trends and data for potential profitable trades is a complex task that involves machine learning and data analysis. Here's a simple Python code using pandas and yfinance to get historical market data and calculate Simple Moving Average (SMA) as a basic trading strategy.

```python
import pandas as pd
import yfinance as yf

# Define the ticker symbol
tickerSymbol = 'AAPL'

# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2020-12-31')

# Calculate the Simple Moving Average with a 30 day window
SMA_30 = pd.DataFrame()
SMA_30['Close Price'] = tickerDf['Close'].rolling(window=30).mean()

# Calculate the Simple Moving Average with a 100 day window
SMA_100 = pd.DataFrame()
SMA_100['Close Price'] = tickerDf['Close'].rolling(window=100).mean()

# Create a new data frame to store all the data
data = pd.DataFrame()
data['AAPL'] = tickerDf['Close']
data['SMA_30'] = SMA_30['Close Price']
data['SMA_100'] = SMA_100['Close Price']

# Create a function to signal when to buy and sell an asset
def buy_sell(data):
    sigPriceBuy = []
    sigPriceSell = []
    flag = -1

    for i in range(len(data)):
        if data['SMA_30'][i] > data['SMA_100'][i]:
            if flag != 1:
                sigPriceBuy.append(data['AAPL'][i])
                sigPriceSell.append(np.nan)
                flag = 1
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)
        elif data['SMA_30'][i] < data['SMA_100'][i]:
            if flag != 0:
                sigPriceSell.append(data['AAPL'][i])
                sigPriceBuy.append(np.nan)
                flag = 0
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)
        else:
            sigPriceBuy.append(np.nan)
            sigPriceSell.append(np.nan)

    return (sigPriceBuy, sigPriceSell)

# Store the buy and sell data into a variable
buy_sell = buy_sell(data)
data['Buy_Signal_Price'] = buy_sell[0]
data['Sell_Signal_Price'] = buy_sell[1]

# Print the data
print(data)
```

This script uses a simple moving average crossover strategy. It signals to buy when the 30-day SMA crosses above the 100-day SMA and to sell when the 30-day SMA crosses below the 100-day SMA. Please note that this is a very basic trading strategy and should not be used for actual trading without further enhancements.