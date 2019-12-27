#!/usr/bin/python3.5
from web3 import Web3,eth,personal
from solc import compile_source
from web3.contract import ConciseContract


instance = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
#instance.personal.newAccount('prg2014')
print(instance.eth.account)


contract_source_code = '''
    pragma solidity 0.4.25;
contract Authentication {

    address owner;

    constructor () public{
        owner=msg.sender;
    }

    function getPublicKeyUser() view public returns(address){
        return(owner);
    }



    function setOwner(address newOwner) public{
        if(msg.sender != owner) return;
        owner=newOwner;
    }
}
        '''
compiled_sol = compile_source(contract_source_code)
contract_interface = compiled_sol['<stdin>:Authentication']
contract = instance.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])

for account in instance.eth.accounts:
    print('account: {}\tbalnce: {}'.format(account,instance.eth.getBalance(account)))

instance.eth.defaultAccount=instance.eth.accounts[0]
print(instance.eth.defaultAccount)


if instance.personal.unlockAccount(instance.eth.accounts[0], 'prg2014'):
    print("ok")

tx_hash=contract.constructor().transact()
tx_receipt = instance.eth.waitForTransactionReceipt(tx_hash)
contract_address = tx_receipt['contractAddress']
print("adresse contrat : {}".format(contract_address))
print('taille: {}'.format(len(contract_address)))
