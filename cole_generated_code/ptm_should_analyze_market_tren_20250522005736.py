To analyze market trends and data, we need to use some libraries such as pandas for data manipulation, matplotlib for data visualization, and yfinance to download the stock data. Here's a simple example of how you might start building a Python Trading Model (PTM).

Please note that this is a very basic example and real trading models involve much more complex algorithms and data analysis.

```python
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Download historical data as dataframe
data = yf.download('AAPL','2019-01-01','2022-12-31')

# Calculate simple moving average
data['SMA'] = data['Close'].rolling(window=20).mean()

# Calculate standard deviation
data['STD'] = data['Close'].rolling(window=20).std()

# Calculate upper Bollinger Band
data['Upper'] = data['SMA'] + (data['STD'] * 2)

# Calculate lower Bollinger Band
data['Lower'] = data['SMA'] - (data['STD'] * 2)

# Plot close price, moving average and Bollinger Bands
data[['Close','SMA','Upper','Lower']].plot(figsize=(10,4))
plt.grid(True)
plt.title('Bollinger Bands')
plt.axis('tight')
plt.ylabel('Price')
plt.show()
```

This script downloads the historical price data for Apple Inc. (AAPL) from 2019 to 2022. It then calculates the simple moving average and standard deviation for the closing prices over a rolling window of 20 days. The upper and lower Bollinger Bands are calculated as two standard deviations above and below the moving average, respectively. Finally, it plots the closing prices, moving average, and Bollinger Bands.

Potential trading opportunities might be identified when the price crosses above or below these bands. However, this is a very simplistic approach and should not be used for actual trading without further refinement and testing.