As an AI, I can't review and update trading strategies in real-time as I don't have access to live data. However, I can provide you with a Python code template that you can use to update your trading strategies based on the market conditions. 

This code will use the pandas library to analyze the data and update the strategies accordingly. Please replace 'your_data.csv' with your actual data file and 'your_strategy' with your actual strategy.

```python
import pandas as pd

# Load the trading data
data = pd.read_csv('your_data.csv')

# Review the market conditions
# For example, we can calculate the moving average
data['MA_10'] = data['Price'].rolling(window=10).mean()
data['MA_50'] = data['Price'].rolling(window=50).mean()

# Define a simple trading strategy
def apply_strategy(data):
    buys = []
    sells = []
    flag = -1

    for i in range(len(data)):
        if data['MA_10'][i] > data['MA_50'][i]:
            if flag != 1:
                buys.append(data['Price'][i])
                sells.append(float('nan'))
                flag = 1
            else:
                buys.append(float('nan'))
                sells.append(float('nan'))
        elif data['MA_10'][i] < data['MA_50'][i]:
            if flag != 0:
                sells.append(data['Price'][i])
                buys.append(float('nan'))
                flag = 0
            else:
                buys.append(float('nan'))
                sells.append(float('nan'))
        else:
            buys.append(float('nan'))
            sells.append(float('nan'))

    return buys, sells

# Apply the strategy
data['Buy_Signal_Price'], data['Sell_Signal_Price'] = apply_strategy(data)

# Print the updated data
print(data)
```

This is a simple moving average crossover strategy. When the short-term moving average crosses above the long-term moving average, it generates a buy signal. When the short-term moving average crosses below the long-term moving average, it generates a sell signal.

Please note that this is a very basic strategy and may not be profitable in real trading. You should adjust this strategy according to your trading style, risk tolerance, and the specific market conditions.