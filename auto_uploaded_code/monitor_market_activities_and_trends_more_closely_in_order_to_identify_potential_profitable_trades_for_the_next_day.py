Here's a simple implementation of your request using Python and the yfinance library, which enables us to fetch market data for different stocks:

```python
import yfinance as yf
import pandas as pd
from pandas_datareader import data as pdr
from datetime import date, timedelta

yf.pdr_override()

class MonitorMarket:
   def __init__(self, tickers, start_date, end_date):
       self.tickers = tickers
       self.start_date = start_date
       self.end_date = end_date

   def get_data(self):
       data = pdr.get_data_yahoo(self.tickers, self.start_date, self.end_date)
       return data

   def calculate_potential_profit(self):
       data = self.get_data()
       data['Potential Profit'] = data['Adj Close'].pct_change() * 100
       return data
      
today = date.today()
start_date = today - timedelta(days=365)
end_date = today

# Add the tickers of the stocks you want to monitor
tickers = ["AAPL", "GOOGL", "AMZN"]

monitor = MonitorMarket(tickers, start_date, end_date)

potential_profits = monitor.calculate_potential_profit()

print(potential_profits)
```

First, this code gets the data for the specific tickers from `start_date` to `end_date`. Then, it calculates the percentage change in the closing price which can be seen as potential profit if one would have bought the stock the day before.

Please note that a profitable trade not only depends on the previous day's price change of a stock. Many other factors, such as company news and overall market trends, need to be considered and ideally be backed by some form of technical analysis. The code above is a very simple approach, and doesn't guarantee profitability. Consider hiring a financial advisor for concrete investing strategies tailored to your specific financial situation.