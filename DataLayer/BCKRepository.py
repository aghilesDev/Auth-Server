from .BCKContext import BCKContext
from solc import compile_source
from web3.contract import ConciseContract
import json
import web3

#class that handles the communication with the contracts
class AuthenticationRepository:
    def __init__(self):
        #We get an instance of the connection context with the blockchaine
        self.context=BCKContext.getinstance()
        #Compiling the code of the contract to have his ABI of
        contract_source_code = '''
pragma solidity ^0.4.0;
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
        self.contract_interface = compiled_sol['<stdin>:Authentication']

    def getPublicKeyUser(self,contract_address):
        #make a a contract instance which is an interface to communicate with the contract using the address of the contract and his ABI
        contract_instance = self.context.eth.contract(abi=self.contract_interface['abi'], address=contract_address)
        message=contract_instance.functions.getPublicKeyUser().call()
        return message
