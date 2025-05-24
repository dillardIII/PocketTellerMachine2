Analyzing market trends and patterns is a complex task that involves a lot of data processing and machine learning. Here is a simple example of how you could use Python to analyze stock prices. In this example, we will use the pandas library to handle data, yfinance to download stock price data, and matplotlib to visualize the data.

```python
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Download historical data for desired ticker symbol 
tickerSymbol = 'AAPL'
tickerData = yf.Ticker(tickerSymbol)
df = tickerData.history(period='1d', start='2010-1-1', end='2020-12-31')

# Use only Close price for prediction
df = df[['Close']]

# Predict for the next 'n' days
forecast_out = 30

# Create another column (the target) shifted 'n' units up
df['Prediction'] = df[['Close']].shift(-forecast_out)

# Create the independent data set (X)
X = df.drop(['Prediction'], 1)[:-forecast_out]

# Create the dependent data set (y)
y = df['Prediction'][:-forecast_out]

# Split the data into 80% training and 20% testing
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create and train the Linear Regression Model
lr = LinearRegression()
lr.fit(x_train, y_train)

# Test the model using score
lr_confidence = lr.score(x_test, y_test)
print("lr confidence: ", lr_confidence)

# Set x_forecast equal to the last 'n' rows of the original data set from Close column
x_forecast = df.drop(['Prediction'], 1)[:-forecast_out]
x_forecast = x_forecast.tail(forecast_out)

# Print linear regression model predictions for the next 'n' days
lr_prediction = lr.predict(x_forecast)
print(lr_prediction)
```

This script will predict the closing price for the next 30 days based on historical data. Please note that this is a very simplified model and real-world trading models are much more complex and take many more factors into account.