Creating a Python program to analyze market trends and opportunities for potential profitable trades is a complex task. It requires knowledge of financial markets, machine learning, and data analysis. Here's a simplified example of how you might start building such a program using Python's pandas and yfinance libraries to fetch and analyze stock data.

```python
import pandas as pd
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression

def analyze_stock(symbol):
    # Download historical data as dataframe
    data = yf.download(symbol, start='2020-01-01', end='2022-12-31')

    # Prepare data for trend analysis
    data['Date'] = data.index
    data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d')
    data['Date'] = data['Date'].map(dt.datetime.toordinal)

    # Use last 30 days data for training
    data_train = data[-30:]

    x_train = data_train.drop(['Close', 'Date'], axis=1)
    y_train = data_train['Close']

    # Normalize data
    scaler = MinMaxScaler(feature_range=(0, 1))
    x_train_scaled = scaler.fit_transform(x_train)

    # Train linear regression model
    model = LinearRegression()
    model.fit(x_train_scaled, y_train)

    # Predict trend for the next day
    x_test = data.tail(1).drop(['Close', 'Date'], axis=1)
    x_test_scaled = scaler.transform(x_test)
    prediction = model.predict(x_test_scaled)

    print(f"Predicted closing price for {symbol} on next trading day is {prediction[0]}")

# Analyze Apple stock
analyze_stock('AAPL')
```

This code downloads historical data for a given stock symbol, trains a linear regression model on the last 30 days of data, and predicts the closing price for the next trading day.

Please note that this is a very simplified example. Real-world trading algorithms use much more complex models, take into account a lot more factors, and require a deep understanding of financial markets. Also, this code does not take into account transaction costs, tax implications, and other factors that could affect profitability. It's also important to remember that past performance is not indicative of future results.