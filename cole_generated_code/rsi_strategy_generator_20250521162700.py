Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It is used to identify overbought or oversold conditions in a market. Here is a simple Python code for generating RSI strategy:

```Python
import pandas as pd 
import pandas_datareader as pdr 
import numpy as np 
import datetime

def compute_rsi(data, window):
    diff = data.diff(1)
    up_chg = 0 * diff
    down_chg = 0 * diff

    # up change is equal to the positive difference, else 0
    up_chg[diff > 0] = diff[ diff>0 ]

    # down change is equal to negative difference, else 0
    down_chg[diff < 0] = diff[ diff < 0 ]

    # calculate SMA of ups and downs
    up_chg_avg   = up_chg.rolling(window).mean()
    down_chg_avg = down_chg.abs().rolling(window).mean()

    rs = abs(up_chg_avg/down_chg_avg)
    rsi = 100 - 100/(1+rs)
    return rsi

def rsi_strategy(ticker, start, end, window = 14):
    data = pdr.get_data_yahoo(ticker,start,end)
    data['RSI'] = compute_rsi(data['Close'], window)
    
    data['Buy_Signal'] = (data['RSI'] < 30) # If RSI < 30, oversold condition -> Buy
    data['Sell_Signal'] = (data['RSI'] > 70) # If RSI > 70, overbought condition -> Sell
    
    Buy_Sell = []
    
    for i in range(len(data)):
        if data['Buy_Signal'][i]:
            Buy_Sell.append('Buy')
        elif data['Sell_Signal'][i]:
            Buy_Sell.append('Sell')
        else:
            Buy_Sell.append('Hold')
    
    data['Buy_Sell'] = Buy_Sell
    
    return data

# Choose the start and end dates for our data
start = datetime.datetime(2020,1,1)
end = datetime.datetime.now()

# Use the RSI strategy function
dataframe = rsi_strategy('AAPL', start, end)
print(dataframe)
```

Note: This code retrieves historical daily price data for the specified ticker using `pandas_datareader` package. This strategy generator should be used for informational purposes only, and does not constitute financial advice. It is important to conduct your own research before making any investment decisions.