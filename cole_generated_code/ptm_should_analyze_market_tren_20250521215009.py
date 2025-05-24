Creating a Python script to analyze market trends and patterns is a complex task and requires a deep understanding of both financial markets and machine learning. Here is a simple example of how you can start analyzing market trends using Python. In this example, we will use the pandas library to handle our data and the yfinance library to get the stock data. We will analyze the closing price of a stock.

```python
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Download historical data as dataframe
data = yf.download('AAPL','2020-01-01','2022-12-31')

# Use only Close price for prediction
data = data[['Close']]

# Predict for the next 'n' days
forecast_out = 30

# Create another column (the target) shifted 'n' units up
data['Prediction'] = data[['Close']].shift(-forecast_out)

# Create the independent data set (X)
X = data.drop(['Prediction'], 1)[:-forecast_out]

# Create the dependent data set (y)
y = data['Prediction'][:-forecast_out]

# Split the data into 80% training and 20% testing
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create and train the Linear Regression Model
lr = LinearRegression()
lr.fit(x_train, y_train)

# Test the model using score
lr_confidence = lr.score(x_test, y_test)
print("lr confidence: ", lr_confidence)

# Set x_forecast equal to the last 30 rows of the original data set from Close column
x_forecast = data.drop(['Prediction'], 1)[:-forecast_out]
x_forecast = x_forecast.tail(forecast_out)

# Print linear regression model predictions for the next 'n' days
lr_prediction = lr.predict(x_forecast)
print(lr_prediction)
```

This script will print the predicted closing prices for the next 30 days. Please note that this is a very basic model and might not give very accurate results. For more accurate results, more complex models and additional factors should be considered. Also, the model does not take into account possible wins and losses, it only predicts the closing prices. 

Please install the necessary libraries by using pip:
```
pip install pandas yfinance sklearn matplotlib
```