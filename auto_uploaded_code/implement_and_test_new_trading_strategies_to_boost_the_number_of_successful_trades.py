Implementing and testing new trading strategies involve financial data analysis and machine learning models for prediction of market trends. Below is an example of a simple moving average crossover strategy, implemented with help of the pandas data analysis library and data available in csv format. 

Before running the Python script, ensure that you have installed necessary Python packages like pandas and matplotlib.

Installation commands:
``` bash
pip install pandas
pip install matplotlib
```

Below is a Python script implementing moving average crossover strategy. 

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file (example with 'AAPL.csv')
data = pd.read_csv('AAPL.csv', index_col='Date', parse_dates=True)

# Calculate short-term and long-term moving averages
data['Short_MA'] = data['Close'].rolling(window=20).mean()
data['Long_MA'] = data['Close'].rolling(window=100).mean()

# Create signals based on crossover
data['Signal'] = 0.0
data['Signal'][data['Short_MA'] > data['Long_MA']] = 1.0
data['Signal'][data['Short_MA'] < data['Long_MA']] = -1.0

# Calculate daily returns
data['Return'] = data['Close'].pct_change() * data['Signal'].shift()

# Calculate cumulative returns
data['Cumulative Return'] = (1 + data['Return']).cumprod()

# Plot the cumulative returns
plt.figure(figsize=(10, 5))
plt.plot(data['Cumulative Return'], label='Moving Average Strategy')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.legend()
plt.show()
```

This script performs the moving average crossover strategy for Apple Inc.'s stock (AAPL). It first calculates the short-term (20 days) and long-term (100 days) moving averages, then generates trading signals based on the crossover of these averages. The script also computes daily and cumulative returns, and then plots the cumulative returns. 

The testing of this strategy is done via paper trading, i.e., the strategy is tested on historical data and its effectiveness is measured based on the cumulative returns it could have generated.

Please note that this simple strategy may not necessarily boost the number of successful trades. For more advanced strategies, one could use machine learning models to predict future asset prices and construct more sophisticated trading signals.

Additionally, the example mentioned here requires a CSV file with historical price data of the stock. Replace "AAPL.csv" with the actual path to this file before running the script.