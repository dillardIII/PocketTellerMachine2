```python
# evolution_module.py

import random
from typing import List, Dict, Callable

def mutate_trading_strategy(strategy: Dict[str, float]) -> Dict[str, float]:
    """Mutate a trading strategy by tweaking its parameters."""
    mutation_rate = 0.1  # 10% chance to mutate each parameter
    for key in strategy:
        if random.random() < mutation_rate:
            strategy[key] += random.uniform(-0.05, 0.05)  # Random small change
    return strategy

def create_ghost_ai_agents(num_agents: int) -> List[Dict[str, float]]:
    """Create a number of ghost AI agents with randomized strategies."""
    agents = []
    for _ in range(num_agents):
        agent = {'risk_tolerance': random.uniform(0.1, 1.0),
                 'investment_bias': random.uniform(0.1, 1.0),
                 'aggressiveness': random.uniform(0.1, 1.0)}
        agents.append(agent)
    return agents

def analyze_liquidity(market_data: Dict[str, List[float]], threshold: float) -> List[str]:
    """Analyze market liquidity and return markets that pass the threshold."""
    high_liquidity_markets = []
    for market, data in market_data.items():
        average_liquidity = sum(data) / len(data)
        if average_liquidity > threshold:
            high_liquidity_markets.append(market)
    return high_liquidity_markets

def manage_vault_payouts(vault_funds: float, distribution_ratios: Dict[str, float]) -> Dict[str, float]:
    """Distribute funds from the vault based on predefined ratios."""
    payouts = {}
    for entity, ratio in distribution_ratios.items():
        payouts[entity] = vault_funds * ratio
    return payouts

if __name__ == "__main__":
    # Example usage of the module
    initial_strategy = {'risk_tolerance': 0.5, 'investment_bias': 0.5, 'aggressiveness': 0.5}
    mutated_strategy = mutate_trading_strategy(initial_strategy)
    print("Mutated Strategy:", mutated_strategy)

    ghost_agents = create_ghost_ai_agents(5)
    print("Created Ghost AI Agents:", ghost_agents)

    market_liquidity_data = {
        'market1': [100, 150, 120],
        'market2': [80, 85, 90],
        'market3': [200, 210, 220]
    }
    high_liquidity_markets = analyze_liquidity(market_liquidity_data, 150)
    print("High Liquidity Markets:", high_liquidity_markets)

    vault_funds = 10000
    distribution_ratios = {'entity1': 0.4, 'entity2': 0.6}
    payouts = manage_vault_payouts(vault_funds, distribution_ratios)
    print("Vault Payouts:", payouts)
```