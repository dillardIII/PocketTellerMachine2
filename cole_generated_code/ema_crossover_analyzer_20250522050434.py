Sure, here is a simple Python code using `pandas` and `yfinance` to analyze EMA crossover for a specific stock. This code calculates the 50-day and 200-day EMA for a stock and identifies the crossover points. 

```python
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Download historical data as dataframe
data = yf.download('AAPL', start='2020-01-01', end='2022-12-31')

# Calculate 50-day EMA
data['50_EMA'] = data['Close'].ewm(span=50, adjust=False).mean()

# Calculate 200-day EMA
data['200_EMA'] = data['Close'].ewm(span=200, adjust=False).mean()

# Identify where the 50-day EMA is greater than the 200-day EMA
data['Buy_Signal'] = data['50_EMA'] > data['200_EMA']

# Identify where the 50-day EMA is less than the 200-day EMA
data['Sell_Signal'] = data['50_EMA'] < data['200_EMA']

# Print data
print(data)

# Plot data
plt.figure(figsize=(12,5))
plt.plot(data['Close'], label='Close Price', color='blue')
plt.plot(data['50_EMA'], label='50-day EMA', color='red')
plt.plot(data['200_EMA'], label='200-day EMA', color='green')
plt.title('Apple EMA Crossover')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(loc='upper left')
plt.show()
```

This code will print out the dataframe with the calculated EMAs and whether there is a buy or sell signal for each day. It will also plot the close price, 50-day EMA, and 200-day EMA on a graph. Please replace 'AAPL' with the ticker symbol of the stock you want to analyze.

Please note that this is a simple example and does not take into account trading fees or other factors that might influence trading decisions. Always do your own research before making trading decisions.