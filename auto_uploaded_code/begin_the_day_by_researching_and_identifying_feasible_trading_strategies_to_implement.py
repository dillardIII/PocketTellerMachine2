Unfortunately, it's not possible to write Python script to research and identify feasible trading strategies because research requires qualitative analysis, reading financial news, watching market trends, understanding geopolitical events - all of which cannot be automated through Python code.

However, python can be used to scrape financial data, to analyze historical data and to backtest certain quantitive trading strategies. Here is an example of how python can be used to backtest a simple moving average trading strategy using Yahoo financial data.

```python
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Download historical data for required stocks
tickersymbol = 'AAPL'
tickerdata = yf.Ticker(tickersymbol)
ticker_df = tickerdata.history(period='1d', start='2010-1-1', end='2020-12-31')

ticker_df['MA50'] = ticker_df['Close'].rolling(50).mean()
ticker_df['MA200'] = ticker_df['Close'].rolling(200).mean()

#Create Buy and Sell signals
ticker_df['Buy_Signal'] = (ticker_df['MA50'] > ticker_df['MA200']) & (ticker_df['MA50'].shift(1) < ticker_df['MA200'].shift(1))
ticker_df['Sell_Signal'] = (ticker_df['MA50'] < ticker_df['MA200']) & (ticker_df['MA50'].shift(1) > ticker_df['MA200'].shift(1))

#plot data and signals  
plt.figure(figsize=(12,5))
plt.plot(ticker_df['Close'], label='Close Price', color='blue')
plt.plot(ticker_df['MA50'], label='Moving Average 50 Days', color='red')
plt.plot(ticker_df['MA200'], label='Moving Average 200 Days', color='green')
plt.scatter(ticker_df.index, ticker_df[ticker_df['Buy_Signal']].Close, color='green', marker='^', alpha=1)
plt.scatter(ticker_df.index, ticker_df[ticker_df['Sell_Signal']].Close, color='red', marker='v', alpha=1)
plt.title('Apple - Moving Average Crossover')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Price in $', fontsize=12)
plt.legend(loc='upper left')
plt.grid()
plt.show()
```

In this script:

- Firstly, prices are fetched from Yahoo finance.
- Then 50 and 200 days moving averages are computed.
- Then buy signal is created when 50 day moving average crosses 200 day moving average from below and sell signal is created when 50 day moving average crosses 200 day moving average from above.
- Finally, prices, moving averages and signals are plotted.