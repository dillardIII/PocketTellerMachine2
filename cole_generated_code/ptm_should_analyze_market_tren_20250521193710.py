To complete this task, we would need to use a Python library like `pandas` for data manipulation and analysis, and `yfinance` to download the stock market data. Here's a simple example of how you might use Python to analyze market trends:

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
tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2020-12-31')

# See your data
print(tickerDf)

# Plot the close prices
plt.figure(figsize=(10,6))
plt.plot(tickerDf.Close)
plt.title('Historical stock price of ' + tickerSymbol)
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.show()
```

This script will download the historical price data for Apple Inc. ('AAPL') from 2010 to 2020, and then plot the closing price over this period. 

Please note that this is a very basic example. In a real-world scenario, you would likely need to perform much more complex analysis, possibly involving machine learning or other advanced techniques, to accurately predict market trends and identify trading opportunities.

Also, please note that this script requires the `yfinance`, `pandas` and `matplotlib` Python libraries. If you don't have these installed, you can do so using pip:

```bash
pip install yfinance pandas matplotlib
```