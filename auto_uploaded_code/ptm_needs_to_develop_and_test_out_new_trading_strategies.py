To develop and test out new trading strategies, we will use the pandas library for data analysis, numpy for numerical calculations, and matplotlib for visualizations (plotting trading strategies). We will use a basic moving average crossover strategy for demonstration.

Before writing the code, make sure that you have installed necessary libraries by running:
```
pip install pandas numpy matplotlib yfinance
```
Then, here is the basic script:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

def calculate_sma(data, window):
    return data.rolling(window).mean()

def calculate_ema(data, window):
    return data.ewm(span=window, adjust=False).mean()

def trading_strategy(data, short_window, long_window):
    sma = calculate_sma(data, short_window)
    ema = calculate_ema(data, long_window)
    
    buying_signals = data[(sma > ema)]
    selling_signals = data[(sma < ema)]
    
    return buying_signals, selling_signals

ticker_symbol = 'AAPL' # use Apple stock as an example
df = yf.download(ticker_symbol, start="2020-01-01", end="2022-12-31")  
df = df['Close']  # we will use the closing price for our trading strategy

# Define our moving windows
short_window = 50
long_window = 200

# Apply the trading strategy
buying_signals, selling_signals = trading_strategy(df, short_window, long_window)

# Visualize data and strategies
plt.figure(figsize=(12,5))
plt.grid(True)
plt.plot(df.index, df.values, label='AAPL')
plt.plot(buying_signals.index, buying_signals.values, color='g', label='Buy')
plt.plot(selling_signals.index, selling_signals.values, color='r', label='Sell')
plt.legend(loc=0)
plt.title('Apple Stock Price 2020-2022')
plt.xlabel('Dates')
plt.ylabel('Price ($)')
plt.show()
```
This script will download Apple's stock data from 2020 to 2022, apply a simple moving average crossover strategy to identify buying and selling opportunities, and plot the stock price, and signals.

Please note that trading in biller markets requires a thorough understanding of the markets and involves substantial financial risks. The provided script illustrates a fundamental trading strategy and should not constitute a recommendation for trading decisions. For an accurate strategy, consider incorporating other factors like trading volume, market volatility index, economic indicators, and more.