from web3 import Web3, EthereumTesterProvider
import json
infura_url = "https://palm-testnet.infura.io/v3/2bd1199ab4664e95affacc45827de31f"
# w3 = Web3(EthereumTesterProvider())
web3 = Web3(Web3.HTTPProvider(infura_url))
# print(web3.isConnected()) # Check testNet connect  


# plz go to ethscan
abi = "" #smart contract looks okays
address = "" #deployed smart contract 

contract = web3.eth.contract(address=address, abi=abi)
totalSupply = contract.functions.totalSupply().call()





