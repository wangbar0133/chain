from web3 import Web3

address = ""
code_hash = ""

i = 0
while(True):
    salt = hex(i)[2:].rjust(64, '0')
    s = "0xff" + address + salt + code_hash
    hashed = Web3.sha3(hexstr=s)
    address = ''.join(['%02x' % b for b in hashed])
  