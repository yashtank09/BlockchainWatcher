import mysql.connector
from web3 import Web3
import time

start = time.time()

cnx = mysql.connector.connect(user='localhost', password='aBC@123.', host='127.0.0.1', database='blockchainwatcher')
coursor = cnx.cursor()

Infura_URL = "https://mainnet.infura.io/v3/78371715113f4bdd946518414b9de62e"

web3Content = Web3(Web3.HTTPProvider(Infura_URL))

BlockDetails = web3Content.eth.get_transaction('0x370831e79f96aba0e926d9d29df1f7b2c357c54536574517990949797054e2e5') #.fromWei('ether')
Blocks = web3Content.eth.get_block(14741984)

addBlocks = ("INSERT INTO Blocks ""(id, Block_Hash, Prerent_Hash, Timestamp, Process) ""VALUES (%s, %s, %s, %s)")

BlockNum = web3Content.eth.block_number

Block_Hash = web3Content.toHex(Blocks['hash'])

Prerent_Hash = web3Content.toHex(Blocks['parentHash'])

Timestamp = Blocks['timestamp']

# Getting process time
a = 0
for i in range(1000):
    a += (i**100)

end = time.time()

processTime = end-start

addBlocksData = (BlockNum, Block_Hash, Prerent_Hash, Timestamp, processTime)

coursor.execute(addBlocks, addBlocksData)
cnx.commit()

cnx.close()
