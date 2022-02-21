from web3 import Web3, EthereumTesterProvider
import web3
infura_url = "https://palm-testnet.infura.io/v3/2bd1199ab4664e95affacc45827de31f"
# w3 = Web3(EthereumTesterProvider())
web3 = Web3(Web3.HTTPProvider(infura_url))
# print(web3.isConnected()) # Boolean testNet connect  
# print(web3.eth.blockNumber) # Print blockNumber

