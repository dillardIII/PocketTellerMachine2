Here's a simple Python code that uses pandas library to analyze market trends. This code reads market data from a CSV file, calculates moving averages, and adjusts trading parameters based on the trend.

```python
import pandas as pd
import numpy as np

class TradingParameters:
    def __init__(self, buy_threshold, sell_threshold):
        self.buy_threshold = buy_threshold
        self.sell_threshold = sell_threshold

def analyze_market_trends(data):
    # Calculate moving averages
    data['MA10'] = data['Price'].rolling(window=10).mean()
    data['MA50'] = data['Price'].rolling(window=50).mean()

    # Identify buy and sell signals
    data['Buy_Signal'] = np.where(data['MA10'] > data['MA50'], 1, 0)
    data['Sell_Signal'] = np.where(data['MA10'] < data['MA50'], 1, 0)

    # Calculate buy and sell thresholds
    buy_threshold = data['Buy_Signal'].sum() / len(data)
    sell_threshold = data['Sell_Signal'].sum() / len(data)

    return TradingParameters(buy_threshold, sell_threshold)

def adjust_trading_parameters(data_file):
    # Read market data from CSV file
    data = pd.read_csv(data_file)

    # Analyze market trends
    trading_parameters = analyze_market_trends(data)

    return trading_parameters

# Adjust trading parameters based on market data in 'market_data.csv'
trading_parameters = adjust_trading_parameters('market_data.csv')

print(f'Buy threshold: {trading_parameters.buy_threshold}')
print(f'Sell threshold: {trading_parameters.sell_threshold}')
```

Please replace 'market_data.csv' with your actual CSV file that contains market data. This script assumes that the CSV file has a column named 'Price' which represents the price of a stock or a commodity.

The moving averages (MA10 and MA50) are calculated for 10 and 50 periods respectively. A buy signal is generated when MA10 is greater than MA50, and a sell signal is generated when MA10 is less than MA50. The buy and sell thresholds are calculated as the ratio of the number of buy and sell signals to the total number of data points.

The `adjust_trading_parameters` function reads market data, analyzes market trends, and returns trading parameters (buy and sell thresholds). These thresholds can be used to initiate trades.