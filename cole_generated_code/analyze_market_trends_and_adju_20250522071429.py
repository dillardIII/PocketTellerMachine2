Analyzing market trends and adjusting trading parameters is a complex task that involves machine learning and data analysis. Here is a simplified example of how you might approach this task using Python. This code uses the pandas library to analyze data and the sklearn library to create a simple linear regression model.

```python
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Assuming you have market data in a CSV file
df = pd.read_csv('market_data.csv')

# Let's assume 'Close' is the target variable we want to predict
# And 'Open', 'High', 'Low' are the features we will use to predict 'Close'
features = ['Open', 'High', 'Low']
target = 'Close'

X = df[features]
y = df[target]

# Split the data into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Create a linear regression model
regressor = LinearRegression()  

# Train the model using the training sets
regressor.fit(X_train, y_train)

# Make predictions using the testing set
y_pred = regressor.predict(X_test)

# Compare actual output values with predicted values
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(df)

# Evaluate the performance of the algorithm
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
```

This code will give you a basic understanding of how your model is performing. You can adjust your trading parameters based on the predictions made by the model. Please note that this is a very simplified model and actual stock market prediction models are much more complex and take into account many more factors.