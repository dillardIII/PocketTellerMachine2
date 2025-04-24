# ghost_intel.py

import requests

def get_market_intel(query):
    # Placeholder logic while we mock Perplexity
    # Replace with real API call when ready
    sample_responses = {
        "TSLA": "Tesla is up 3% today after strong delivery numbers. Analysts expect continued momentum into Q3.",
        "AMD": "AMD's earnings beat estimates. Revenue from AI chips is projected to double next quarter.",
        "SPY": "SPY is flat today. CPI data expected tomorrow could move the broader market."
    }

    # Return sample or generic if not matched
    return sample_responses.get(query.upper(), f"No direct intel found for '{query}', but markets are mixed and watching macro indicators.")

# Example:
if __name__ == "__main__":
    print(get_market_intel("TSLA"))