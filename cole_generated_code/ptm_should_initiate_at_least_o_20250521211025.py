from ghost_env import INFURA_KEY, VAULT_ADDRESS
Here is a simple example of how you could initiate a trade using Python. This example uses the `yfinance` library to download stock data and the `alpaca_trade_api` library to initiate the trade. Please replace `APCA-API-KEY-ID` and `APCA-API-SECRET-KEY` with your actual Alpaca API key and secret.

```python
import yfinance as yf
from alpaca_trade_api import REST

# Download historical data for desired stock
data = yf.download('AAPL','2021-01-01','2022-12-31')

# Calculate simple moving average
data['SMA'] = data['Close'].rolling(window=14).mean()

# Create a REST object
api = REST('APCA-API-KEY-ID', 'APCA-API-SECRET-KEY', base_url='https://paper-api.alpaca.markets') 

# Check if the last close price is greater than the SMA
if data['Close'][-1] > data['SMA'][-1]:
    # If true, initiate a buy order
    api.submit_order(
        symbol='AAPL',
        qty=1,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
else:
    # If false, initiate a sell order
    api.submit_order(
        symbol='AAPL',
        qty=1,
        side='sell',
        type='market',
        time_in_force='gtc'
    )
```

This is a very basic example and does not take into account many factors that should be considered when making trades. It's also important to note that this will only initiate a trade, it won't assess the effectiveness of the strategy. That would require additional code to track the performance of the trades over time.