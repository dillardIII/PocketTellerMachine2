Sure, here is a simple Python code to analyze EMA crossover using pandas for data manipulation and yfinance to download the stock data. 

```python
import pandas as pd
import yfinance as yf

def calculate_ema(data, window):
    return data.ewm(span=window, adjust=False).mean()

def ema_crossover_analyzer(stock, short_window, long_window):
    # Download historical data as dataframe
    data = yf.download(stock, start='2020-01-01', end='2022-12-31')

    # Calculate short and long EMA
    data['Short_EMA'] = calculate_ema(data['Close'], short_window)
    data['Long_EMA'] = calculate_ema(data['Close'], long_window)

    # Create signals
    data['Buy_Signal'] = (data['Short_EMA'] > data['Long_EMA'])
    data['Sell_Signal'] = (data['Short_EMA'] < data['Long_EMA'])

    # Print data
    print(data)

# Test the function
ema_crossover_analyzer('AAPL', 12, 26)
```
This script will download the historical data for the given stock (in this case, AAPL) and calculate the short and long EMA (12 and 26 days respectively in this case). It will then create a buy signal when the short EMA is above the long EMA and a sell signal when the short EMA is below the long EMA. The resulting dataframe will be printed to the console. 

Please note that this is a very basic implementation and might need to be adjusted based on the specific requirements and conditions.