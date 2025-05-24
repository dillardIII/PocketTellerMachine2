To accomplish this task, we will need to use the pandas library for data manipulation and the yfinance library to download the stock price data. The Moving Average Convergence Divergence (MACD) is a trend-following momentum indicator that shows the relationship between two moving averages of a security’s price.

Here is a simple Python code to calculate the MACD and Signal line indicators and then scan for the condition where MACD crosses above the Signal line.

```python
import pandas as pd
import yfinance as yf

def calculate_macd(data, short_term, long_term):
    short_ema = data.ewm(span=short_term, adjust=False).mean()
    long_ema = data.ewm(span=long_term, adjust=False).mean()
    macd = short_ema - long_ema
    signal = macd.ewm(span=9, adjust=False).mean()
    return macd, signal

def macd_crossover(data):
    macd, signal = calculate_macd(data['Close'], 12, 26)
    data['MACD'] = macd
    data['Signal Line'] = signal
    data['Crossover'] = data['MACD'] > data['Signal Line']
    return data[data['Crossover'] == True]

# Download historical data as dataframe
data = yf.download('AAPL', start='2020-01-01', end='2022-12-31')

# Scan for MACD crossover
crossover_data = macd_crossover(data)
print(crossover_data)
```

This code first downloads the historical price data for the specified stock (in this case, Apple Inc.) using the yfinance library. It then calculates the MACD and Signal line values and adds them as new columns to the dataframe. Finally, it scans for the condition where the MACD line crosses above the Signal line and returns those data points.

Please note that you need to install the required libraries using pip:

```bash
pip install pandas yfinance