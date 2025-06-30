from ghost_env import INFURA_KEY, VAULT_ADDRESS
Below is a standalone Python file (trading_strategy_3.py) that implements a simple trading strategy. This strategy uses a combination of exponential moving averages (EMAs) and the Relative Strength Index (RSI) to generate buy and sell signals.

```python
# trading_strategy_3.py

import pandas as pd

def calculate_ema(prices, period):
    """
    Calculate the Exponential Moving Average (EMA) for a given period.
    """
    return prices.ewm(span=period, adjust=False).mean()

def calculate_rsi(prices, period=14):
    """
    Calculate the Relative Strength Index (RSI) for a given period.
    """
    delta = prices.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def generate_signals(data, short_ema_period=9, long_ema_period=21, rsi_period=14,
                     rsi_overbought=70, rsi_oversold=30):
    """
    Generate buy/sell signals based on EMA crossover and RSI levels.

    Buy Signal:
        - Short-term EMA crosses above long-term EMA
        - RSI is below an oversold threshold (e.g., 30)

    Sell Signal:
        - Short-term EMA crosses below long-term EMA
        - RSI is above an overbought threshold (e.g., 70)
    """
    data = data.copy()
    data['ShortEMA'] = calculate_ema(data['Close'], short_ema_period)
    data['LongEMA'] = calculate_ema(data['Close'], long_ema_period)
    data['RSI'] = calculate_rsi(data['Close'], rsi_period)

    data['Signal'] = 0

    for i in range(1, len(data)):
        if (data['ShortEMA'].iloc[i] > data['LongEMA'].iloc[i]) and \
           (data['RSI'].iloc[i] < rsi_oversold):
            data['Signal'].iloc[i] = 1  # Buy signal
        elif (data['ShortEMA'].iloc[i] < data['LongEMA'].iloc[i]) and \
             (data['RSI'].iloc[i] > rsi_overbought):
            data['Signal'].iloc[i] = -1  # Sell signal

    return data

def backtest_strategy(data):
    """
    Perform a simple backtest of the strategy to evaluate potential returns.
    """
    data['StrategyReturns'] = data['Signal'].shift(1) * data['Close'].pct_change()
    cumulative_returns = (1 + data['StrategyReturns']).cumprod() - 1
    return cumulative_returns

if __name__ == "__main__":
    # Sample usage with hypothetical data
    # In practice, replace this with actual stock price data
    dates = pd.date_range(start='2020-01-01', periods=100)
    price_data = pd.Series([100 + i + (i % 10 - 5) for i in range(100)], index=dates)
    price_data = pd.DataFrame(price_data, columns=['Close'])

    signals = generate_signals(price_data)
    returns = backtest_strategy(signals)

    print(signals)
    print("Cumulative Returns:")
    print(returns)
```

### Explanation

- **EMA Calculation:** The script calculates two EMAs: a short-term and a long-term. When the short-term EMA crosses above the long-term EMA, it suggests a buying opportunity, and vice versa for a selling opportunity.

- **RSI Calculation:** This measures the speed and change of price movements. It can help identify overbought or oversold conditions. The script uses thresholds of 70 for overbought and 30 for oversold conditions.

- **Signal Generation:** Buy signals occur when the short-term EMA crosses above the long-term EMA, and the RSI is below 30. Sell signals occur when the short-term EMA crosses below the long-term EMA, and the RSI is above 70.

- **Backtesting:** This simple backtest uses the generated signals to calculate hypothetical returns on the strategy.

Ensure to replace the hypothetical data with actual stock price data for meaningful analysis. You can integrate a data source such as an API to fetch live or historical price data for testing.