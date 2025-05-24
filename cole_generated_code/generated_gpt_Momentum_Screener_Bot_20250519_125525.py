As an AI assistant, I need more specific details to provide an accurate solution. However, I can give you a basic example of a screener bot using Python. This bot will use the `yfinance` library to download stock data and calculate momentum. Please adjust the code according to your needs.

```python
import yfinance as yf
import pandas as pd

# Define the list of tickers for which we want to screen momentum
tickers_list = ['AAPL', 'GOOG', 'MSFT', 'AMZN']

# Create a dataframe to store the adjusted close price of the stocks
df = pd.DataFrame()

# Fetch the data
for ticker in tickers_list:
    df[ticker] = yf.download(ticker, period='1y')['Adj Close']

# Calculate the 1 year momentum
momentum = df.pct_change(252)

# Screen for stocks with positive momentum
positive_momentum_stocks = momentum[momentum > 0].dropna(how='all')

print(positive_momentum_stocks)
```

This code will print out the stocks from the `tickers_list` that have positive momentum over the past year. You can modify the `tickers_list` and the period over which momentum is calculated to suit your needs.

Please note that this is a very basic momentum screener and does not take into account many factors that you might want to consider when screening for stocks. Also, you need to install `yfinance` library using pip:

```bash
pip install yfinance
```

Please replace the ticker symbols with the ones you are interested in.