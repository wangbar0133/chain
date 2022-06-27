from web3 import Web3

# 读取slot

w3 = Web3(Web3.HTTPProvider('http://123.60.36.208:8545/'))

value = w3.eth.getStorageAt("0x21ac0df70A628cdB042Dde6f4Eb6Cf49bDE00Ff7", 2).hex()

print(value)