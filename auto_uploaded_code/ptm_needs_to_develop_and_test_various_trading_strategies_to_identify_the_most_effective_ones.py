Sure, I can provide a simple Python code for a basic trading strategy. In this example, we will use a simple moving average crossover strategy. 

Please note, for real-world trading, you would need to consider many more factors and this code is highly simplified for illustrative purposes. 

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as web

# Define the instruments to download. We would like to see Apple, Microsoft and others.
companies_dict = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Amazon': 'AMZN',
    'Google': 'GOOG',
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

This script will print out a DataFrame that shows whether a trading signal is present for a particular day, based on the moving average crossover strategy. A "1.0" means that the short-term average is above the long-term average, which is a signal to buy, and a "-1.0" means the short-term average is below the long-term average, which is a signal to sell. 

Please replace 'AAPL', 'MSFT', 'AMZN', 'GOOG' with the actual stock symbols you are interested in. 

Also, you need to install pandas_datareader library if not already installed. You can do it by running !pip install pandas_datareader in your jupyter notebook or pip install pandas_datareader in your terminal. 

Please note this is a very basic strategy and in real trading scenario you would need to consider transaction costs, risk management, portfolio diversification etc.