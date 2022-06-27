from ethereum import utils
import os, sys

# generate EOA with appendix 1b1b
def generate_eoa1():
    priv = utils.sha3(os.urandom(4096))
    addr = utils.checksum_encode(utils.privtoaddr(priv))

    while not addr.lower().endswith("1b1b"):
        priv = utils.sha3(os.urandom(4096))
        addr = utils.checksum_encode(utils.privtoaddr(priv))

    print('Address: {}\nPrivate Key: {}'.format(addr, priv.hex()))


# generate EOA with the ability to deploy contract with appendix 1b1b
def generate_eoa2():
    priv = utils.sha3(os.urandom(4096))
    addr = utils.checksum_encode(utils.privtoaddr(priv))

    while not (utils.decode_addr(utils.mk_contract_address(addr, 0)).endswith("61") and utils.decode_addr(utils.mk_contract_address(addr, 0)).startswith("fd")):
        priv = utils.sha3(os.urandom(4096))
        addr = utils.checksum_encode(utils.privtoaddr(priv))


    print('Address: {}\nPrivate Key: {}'.format(addr, priv.hex()))


if __name__  == "__main__":
    if sys.argv[1] == "1":
        generate_eoa1()
    elif sys.argv[1] == "2":
        generate_eoa2()
    else:
        print("Please enter valid argument")