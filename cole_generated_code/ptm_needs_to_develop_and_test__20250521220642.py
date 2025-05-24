Sure, here's a simple example of a Python script that uses the pandas library to backtest a simple moving average crossover strategy on historical stock price data.

```python
import pandas as pd
import pandas_datareader as web
import datetime as dt

# Define the trading strategy
def strategy(df, short_window, long_window):
    # Create a 'signal' column and initialize it to 0
    df['signal'] = 0.0

    # Create short simple moving average over the short window
    df['short_mavg'] = df['Close'].rolling(window=short_window, min_periods=1, center=False).mean()

    # Create long simple moving average over the long window
    df['long_mavg'] = df['Close'].rolling(window=long_window, min_periods=1, center=False).mean()

    # Create signals
    df['signal'][short_window:] = np.where(df['short_mavg'][short_window:] 
                                            > df['long_mavg'][short_window:], 1.0, 0.0)   

    # Generate trading orders
    df['positions'] = df['signal'].diff()

# Define the backtesting
def backtest(df):
    # Print the dataframe
    print(df)

    # Create a figure
    fig = plt.figure()

    # Add a subplot and label for y-axis
    ax1 = fig.add_subplot(111,  ylabel='Price in $')

    # Plot the closing price
    df['Close'].plot(ax=ax1, color='r', lw=2.)

    # Plot the short and long moving averages
    df[['short_mavg', 'long_mavg']].plot(ax=ax1, lw=2.)

    # Plot the buy signals
    ax1.plot(df.loc[df.positions == 1.0].index, 
             df.short_mavg[df.positions == 1.0],
             '^', markersize=10, color='m')
    
    # Plot the sell signals
    ax1.plot(df.loc[df.positions == -1.0].index, 
             df.short_mavg[df.positions == -1.0],
             'v', markersize=10, color='k')
    
    # Show the plot
    plt.show()

# Define the main function
def main():
    # Define the stock to be used
    stock = 'AAPL'
    
    # Define the start and end dates
    start_date = dt.datetime(2020,1,1)
    end_date = dt.datetime(2021,12,31)

    # Get the stock data
    df = web.DataReader(stock, 'yahoo', start_date, end_date)

    # Apply the strategy
    strategy(df, 50, 200)

    # Backtest the strategy
    backtest(df)

# Run the main function
if __name__ == "__main__":
    main()
```

This script uses the Yahoo Finance API to download historical stock price data. It then calculates a short and long moving average of the closing prices. When the short moving average crosses above the long moving average, it generates a buy signal, and when it crosses below, it generates a sell signal. These signals are then plotted on a graph for visual inspection.

Please note that this is a very basic trading strategy and is unlikely to be profitable without further refinement. It's also important to remember that past performance is not indicative of future results.