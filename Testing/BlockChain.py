# web3 Module for interacting with Etherium
from web3 import Web3

# Getting Infura url that allow developers to easily take their blockchain application from testing to scaled deployment - with simple, reliable access to Ethereum and IPFS
Infura_URL = "https://mainnet.infura.io/v3/78371715113f4bdd946518414b9de62e"

# make connection to Blockchain
web3 = Web3(Web3.HTTPProvider(Infura_URL))

# Checking is we connected with Chain
print(web3.isConnected())

# here we are printing block number
print(web3.eth.blockNumber)

# getting balance of Metamask Wallet using their hash code
Balance = web3.eth.getBalance('0xfEa5D9023Cd95F3a60584C812f3d5C8cEDa41a7d')

print(web3.fromWei(Balance, 'ether'))