from web3 import Web3

# 调用已部署的合约

# geth节点
w3 = Web3(Web3.HTTPProvider('http://123.60.36.208:8545/'))

# 导入外部账户
account = w3.eth.account.from_key(
    "0x7bb22bc28680d0b414a7affb8ff9059291524611ab54f336f985a8ef2c5b6e66")

# 导入调用合约的abi
abi =[
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "addr",
				"type": "address"
			}
		],
		"name": "cal",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]

# 合约地址
address = "0xD4D8F0E620cB907800E305caEBFE34649ecfDA4e"

# 参数
ob_address = ""

# 生成合约实例
contract_instance= w3.eth.contract(address=address, abi=abi)

# 调用合约
ob_address = contract_instance.functions.cal(ob_address).call()