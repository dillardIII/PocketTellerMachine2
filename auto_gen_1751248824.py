```python
# stealth_liquidity_hunter.py

import requests
from web3 import Web3
import time
import json

# Configuration
configs = {
    'ethereum': {
        'rpc_url': '<ETHEREUM_RPC_URL>',
        'router_address': '<UNISWAP_ROUTER_ADDRESS>',
        'private_key': '<YOUR_PRIVATE_KEY>'
    },
    'binance': {
        'rpc_url': '<BINANCE_SMART_CHAIN_RPC_URL>',
        'router_address': '<PANCAKESWAP_ROUTER_ADDRESS>',
        'private_key': '<YOUR_PRIVATE_KEY>'
    }
}

def check_liquidity(chain, token_address):
    web3 = Web3(Web3.HTTPProvider(configs[chain]['rpc_url']))
    router_address = Web3.toChecksumAddress(configs[chain]['router_address'])
    contract = web3.eth.contract(address=router_address, abi=load_abi())

    reserves = contract.functions.getReserves().call()
    token_reserve = reserves[0] if reserves[0] > reserves[1] else reserves[1]

    if token_reserve > threshold:
        return True
    return False

def load_abi():
    # Load ABI file
    with open('uniswap_router_abi.json', 'r') as abi_file:
        return json.load(abi_file)

def execute_trade(chain, buy=True, token_address=None, amount_in_wei=None):
    web3 = Web3(Web3.HTTPProvider(configs[chain]['rpc_url']))
    account = web3.eth.account.privateKeyToAccount(configs[chain]['private_key'])

    nonce = web3.eth.get_transaction_count(account.address)
    trade_func = web3.eth.contract(
        address=Web3.toChecksumAddress(configs[chain]['router_address']),
        abi=load_abi()
    )

    if buy:
        tx = trade_func.functions.swapExactETHForTokens(
            0,
            [web3.toChecksumAddress(Web3.toHex(token_address))],
            account.address,
            int(time.time()) + 1000
        ).buildTransaction({
            'from': account.address,
            'value': amount_in_wei,
            'gas': 250000,
            'gasPrice': web3.toWei('10', 'gwei'),
            'nonce': nonce
        })
    else:
        pass  # Implement 'sell' logic

    signed_tx = web3.eth.account.sign_transaction(tx, private_key=configs[chain]['private_key'])
    web3.eth.send_raw_transaction(signed_tx.rawTransaction)

def main():
    token_address = '<TARGET_TOKEN_ADDRESS>'
    amount_in_wei = Web3.toWei(0.1, 'ether')
    threshold = 1000000

    while True:
        for chain in configs.keys():
            if check_liquidity(chain, token_address):
                execute_trade(chain, buy=True, token_address=token_address, amount_in_wei=amount_in_wei)
                print(f"Trade executed on {chain}")
                break
        time.sleep(10)

if __name__ == "__main__":
    main()
```

Ensure to replace the placeholder values with actual details like RPC URLs, router addresses, private key, and token address. Make sure to download the ABI for Uniswap or PancakeSwap router and save it as `uniswap_router_abi.json`.