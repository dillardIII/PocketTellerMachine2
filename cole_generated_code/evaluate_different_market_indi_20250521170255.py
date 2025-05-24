Here's a simple Python code using Pandas library to analyze the trading data and predict some investment opportunities based on market indicators:

```python
import pandas as pd
from pandas_datareader import data

# Market Indicators
stocks = ['AAPL', 'MSFT', 'GOOG', 'IBM']

# Define which online source to use
data_source = 'yahoo'

# Define the start and end dates that we want to see
start_date = '2015-01-01'
end_date = '2020-12-31'

# Use pandas_reader.data.DataReader to load the desired data.
panel_data = data.DataReader(stocks, data_source, start_date, end_date)

# Calculate daily stock movement
stock_close = panel_data['Close']
stock_open = panel_data['Open']
 
stock_close = np.array(stock_close).T
stock_open = np.array(stock_open).T
 
row, col = stock_close.shape
 
movements = np.zeros([row, col])
 
for i in range(0, row):
    movements[i, :] = np.subtract(stock_close[i, :], stock_open[i, :])


# Identify potential investment based on movements
for company, movement in zip(stocks, movements):
    if np.sum(movement) > 0:
        print(f"{company} shows a positive movement, indicating a potential investment opportunity.")
    else:
        print(f"{company} does not show substantial activity at this time.")

```

Note: For a real-world application, you would use more robust indicators and models such as machine learning algorithms, technical indicators (RSI, MACD, Moving Average, etc), and financial statement analysis to evaluate investment opportunities and market conditions. This sample code provides a very basic form of analysis purely for educational purposes. Always consult with a financial advisor before making investment decisions.