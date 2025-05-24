As a language model AI developed by OpenAI, I can generate an example Python code using libraries like pandas, numpy and matplotlib to analyze historical financial data. However, it's important to note that this a significant simplification of what's required. Running an actual trading strategy would need real-time data, rigorous backtesting, and additional measures.

Here's a sample Python code to analyze market data using pandas:

```python
import pandas as pd
import matplotlib.pyplot as plt

# Assuming that data.csv is a file with historical data
data = pd.read_csv('data.csv')

# Calculate a 30 day moving average
data['30 Day MA'] = data['Price'].rolling(window=20).mean()

# Calculate a 100 day moving average
data['100 Day MA'] = data['Price'].rolling(window=100).mean()

# Create a "Buy Signal" column (When the short moving average crosses above the long moving average)
data['Buy Signal'] = np.where(data['30 Day MA'] > data['100 Day MA'], True, False)

# Create a "Sell Signal" column (When the long moving average crosses above the short moving average)
data['Sell Signal'] = np.where(data['100 Day MA'] > data['30 Day MA'], True, False)

# Plotting
plt.figure(figsize=(12,5))
plt.grid(True)
plt.plot(data['Price'],label='Data')
plt.plot(data['30 Day MA'], label='30 Day MA')
plt.plot(data['100 Day MA'], label='100 Day MA')
plt.legend(loc=2)

# Print potential profitable trades
trades = data.loc[data['Buy Signal'] == True]
print("Potential profitable trades: \n", trades)
```

This python script will calculate the 30 day and 100 day moving average of the prices and generate a graph showing these averages. It also generates potential buy signals when the 30 day moving average crosses above the 100 day moving average and sell signals when the 100 day moving average crosses above the 30 day moving average.

The 'data.csv' file is presumed to have a 'Price' column containing prices for the security/asset being analyzed. An actual market analysis platform would include a direct interface with a data provider (such as IEX) to pull in the relevant data, as well as risk management, direct market access, and potentially machine learning algorithms for decision making.