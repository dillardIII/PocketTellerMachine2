To analyze market trends and patterns, we can use libraries like pandas for data manipulation, numpy for numerical operations, matplotlib for plotting graphs, and sklearn for machine learning tasks.

Here is a simple example of how you might start to build a Python Trading Model (PTM). This example uses historical data to calculate simple moving averages, which are often used to identify market trends.

Please note that this is a very basic example and real-world trading models are much more complex and involve many more factors.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Load historical market data
df = pd.read_csv('market_data.csv')

# Calculate simple moving average
df['SMA'] = df['Price'].rolling(window=14).mean()

# Plot price and simple moving average
plt.figure(figsize=(12,6))
plt.plot(df['Price'], label='Price')
plt.plot(df['SMA'], label='Simple Moving Average')
plt.legend(loc='upper left')
plt.show()

# Prepare data for machine learning model
df = df.dropna()
X = df['SMA'].values.reshape(-1,1)
y = df['Price'].values.reshape(-1,1)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
```

This code is a starting point and can be expanded to include other indicators, use different machine learning models, and analyze different types of market data. It's also important to note that trading involves significant risk and this code should not be used for real trading without further development and testing.