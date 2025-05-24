Sure, I can provide a simple example of analyzing market trends using Python. I'll be using the pandas library for the data manipulation and matplotlib for data visualization. We are going to use daily Bitcoin data from the Yahoo Finance.

```python
import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import yfinance as yf

yf.pdr_override() 

# Download historical data as dataframe
df = pdr.get_data_yahoo("BTC-USD", start="2020-01-01", end="2020-12-31")

# Calculate moving averages
df['SMA_20'] = df['Close'].rolling(window=20, min_periods=1).mean()
df['SMA_50'] = df['Close'].rolling(window=50, min_periods=1).mean()

# Visualization
plt.figure(figsize=[15,10])
plt.grid(True)
plt.plot(df['Close'],label='BTC', linewidth=2, color='blue')
plt.plot(df['SMA_20'],label='SMA 20 days', linewidth=2, color='red')
plt.plot(df['SMA_50'],label='SMA 50 days', linewidth=2, color='green')
plt.legend(loc=2)
plt.show()

```

In this script:
1. We download the historical data of Bitcoin (BTC) from `2020-01-01` to `2020-12-31`.
2. We calculate 20-day and 50-day simple moving averages (SMA) for the closing prices.
3. We plot the closing prices and the SMAs.

Remember that this is a simplified example. Real-world trading systems use more complex indicators, algorithms, and control risk and money management systems. Plus, building a bot for live trading with real money requires a more sophisticated setup, and is subject to financial regulations. 

For more advanced techniques, you might want to learn about machine learning models for price prediction, algorithmic trading, and other relevant topics.

Also, make sure to use your own yahoo finance data API key in the code to fetch the data.