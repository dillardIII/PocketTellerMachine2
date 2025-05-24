Predicting future market trends and movements is a complex task that involves machine learning and data analysis. Here is a simple example of how you can use Python to analyze historical stock price data and make predictions using a linear regression model. We'll use the pandas library to handle our data and the sklearn library to create the regression model.

Please note that this is a very basic model and real-world trading algorithms are much more complex and take many more factors into account.

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Load the data
df = pd.read_csv('stock_data.csv')  # replace with your csv file

# Check the data
print(df.head())

# We'll use the 'High' price to predict the 'Close' price
X = df['High'].values.reshape(-1,1)
y = df['Close'].values.reshape(-1,1)

# Split the data into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Create a linear regression model and fit it to the training data
regressor = LinearRegression()  
regressor.fit(X_train, y_train)

# Use the model to make predictions
y_pred = regressor.predict(X_test)

# Compare the actual 'Close' prices to the predicted 'Close' prices
df = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})
print(df)
```

This code will load a CSV file containing stock data, use the 'High' price to predict the 'Close' price, split the data into a training set and a test set, create a linear regression model, fit the model to the training data, use the model to make predictions on the test data, and then compare the actual 'Close' prices to the predicted 'Close' prices.

Please note that this is a very simple model and is unlikely to be accurate for real-world trading. In reality, stock prices are influenced by a huge number of factors and it's unlikely that the 'High' price alone would be a good predictor of the 'Close' price.