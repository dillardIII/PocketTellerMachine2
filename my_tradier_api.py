from ghost_env import INFURA_KEY, VAULT_ADDRESS
class TradierClient:
    def get_quote(self, ticker):
        # Simulate a Tradier quote response
        print(f"[TradierClient] Fetching quote for {ticker}")
        return {
            "open": 150.0,
            "high": 155.0,
            "low": 148.5,
            "volume": 1000000
        }

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():