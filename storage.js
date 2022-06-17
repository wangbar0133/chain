let Web3 = require("web3")

let web3 = new Web3(new Web3.providers.HttpProvider("https://ropsten.infura.io/v3/c05bace974064c25ae612ad7e7afb5aa"))

// address and slot loc
let pin = web3.eth.getStorageAt("0x7e3ed5d28db7be6b572bf96f37ae92f98b491a5f", 0).then(console.log)