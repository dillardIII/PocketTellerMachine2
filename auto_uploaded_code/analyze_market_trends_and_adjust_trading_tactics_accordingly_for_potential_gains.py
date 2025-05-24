Analyzing market trends and adjusting trading tactics accordingly is a complex task that involves a lot of data analysis and possibly machine learning. Here is a simple example of how you can analyze market trends using Python with the help of pandas and yfinance libraries. 

```python
import pandas as pd
import yfinance as yf
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Download historical data as dataframe
data = yf.download('AAPL','2020-01-01','2022-12-31')

# Calculate the short term exponential moving average (EMA)
ShortEMA = data.Close.ewm(span=12, adjust=False).mean()

# Calculate the long term exponential moving average
LongEMA = data.Close.ewm(span=26, adjust=False).mean()

# Calculate the Moving Average Convergence/Divergence (MACD)
MACD = ShortEMA - LongEMA

# Calculate the signal line
signal = MACD.ewm(span=9, adjust=False).mean()

# Create a new column in the dataframe for the strategy
data['Buy_Signal_Price'] = 0
data['Sell_Signal_Price'] = 0

# Create a flag to indicate whether the stock is being held
flag = -1

# Loop through the dataframe
for i in range(len(data)):
    if MACD[i] > signal[i]:  # A good time to buy
        if flag != 1:
            data['Buy_Signal_Price'][i] = data['Close'][i]
            flag = 1
    elif MACD[i] < signal[i]:  # A good time to sell
        if flag != 0:
            data['Sell_Signal_Price'][i] = data['Close'][i]
            flag = 0

print(data)
```

This script downloads the historical price data for a specific stock (in this case, Apple Inc.), calculates the MACD and the signal line, and then generates buy and sell signals based on these indicators.

Please note that this is a very basic trading strategy and may not be profitable in real trading. A more sophisticated strategy may involve multiple indicators, machine learning algorithms, and possibly other sources of data. Always test your trading strategies with historical data before using them in real trading.