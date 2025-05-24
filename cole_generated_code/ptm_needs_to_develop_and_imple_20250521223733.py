Sure, I can provide a basic example of how you might implement a simple trading strategy in Python. For this example, let's use a simple moving average crossover strategy. This strategy buys a stock when its short term moving average crosses above its long term moving average, and sells when the opposite occurs.

First, you'll need to install the necessary libraries if you haven't already done so:

```python
pip install pandas_datareader
pip install matplotlib
```

Here's the Python code:

```python
import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt

# Define the stock to be analyzed
stock = 'AAPL'

# Define the start and end dates
start_date = '01-01-2010'
end_date = '01-01-2022'

# Load the data from web
df = web.DataReader(stock, 'yahoo', start_date, end_date)

# Calculate short-term 50 days moving average
df['50_SMA'] = df['Adj Close'].rolling(window=50).mean()

# Calculate long-term 200 days moving average
df['200_SMA'] = df['Adj Close'].rolling(window=200).mean()

# Create a function to signal when to buy and sell the asset/stock
def buy_sell(signal):
    Buy = []
    Sell = []
    flag = -1

    for i in range(len(signal)):
        if signal['50_SMA'][i] > signal['200_SMA'][i]:
            Sell.append(np.nan)
            if flag != 1:
                Buy.append(signal['Adj Close'][i])
                flag = 1
            else:
                Buy.append(np.nan)
        elif signal['50_SMA'][i] < signal['200_SMA'][i]:
            Buy.append(np.nan)
            if flag != 0:
                Sell.append(signal['Adj Close'][i])
                flag = 0
            else:
                Sell.append(np.nan)
        else:
            Buy.append(np.nan)
            Sell.append(np.nan)
            
    return (Buy, Sell)

# Create buy and sell column
df['Buy_Signal_Price'] = buy_sell(df)[0]
df['Sell_Signal_Price'] = buy_sell(df)[1]

# Plot the data
plt.figure(figsize=(12.5, 4.5))
plt.plot(df['Adj Close'], label=stock, alpha=0.35)
plt.plot(df['50_SMA'], label='50_SMA', alpha=0.35)
plt.plot(df['200_SMA'], label='200_SMA', alpha=0.35)
plt.scatter(df.index, df['Buy_Signal_Price'], color='green', label='Buy Signal', marker='^', alpha=1)
plt.scatter(df.index, df['Sell_Signal_Price'], color='red', label='Sell Signal', marker='v', alpha=1)
plt.title('Stock Buy & Sell Signals')
plt.xlabel('Date')
plt.ylabel('Adjusted Close Price')
plt.legend(loc='upper left')
plt.show()
```

This code will plot the adjusted close price, the short term moving average, the long term moving average, and points where the strategy would buy or sell the stock.

Please note that this is a very basic trading strategy and should be used for learning purposes only. In practice, trading strategies need to be much more complex and take into account many other factors.