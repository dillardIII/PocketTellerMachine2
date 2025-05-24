Sure, below is a simple Python code using `pandas_datareader` to fetch stock data from Yahoo Finance and analyze it for potential trading opportunities. For simplicity, we're using a simple moving average (SMA) strategy. If the short-term SMA (10 days) crosses above the long-term SMA (50 days), it's a buy signal. If the short-term SMA crosses below the long-term SMA, it's a sell signal.

```python
import pandas as pd
import pandas_datareader.data as web
from datetime import datetime

# Define the instruments to download
tickers = ['AAPL', 'MSFT', 'GOOG']

# Define which online source to use
data_source = 'yahoo'

# Define the start and end dates
start_date = '2010-01-01'
end_date = '2020-12-31'

# Use pandas_datareader.data.DataReader to load the desired data
panel_data = web.DataReader(tickers, data_source, start_date, end_date)

# Calculate short-term and long-term moving averages
short_rolling = panel_data['Close'].rolling(window=10).mean()
long_rolling = panel_data['Close'].rolling(window=50).mean()

# Create signals based on crossover of short and long moving averages
signals = pd.DataFrame(index=panel_data.index)
signals['signal'] = 0.0

for ticker in tickers:
    signals['short_mavg'] = short_rolling[ticker]
    signals['long_mavg'] = long_rolling[ticker]
    signals['signal'][short_rolling[ticker] > long_rolling[ticker]] = 1.0
    print(f"Trading signals for {ticker}:")
    print(signals)
```

Please note that this is a very basic trading strategy and is not recommended for actual trading. Real-world trading involves much more complex analysis and risk management. Also, you need to install `pandas_datareader` package if not already installed. You can install it via pip:

```shell
pip install pandas-datareader
```

Also, please replace `'AAPL', 'MSFT', 'GOOG'` with the actual tickers you're interested in.