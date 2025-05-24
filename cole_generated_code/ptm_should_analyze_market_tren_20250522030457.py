To analyze market trends and opportunities for potential trades, we need to use some sort of data analysis. Python has a library called pandas which is great for this kind of task. Also, we can use yfinance to download the stock market data.

Here is a basic example of how you can do this:

```python
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Define the ticker symbol
tickerSymbol = 'AAPL'

# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2020-1-25')

# Plot the close price of the stock
tickerDf['Close'].plot(title="Stock's closing price")
plt.show()

# Calculate the moving average
tickerDf['MA_50'] = tickerDf['Close'].rolling(50).mean()
tickerDf['MA_200'] = tickerDf['Close'].rolling(200).mean()

# Plot the moving average along with close price
tickerDf[['Close', 'MA_50', 'MA_200']].plot(title="Stock's closing price with MA")
plt.show()

# Check for trading opportunities
# If MA_50 > MA_200 then it's a good time to buy
# If MA_50 < MA_200 then it's a good time to sell
trading_signals = tickerDf['MA_50'] > tickerDf['MA_200']
print("Trading Opportunities")
print(trading_signals)
```

This script will download the historical data for the Apple stock, calculate the moving average for the last 50 and 200 days, and then plot this data. It also checks for trading opportunities based on the moving averages.

Please note that this is a very basic example and real-world trading involves much more complex analysis. Also, this script assumes that you have the yfinance and pandas libraries installed. If not, you can install them using pip:

```bash
pip install yfinance pandas matplotlib
```

Also, please replace 'AAPL' with the ticker symbol of the stock you want to analyze.