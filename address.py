from eth_account import Account

from web3 import Web3

def createNewETHWallet():
    """用于生成尾号为<>的地址"""
    while True:
        account = Account.create()
        privateKey = account._key_obj
        publicKey = privateKey.public_key
        address = publicKey.to_checksum_address()
        # print(address[-4::])
        if address[-4::] == "525B":
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            break
    print(privateKey)
    print(publicKey)
    print(address) 

if __name__ == "__main__":
    createNewETHWallet()