from ghost_env import INFURA_KEY, VAULT_ADDRESS
def get_strategy_metadata():
    return [
        {
            "name": "covered_call",
            "type": "options",
            "description": "Earn premium by selling calls against stock you own."
        },
        {
            "name": "cash_secured_put",
            "type": "options",
            "description": "Sell puts with cash on hand in case assigned. Great for entry."
        },
        {
            "name": "iron_condor",
            "type": "multi-leg",
            "description": "Neutral strategy using both a call and put credit spread."
        },
        {
            "name": "credit_spread",
            "type": "options",
            "description": "Sell a closer strike, buy a further one. Profit from time decay."
        },
        {
            "name": "long_call",
            "type": "directional",
            "description": "Bullish bet on a stock going up."
        },
        {
            "name": "long_put",
            "type": "directional",
            "description": "Bearish bet on a stock going down."
        },
        {
            "name": "straddle",
            "type": "volatility",
            "description": "Expect a big move, but not sure which direction."
        },
        {
            "name": "strangle",
            "type": "volatility",
            "description": "Similar to straddle, but with further strikes. Cheaper."
        },
        {
            "name": "stock_momentum",
            "type": "technical",
            "description": "Enter trades when RSI is bullish and price above SMA."
        },
        {
            "name": "reversal_play",
            "type": "technical",
            "description": "Betting on a reversal when RSI is oversold or overbought."
        }
    ]

def log_event():ef drop_files_to_bridge():