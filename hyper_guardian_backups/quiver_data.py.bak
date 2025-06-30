import os
import requests

QUIVER_API_KEY = os.getenv("QUIVER_API_KEY")
BASE_URL = "https://api.quiverquant.com/beta"

headers = {
    "Authorization": f"Bearer {QUIVER_API_KEY}"
}

# Example: Get Recent Congressional Trades
def get_congress_trades():
    endpoint = "/live/congresstrading"
    url = BASE_URL + endpoint
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data[:10]  # return top 10 most recent
    else:
        print("Error:", response.status_code, response.text)
        return []

# Test it
if __name__ == "__main__":
    trades = get_congress_trades()
    for trade in trades:
        print(f"{trade['Politician']} bought {trade['Ticker']} on {trade['TransactionDate']}")