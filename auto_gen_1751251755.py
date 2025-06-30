```python
import threading
import time
from web3 import Web3

class LiquidityHunter:
    def __init__(self, rpc_urls, token_contract_address, wallet_address, private_key):
        self.web3_instances = {network: Web3(Web3.HTTPProvider(url)) for network, url in rpc_urls.items()}
        self.token_contract_address = token_contract_address
        self.wallet_address = wallet_address
        self.private_key = private_key
        self.initialized = False

    def initialize(self):
        for web3 in self.web3_instances.values():
            if not web3.isConnected():
                raise ConnectionError("Unable to connect to a Blockchain network.")
        self.initialized = True

    def check_liquidity(self, web3):
        if not self.initialized:
            raise Exception("LiquidityHunter not initialized.")
        
        contract = web3.eth.contract(address=self.token_contract_address, abi=self._get_abi())
        reserves = contract.functions.getReserves().call()
        return reserves[0] > 0 and reserves[1] > 0

    def _get_abi(self):
        # Basic ERC20 token ABI
        return [{"constant":True,"inputs":[],"name":"getReserves","outputs":[{"name":"","type":"uint112"},{"name":"","type":"uint112"},{"name":"","type":"uint32"}],"payable":False,"stateMutability":"view","type":"function"}]

    def buy_token(self, web3):
        contract = web3.eth.contract(address=self.token_contract_address, abi=self._get_abi())
        nonce = web3.eth.getTransactionCount(self.wallet_address)
        
        transaction = contract.functions.purchase().buildTransaction({
            'chainId': web3.eth.chain_id,
            'gas': 250000,
            'gasPrice': web3.toWei('5', 'gwei'),
            'nonce': nonce,
        })
        
        signed_tx = web3.eth.account.sign_transaction(transaction, private_key=self.private_key)
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        return tx_hash

    def monitor_liquidity(self, network):
        web3 = self.web3_instances[network]
        while True:
            if self.check_liquidity(web3):
                print(f"Liquidity detected on {network}!")
                tx_hash = self.buy_token(web3)
                print(f"Purchase transaction sent: {tx_hash.hex()}")
                break
            time.sleep(1)

    def run(self):
        if not self.initialized:
            self.initialize()
        
        threads = []
        for network in self.web3_instances.keys():
            t = threading.Thread(target=self.monitor_liquidity, args=(network,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

if __name__ == "__main__":
    rpc_urls = {
        "Ethereum": "https://mainnet.infura.io/v3/YOUR_PROJECT_ID",
        "BSC": "https://bsc-dataseed.binance.org/",
    }
    token_contract_address = "0xYourTokenContractAddress"
    wallet_address = "0xYourWalletAddress"
    private_key = "YourPrivateKey"
    
    liquidity_hunter = LiquidityHunter(rpc_urls, token_contract_address, wallet_address, private_key)
    liquidity_hunter.run()
```
