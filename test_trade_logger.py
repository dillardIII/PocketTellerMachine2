from ghost_env import INFURA_KEY, VAULT_ADDRESS
from log_trade_class import TradeLogger
from my_tradier_api import TradierClient
from sentiment_model import get_sentiment
from risk_module import grade_risk

# Instantiate with dependencies
logger = TradeLogger(TradierClient(), get_sentiment, grade_risk)

# Log a trade
logger.log_trade("AAPL", "buy_call", quantity=2)

def log_event():ef drop_files_to_bridge():