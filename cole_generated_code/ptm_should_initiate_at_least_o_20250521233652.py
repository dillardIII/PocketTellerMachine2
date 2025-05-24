Sure, here's a simple example of a Python script that uses the Alpaca API to initiate a trade. This script will buy 1 share of Apple stock. Please replace `APCA-API-KEY-ID` and `APCA-API-SECRET-KEY` with your actual Alpaca API keys.

```python
import alpaca_trade_api as tradeapi

# Set up the API connection
api = tradeapi.REST('APCA-API-KEY-ID', 'APCA-API-SECRET-KEY', base_url='https://paper-api.alpaca.markets') 

# Define the symbol and quantity for the trade
symbol = 'AAPL'
qty = 1

# Submit the trade
api.submit_order(
    symbol=symbol,
    qty=qty,
    side='buy',
    type='market',
    time_in_force='gtc'
)

print(f"Submitted order to buy {qty} share(s) of {symbol}")
```

This script will initiate a trade in a paper trading environment, which means it's a simulated trade and no real money is involved. This is a good way to gain experience and data for analysis without risking real money. 

Please note that you need to install the `alpaca-trade-api` Python package to use this script. You can install it with pip:

```bash
pip install alpaca-trade-api
```

Also, please be aware that trading involves risk, and this script does not include any kind of risk management or investment strategy. It's important to understand these concepts before trading with real money.