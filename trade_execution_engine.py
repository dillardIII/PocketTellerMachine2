from ptm_config import PAPER_TRADING_MODE

def execute_trade(strategy, ticker, side, qty, entry_price):
    print(f"[Execution] {('PAPER' if PAPER_TRADING_MODE else 'LIVE')} TRADE: {side} {qty} {ticker} at {entry_price}")

    # === Paper Trading Simulation ===
    if PAPER_TRADING_MODE:
        return {
            "mode": "paper",
            "strategy": strategy,
            "ticker": ticker,
            "side": side,
            "qty": qty,
            "entry_price": entry_price,
            "status": "simulated",
            "executed_at": entry_price
        }

    # === Live Execution Placeholder (to be integrated with API later) ===
    try:
        # Future code example:
        # result = tradier_api.submit_order(ticker, side, qty, entry_price)
        return {
            "mode": "live",
            "strategy": strategy,
            "ticker": ticker,
            "side": side,
            "qty": qty,
            "entry_price": entry_price,
            "status": "submitted",
            "executed_at": entry_price
        }
    except Exception as e:
        print(f"[Execution ERROR] {e}")
        return {
            "mode": "live",
            "status": "error",
            "error": str(e)
        }