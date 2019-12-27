from web3 import Web3,eth,personal
from solc import compile_source
from web3.contract import ConciseContract
import json
import web3

# Initialising a Web3 instance with an RPCProvider:
#web3rpc = Web3(TestRPCProvider())

# or specifying host and port.
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))


with open('/home/aghiles/.ethereum/keystore/UTC--2018-04-30T00-02-44.472920115Z--998692d7a478d2c006330ec2cab5c0142ee804f5') as keyfile:
    encrypted_key = keyfile.read()
    private_key = w3.eth.account.decrypt(encrypted_key, 'astabene69')
    print('privKey: {}\n pubkey {}'.format(private_key,w3.eth.accounts[0]))



privee=b'\xd7a^\xcb\xae}\x96R\x95H\x19\x1fu[\xb24E\x91\x86Zm\xdd\x8e~\t>P\x0bf\t\xfdw'
public='0x998692D7a478D2C006330ec2cAB5c0142eE804f5'



for account in w3.eth.accounts:
    print('account: {}\tbalnce: {}'.format(account,w3.eth.getBalance(account)))

w3.eth.defaultAccount=w3.eth.accounts[0]
print(w3.eth.defaultAccount)

contract_source_code = '''
pragma solidity ^0.4.0;
contract Authentication {

address owner;
string ipAddress;

constructor (string _ipAddress) public{
owner=msg.sender;
ipAddress=_ipAddress;
}

function getPublicKeyUser() view public returns(address){
return(owner);
}

function getIpAddressUser() view public returns(string){
return(ipAddress);
}

function setOwner(address newOwner) public{
if(msg.sender != owner) return;
owner=newOwner;
}
}
'''
compiled_sol = compile_source(contract_source_code) # Compiled source code
contract_interface = compiled_sol['<stdin>:Authentication']



if w3.personal.unlockAccount(w3.eth.accounts[1], 'astabene69'):
    print("ok")
# Instantiate and deploy contract
contract = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])
tx_hash=contract.constructor('192.168.45.208').transact()
# Get transaction hash from deployed contract
#tx_hash = contract.deploy(transaction={'from': w3.eth.accounts[0], 'gas': 410000})


# Get tx receipt to get contract address
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    #print(tx_receipt)

contract_address = tx_receipt['contractAddress']
print("adresse contrat : {}".format(contract_address))
print('taille: {}'.format(len(contract_address)))
# Contract instance in concise mode
contract_instance = w3.eth.contract(abi=contract_interface['abi'], address=contract_address)

print("message: {}".format(contract_instance.functions.getPublicKeyUser().call()))




    # tip: do not save the key or password anywhere, especially into a shared source file

### Setting defaults
#web3.eth.account.create('asdf')
#web3.eth.defaultAccount = <your (unlocked) account>
#web3.eth.defaultBlock = "latest"
# Can also be an integer or one of "latest", "pending", "earliest"
