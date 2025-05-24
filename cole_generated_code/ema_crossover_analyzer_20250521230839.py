Sure, here's a simple Python script to calculate Exponential Moving Average (EMA) and analyze its crossover. This script uses the `pandas` library to calculate EMA and `matplotlib` to plot the data.

```python
import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as web

# Fetching the data
def fetch_data(stock, start, end):
    df = web.DataReader(stock, 'yahoo', start, end)
    return df

# Calculating EMA
def calculate_ema(data, window):
    return data.ewm(span=window, adjust=False).mean()

# Plotting the data
def plot_data(data, ema_short, ema_long):
    plt.figure(figsize=(10,5))
    plt.plot(data.index, data['Close'], label='Close Price', color='blue')
    plt.plot(data.index, ema_short, label='Short EMA', color='red')
    plt.plot(data.index, ema_long, label='Long EMA', color='green')
    plt.title('EMA Crossover')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.legend(loc='upper left')
    plt.show()

# Main function
def main():
    # Define stock, start and end date
    stock = 'AAPL'
    start_date = '01-01-2020'
    end_date = '01-01-2022'

    # Fetch the data
    df = fetch_data(stock, start_date, end_date)

    # Calculate short and long EMA
    short_ema = calculate_ema(df['Close'], 20)
    long_ema = calculate_ema(df['Close'], 100)

    # Plot the data
    plot_data(df, short_ema, long_ema)

if __name__ == "__main__":
    main()
```

This script fetches the stock data, calculates the short-term and long-term EMA, and then plots the close price, short-term EMA, and long-term EMA on a graph. The EMA crossover points on the graph can be used to analyze potential buy/sell signals. The short EMA crossing above the long EMA may be considered a buy signal, while the short EMA crossing below the long EMA may be considered a sell signal.

Please note that you need to install `pandas_datareader` and `matplotlib` libraries to run this script. You can install them using pip:

```
pip install pandas_datareader matplotlib
```