# import mysql.connector
from web3 import Web3


cnx = mysql.connector.connect(user='localhost', password='aBC@123.', host='127.0.0.1', database='blockchainwatcher')
coursor = cnx.cursor()

Infura_URL = "https://mainnet.infura.io/v3/78371715113f4bdd946518414b9de62e"

web3Content = Web3(Web3.HTTPProvider(Infura_URL))

addTransactions = ("INSERT INTO Transactions ""(id, Transaction_Hash, FromAddress, ToAddress, Amount) ""VALUES (%s, %s, %s, %s)")

# ID
BlockNum = web3Content.eth.block_number

# Transaction_Hash
Transact_ID = '0x370831e79f96aba0e926d9d29df1f7b2c357c54536574517990949797054e2e5' # Tnx_Hash
Tnx_Data = web3Content.eth.getTransaction(Transact_ID)

# FromAddress
FromAddress = Tnx_Data['from']

# ToAddress
ToAddress = Tnx_Data['to']

# Amount
Amount = Tnx_Data['value']

addTransactionDetails = (BlockNum, Transact_ID, FromAddress, ToAddress, Amount)

coursor.execute(addTransactions, addTransactionDetails)
cnx.commit()

cnx.close()