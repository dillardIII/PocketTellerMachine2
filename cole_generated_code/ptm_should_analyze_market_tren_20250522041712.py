To analyze market trends and identify potential trading opportunities, we can use Python's libraries like pandas for data manipulation, matplotlib for data visualization, and yfinance to download the historical market data from Yahoo finance.

Here is a simple example of how you can do this:

```python
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Download historical data as dataframe
data = yf.download('AAPL', start='2020-01-01', end='2022-12-31')

# Calculate moving averages
data['SMA_50'] = data['Close'].rolling(window=50).mean()
data['SMA_200'] = data['Close'].rolling(window=200).mean()

# Plot closing price, short-term and long-term moving averages 
data[['Close', 'SMA_50', 'SMA_200']].plot(figsize=(10,5))
plt.grid(True)
plt.title('AAPL Close Prices with SMA 50 & 200')
plt.axis('tight')
plt.ylabel('Price')

plt.show()

# Create a column 'Signal' such that if SMA_50 > SMA_200 then buy else sell
data['Signal'] = 0.0  
data['Signal'][49:] = np.where(data['SMA_50'][49:] > data['SMA_200'][49:], 1.0, 0.0)

# Generate trading orders
data['Position'] = data['Signal'].diff()

# Print data
print(data)
```

This script will download the historical data for Apple Inc. (AAPL) from Yahoo finance, calculate the 50-day and 200-day moving averages, and plot them along with the closing prices. It will then generate a trading signal based on the crossover of these moving averages (a common trading strategy), and generate trading orders based on these signals.

Please note that this is a very basic form of market trend analysis and trading signal generation. In practice, market trend analysis can get very complex and may involve the use of advanced statistical methods and machine learning models.