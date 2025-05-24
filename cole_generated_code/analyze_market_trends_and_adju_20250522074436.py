Analyzing market trends and adjusting trading parameters to optimize potential for successful trades is a complex task that involves machine learning and data analysis. Here is a simple example of how you might approach this task using Python, pandas for data manipulation, and sklearn for machine learning.

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load market data
data = pd.read_csv('market_data.csv')

# Assume the data has columns 'Open', 'High', 'Low', 'Close', 'Volume'
# Create a new column 'Average' as the average of 'High' and 'Low'
data['Average'] = data[['High', 'Low']].mean(axis=1)

# Use 'Open', 'High', 'Low', 'Volume', 'Average' to predict 'Close'
X = data[['Open', 'High', 'Low', 'Volume', 'Average']]
y = data['Close']

# Split the data into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict the 'Close' prices for the test set
y_pred = model.predict(X_test)

# Calculate the mean squared error of the predictions
mse = mean_squared_error(y_test, y_pred)

print(f'Mean Squared Error: {mse}')

# If the error is too high, adjust trading parameters
if mse > threshold:
    # Adjust trading parameters here
    pass
```

This is a very basic example. In a real-world scenario, you would likely use more sophisticated models and techniques, and you would need to consider many more factors, such as market volatility, the time of day, the specific assets you're trading, and so on. You would also need to continually retrain your model as new data becomes available.