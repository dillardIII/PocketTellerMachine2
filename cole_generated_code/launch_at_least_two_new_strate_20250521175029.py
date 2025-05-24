As an AI text-based model, I don't have the ability to create real-world trading strategies for a live system as these require a thorough understanding of the trading system mechanics, coding structures, and financial theory. Detailed specific code will highly depend on the actual APIs, libraries, and trading strategies Cole's trading system incorporates. 

However, I can provide the generalized conceptual Python code snippets for two simple trading strategies, assuming that PTM is a trading engine object:

1. Moving Average Crossover Strategy: This approach involves two Moving Averages, typically a short-term and long-term moving avg. A "Buy Signal" is triggered when the short-term average crosses above the long-term, and a "Sell Signal" when the short-term crosses below the long-term.

2. Bollinger Bands Strategy: This strategy involves a simple moving average(SMA) along with two standard deviation lines, each above and below the SMA. It typically triggers a Buy Signal when the price falls at or below the lower band and a Sell Signal when the price touches or crosses the upper band.

Snippet for Moving Average Crossover Strategy:

```python
class MovingAverageStrategy:
    def __init__(self, short_window, long_window):
        self.short_window = short_window
        self.long_window = long_window

    def generate_signals(self, df):
        signals = pd.DataFrame(index=df.index)
        signals['signal'] = 0.0

        # Short moving average
        signals['short_mavg'] = df['Close'].rolling(window=self.short_window, min_periods=1).mean()

        # Long moving average
        signals['long_mavg'] = df['Close'].rolling(window=self.long_window, min_periods=1).mean()

        # Create signals
        signals['signal'][self.short_window:] = np.where(
            signals['short_mavg'][self.short_window:] > signals['long_mavg'][self.short_window:], 1.0, 0.0)
        
        signals['positions'] = signals['signal'].diff()
        return signals

ma_strategy = MovingAverageStrategy(short_window=50, long_window=200)
ptm.launch_strategy(ma_strategy)

```

Snippet for Bollinger Bands Strategy:

```python
class BollingerBandsStrategy:
    def __init__(self, window, num_std):
        self.window = window
        self.num_std = num_std

    def generate_signals(self,df):
        rolling_mean = df['Close'].rolling(window=self.window).mean()
        rolling_std = df['Close'].rolling(window=self.window).std()

        df['Bollinger High'] = rolling_mean + (rolling_std * self.num_std)
        df['Bollinger Low'] = rolling_mean - (rolling_std * self.num_std)
        
        df['Short'] = None
        df['Long'] = None
        df['Position'] = None

        for row in range(len(df)):
    
            if (df['Close'].iloc[row] > df['Bollinger High'].iloc[row]) and (df['Close'].iloc[row-1] < df['Bollinger High'].iloc[row-1]):
                df['Position'].iloc[row] = -1
            
            if (df['Close'].iloc[row] < df['Bollinger Low'].iloc[row]) and (df['Close'].iloc[row-1] > df['Bollinger Low'].iloc[row-1]):
                df['Position'].iloc[row] = 1
                
        df['Position'].fillna(method='ffill',inplace=True)

        df['Market Return'] = np.log(df['Close'] / df['Close'].shift(1))
        df['Strategy Return'] = df['Market Return'] * df['Position']

        df['Strategy Return'].cumsum().plot()
        
        return df

bb_strategy = BollingerBandsStrategy(window=20, num_std=2)
ptm.launch_strategy(bb_strategy)
```

Please consider this code as a general reference and you would need to modify or enhance them based on the actual development environment, APIs, and data structure, and of course, the risk and desired artificial intelligence to cover trading needs.

Also, note that for both strategies, we used the 'Close' price. This can vary based on the preferred input for the strategy (such as open, high, low, close, adjusted close, volume, etc.). Furthermore, these strategies don't incorporate transaction cost, slippage, risk management, and this is crucial for real trading.