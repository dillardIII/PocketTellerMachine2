While I can't literally increase PTM's market trend prediction efforts, I can write a Python code to analyze it's current market trends. However, for a complete market analysis, I would need a vast amount of market data, which is beyond the scope of this assistant.

However, I'll show you a simple function which uses pandas and Python's stock market analysis library 'yfinance' to get PTM's latest stock data and calculate its moving averages for trend analysis. Please note that this is a simplistic example and real-world market trend prediction algorithms can be extremely complex and resource-intensive.

You need to install yfinance module using pip: 
```python
pip install yfinance
```
And here is your python code:

```python
import yfinance as yf
import pandas as pd

def calculate_moving_averages(symbol, short_window=20, long_window=50):
    # Getting historical market data
    hist = yf.Ticker(symbol).history(period="1y")

    # Calculate short and long moving averages
    hist['Short_MA'] = hist['Close'].rolling(window=short_window, min_periods=1).mean()
    hist['Long_MA'] = hist['Close'].rolling(window=long_window, min_periods=1).mean()
    
    return hist[['Close', 'Short_MA', 'Long_MA']]

# Use PTM symbol to get moving averages
ptm_data = calculate_moving_averages('PTM')
print(ptm_data)
```
This code will fetch the past 1 year data of PTM stocks, and calculate the 20-day (short term) and 50-day (long term) moving averages. You can observe the trends by comparing the short term moving averages with long term. If the short term average crosses above the long term average, it could signal an upward trend or vice versa. Please consult with a financial advisor for detailed analysis and trading decisions.

This is just one simplistic way of trend predictions, for building a sophisticated prediction model it would require complex machine learning algorithms.