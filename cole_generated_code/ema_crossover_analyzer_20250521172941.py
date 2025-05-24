Sure, Here's a Python code to do EMA (Exponential Moving Average) Crossover analysis on a financial time series data. In this code, I'll assume you have a `pandas DataFrame` that contains date-wise stock prices.

```python
import pandas as pd
import numpy as np
from datetime import datetime
import yfinance as yf

# Downloading data
data = yf.download('AAPL', '2020-01-01', datetime.today().strftime('%Y-%m-%d'))

# calculating short-term exponential moving average (EMA)
ShortEMA = data.Close.ewm(span=12, adjust=False).mean() 

# calculating long-term exponential moving average
LongEMA = data.Close.ewm(span=26, adjust=False).mean() 

def crossover_analysis(data):

    Buy_Signal = []
    Sell_Signal = []

    # Looping through the dataset
    for i in range(len(data)):
        # if short-term EMA is greater than long-term EMA then it's a buying signal
        if ShortEMA[i] > LongEMA[i]:
            if len(Buy_Signal) == len(Sell_Signal): 
                Buy_Signal.append(data['Close'][i]) 
                Sell_Signal.append(np.nan)
            else:
                Buy_Signal.append(np.nan)
                Sell_Signal.append(np.nan)
        # if short-term EMA is less than long-term EMA then it's a selling signal
        elif ShortEMA[i] < LongEMA[i]:
            if len(Buy_Signal) > len(Sell_Signal):
                Buy_Signal.append(np.nan)
                Sell_Signal.append(data['Close'][i])
            else:
                Buy_Signal.append(np.nan)
                Sell_Signal.append(np.nan)
        else:
            Buy_Signal.append(np.nan)
            Sell_Signal.append(np.nan)

    return Buy_Signal, Sell_Signal

# Add buying and selling signals to the dataset
data['Buy_Signal'] = crossover_analysis(data)[0]
data['Sell_Signal'] = crossover_analysis(data)[1]
```

Note: You'll need the yfinance package for downloading the stock data. If you don't have the package installed, you can use pip to install it:

```python
pip install yfinance
```