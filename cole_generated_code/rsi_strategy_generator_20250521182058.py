The RSI (Relative Strength Index) strategy is commonly used in trading as a momentum oscillator to measure the speed and change of price movements. Below is an example of how you could generate a simple RSI trading strategy using Python, pandas and yfinance libraries. 

```python
# Import required libraries
import pandas as pd
import yfinance as yf
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
from datetime import datetime

# set the start and end date for the data
start_date = datetime(2020, 6, 1)
end_date = datetime(2021, 6, 1)

# Download historical data as dataframe
data = pdr.get_data_yahoo('GOOGL', start=start_date, end=end_date)

# Calculate the RSI
delta = data['Close'].diff()
gain = (delta > 0) * delta
loss = (delta < 0) * -delta
average_gain = gain.rolling(window=14).mean()
average_loss = loss.rolling(window=14).mean()
rs = average_gain / average_loss
rsi = 100 - (100 / (1 + rs))

# Generate RSI Strategy
data['Buy_Signal'] = (rsi < 30)
data['Sell_Signal'] = (rsi > 70)

# Print data
print(data)

# Plot data
plt.figure(figsize=(12, 5))
plt.plot(data.index, data['Close'], label='Google Price', color='lightgray')
plt.plot(data[data['Buy_Signal']].index, data[data['Buy_Signal']]['Close'], 
         '^', color='g', markersize=12, label='Buy Signal')
plt.plot(data[data['Sell_Signal']].index, data[data['Sell_Signal']]['Close'], 
         'v', color='r', markersize=12, label='Sell Signal')
plt.legend()
plt.show()
```
This script calculates the RSI index and selects the points where a stock should be bought or sold. It assumes that a stock should be bought when RSI < 30 (being underbought) and sold when RSI > 70 (being overbought). Then it plots the closing prices of the stock, with green up arrows representing buy signals and red down arrows representing sell signals. The example uses Google's stock (GOOGL).

Please remember that this is a very simple strategy and real-life trading systems are much more complex and take more factors into account when deciding whether to buy or sell. Always backtest your strategy on historical data before you try it on the live market.