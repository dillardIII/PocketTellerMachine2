from ghost_env import INFURA_KEY, VAULT_ADDRESS
To develop and implement new trading strategies, we first need to have some data to work with. For that, we can use the pandas_datareader library to fetch some stock data. Then we can implement a simple moving average crossover strategy as an example.

Here is a simple Python code for that:

```python
import pandas as pd
import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt

# Define the instruments to download. We would like to see Apple, Microsoft and others.
companies_dict = {
    'Amazon': 'AMZN',
    'Apple': 'AAPL',
    'Walgreen': 'WBA',
    'Northrop Grumman': 'NOC',
    'Boeing': 'BA',
    'Lockheed Martin':'LMT',
    'McDonalds': 'MCD',
    'Intel': 'INTC',
    'Navistar': 'NAV',
    'IBM': 'IBM',
    'Texas Instruments': 'TXN',
    'MasterCard': 'MA',
    'Microsoft': 'MSFT',
    'General Electrics': 'GE',
    'American Express': 'AXP',
    'Pepsi': 'PEP',
    'Coca Cola': 'KO',
    'Johnson & Johnson': 'JNJ'
}

companies = sorted(companies_dict.items(), key=lambda x: x[1])

# Define which online source to use
data_source = 'yahoo'

# Define the start and end dates
start_date = '2015-01-01'
end_date = '2020-12-31'

# Use pandas_datareader.data.DataReader to load the desired data
panel_data = web.DataReader(list(companies_dict.values()), data_source, start_date, end_date)

# Calculate the short and long window simple moving averages
short_window = 40
long_window = 100

signals = pd.DataFrame(index=panel_data.index)
signals['signal'] = 0.0

# Create a short simple moving average over the short window
signals['short_mavg'] = panel_data['Close'].rolling(window=short_window, min_periods=1, center=False).mean()

# Create long simple moving average over the long window
signals['long_mavg'] = panel_data['Close'].rolling(window=long_window, min_periods=1, center=False).mean()

# Create signals
signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] 
                                            > signals['long_mavg'][short_window:], 1.0, 0.0)   

# Generate trading orders
signals['positions'] = signals['signal'].diff()

# Print `signals`
print(signals)
```

This is a simple moving average crossover strategy, it's not recommended to use it for actual trading. For real trading, you would need to consider transaction costs, slippage, risk management, etc. Also, you would need to use more sophisticated strategies, possibly incorporating machine learning and other techniques.