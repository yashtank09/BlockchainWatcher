import time
from web3 import Web3

# Connect to Ganache Access
ganace_URL = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganace_URL))
# print(Web3.isConnected())

Acc_1 = "0x6f7bB93CF132D57C21694025AE73D73afDa7D9B1"
Acc_2 = "0x686F826DcB0E1F2F9475775BE430952F10b2e04D"

Private_key = "b687f5bbeadf633daa84901e29b58cc37f61feeea8a518ff2a7b9780df39a788"

# get the nance
nance = web3.eth.getTransactionCount(Acc_1)

# Buld transaction
tx = {
    'nonce': nance,
    'to': Acc_2,
    'value': web3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei'),
}
# sign Transaction
Sign_Trans = web3.eth.account.signTransaction(tx, Private_key)

# send transaction
tnx_hash = web3.eth.sendRawTransaction(Sign_Trans.rawTransaction)
print(tnx_hash)
print(web3.toHex(tnx_hash))
# get transaction