Sure, I can provide a simple example of a pair trading strategy using Python. This is a type of statistical arbitrage strategy used by many hedge funds. The idea is to find two stocks that are historically correlated, then go long on the one that is underperforming and short on the one that is overperforming. This strategy assumes that the spread between the two stocks will converge in the future.

Please note that this is a simplified example and real-world trading strategies are much more complex and take into account many more factors.

```python
import numpy as np
import pandas as pd
import yfinance as yf
from sklearn.linear_model import LinearRegression

# Download historical data for required stocks
stock1 = yf.download('AAPL','2016-01-01','2021-12-31')
stock2 = yf.download('MSFT','2016-01-01','2021-12-31')

# We will use 'Close' price for our analysis
stock1 = stock1[['Close']]
stock2 = stock2[['Close']]

# Rename the columns 
stock1.columns = ['AAPL']
stock2.columns = ['MSFT']

# Join the two dataframes
data = stock1.join(stock2, how='inner')

# Calculate the spread between the two stocks
data['spread'] = data['AAPL'] - data['MSFT']

# Define the training data
X = data['AAPL'].values.reshape(-1,1)
y = data['MSFT'].values

# Create and train a linear regression model
model = LinearRegression()
model.fit(X, y)

# Predict the 'MSFT' prices
data['predicted_MSFT'] = model.predict(X)

# Calculate the residuals
data['residuals'] = data['MSFT'] - data['predicted_MSFT']

# If residuals are positive go long on the underperforming stock (MSFT) and short on the overperforming stock (AAPL)
data['longs'] = (data['residuals'] > 0) * 1

# If residuals are negative go short on the underperforming stock (MSFT) and long on the overperforming stock (AAPL)
data['shorts'] = (data['residuals'] < 0) * -1

# The positions are the sum of longs and shorts
data['positions'] = data['longs'] + data['shorts']

print(data)
```

This script downloads historical data for Apple and Microsoft, calculates the spread between the two stocks, and then uses a linear regression model to predict the prices of Microsoft given the prices of Apple. The residuals of this model are then used to determine whether to go long or short on each stock.

Please note that this is a very simplified trading strategy and in a real-world scenario, you would need to consider transaction costs, slippage, risk management, etc. Also, this strategy assumes that the relationship between the two stocks will remain stable, which might not be the case.