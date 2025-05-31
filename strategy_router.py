# Strategy Router
def route_strategy(strategy):
    if strategy["type"] == "bullish":
        print("[Strategy Router] Routing to bullish strategy engine...")
    elif strategy["type"] == "bearish":
        print("[Strategy Router] Routing to bearish strategy engine...")
    else:
        print("[Strategy Router] No matching strategy engine found.")