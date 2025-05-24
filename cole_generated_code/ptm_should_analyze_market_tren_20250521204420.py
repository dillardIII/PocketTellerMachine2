To analyze market trends and data, we need to use some libraries like pandas for data manipulation, matplotlib for data visualization, and yfinance to download the historical market data from Yahoo finance. 

Please note that this is a simple example and real trading algorithms require much more complex analysis and strategies. 

```python
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Download historical data as dataframe
data = yf.download('AAPL','2016-01-01','2021-12-31')

# Calculate the moving average
data['MA_50'] = data['Close'].rolling(50).mean()
data['MA_200'] = data['Close'].rolling(200).mean()

# Identify potential trading opportunities
# Buy signal: when MA_50 crosses above MA_200
# Sell signal: when MA_50 crosses below MA_200
data['Buy_Signal'] = (data['MA_50'] > data['MA_200']).astype(int)
data['Sell_Signal'] = (data['MA_50'] < data['MA_200']).astype(int)

# Plot the close price and moving averages
plt.figure(figsize=(12,5))
plt.plot(data['Close'], label='Close Price', color='blue')
plt.plot(data['MA_50'], label='50 Day MA', color='red')
plt.plot(data['MA_200'], label='200 Day MA', color='green')
plt.legend(loc='best')
plt.show()

# Print potential trading opportunities
print('Potential Buy Signals:')
print(data.loc[data['Buy_Signal'] == 1])

print('Potential Sell Signals:')
print(data.loc[data['Sell_Signal'] == 1])
```

This script will download the historical data for Apple Inc. (AAPL) from 2016 to 2021, calculate the 50-day and 200-day moving averages, generate buy and sell signals based on these moving averages, plot the close price and moving averages, and print the potential trading opportunities. 

Please note that this is a very simple trading strategy and it's not recommended to use it for real trading without further improvements and adjustments.