```python
import time
from decimal import Decimal
from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_account import Account

# Configuration for Ethereum network
ETH_RPC_URL = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'
PRIVATE_KEY = 'YOUR_PRIVATE_KEY'

# Configuration for Binance Smart Chain network
BSC_RPC_URL = 'https://bsc-dataseed.binance.org/'
BSC_PRIVATE_KEY = 'YOUR_BSC_PRIVATE_KEY'

# Configuration Parameters
TOKEN_CONTRACT_ADDRESS = '0xTOKEN_CONTRACT_ADDRESS'
WETH_CONTRACT_ADDRESS = '0xc778417E063141139Fce010982780140Aa0cD5Ab'  # Example for Ethereum Testnet
SLIPPAGE = 0.01  # 1% slippage

# Web3 Instances
web3_eth = Web3(Web3.HTTPProvider(ETH_RPC_URL))
web3_bsc = Web3(Web3.HTTPProvider(BSC_RPC_URL))
web3_bsc.middleware_stack.inject(geth_poa_middleware, layer=0)  # Required for BSC

def set_web3_network(network):
    if network == 'eth':
        return web3_eth, PRIVATE_KEY
    elif network == 'bsc':
        return web3_bsc, BSC_PRIVATE_KEY
    else:
        raise ValueError(f"Unsupported network: {network}")

def get_account(network):
    web3, private_key = set_web3_network(network)
    account = Account.from_key(private_key)
    return account

def create_buy_tx(web3, token_address, account, amount_in_ether):
    # ABI for interacting with the contract
    uniswap_abi = '[...]'  # Should provide the full ABI depending on the DEX you're interacting with
    router_address = '0xf164fC0Ec4E93095b804a4795bBe1e041497b92a'  # Uniswap V2 Router for example
    contract = web3.eth.contract(address=router_address, abi=uniswap_abi)

    # Estimate gas
    estimated_gas = contract.functions.swapExactETHForTokens(
        int((1 - SLIPPAGE) * 100),
        [WETH_CONTRACT_ADDRESS, token_address],
        account.address,
        int(time.time()) + 1000
    ).estimateGas({'from': account.address, 'value': web3.toWei(amount_in_ether, 'ether')})

    # Build transaction
    nonce = web3.eth.get_transaction_count(account.address)
    tx = contract.functions.swapExactETHForTokens(
        int((1 - SLIPPAGE) * 100),
        [WETH_CONTRACT_ADDRESS, token_address],
        account.address,
        int(time.time()) + 1000
    ).buildTransaction({
        'from': account.address,
        'value': web3.toWei(amount_in_ether, 'ether'),
        'gas': estimated_gas,
        'gasPrice': web3.toWei('5', 'gwei'),
        'nonce': nonce
    })
    return tx

def send_transaction(web3, account, tx):
    signed_tx = account.sign_transaction(tx)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return tx_hash

def hunter():
    networks = ['eth', 'bsc']
    for network in networks:
        web3, _ = set_web3_network(network)
        account = get_account(network)

        balance = web3.eth.get_balance(account.address)
        if balance > web3.toWei(0.1, 'ether'):  # Check for a minimum balance
            token_price = 0.01  # Example token price in ethers
            amount_in_ether = 0.01

            try:
                tx = create_buy_tx(web3, TOKEN_CONTRACT_ADDRESS, account, amount_in_ether)
                tx_hash = send_transaction(web3, account, tx)
                print(f"Transaction sent on {network}: {tx_hash.hex()}")
            except Exception as e:
                print(f"Failed on {network}: {e}")

if __name__ == '__main__':
    while True:
        hunter()
        time.sleep(10)  # Poll every 10 seconds
```
