from BCKContext import BCKContext
from solc import compile_source
from web3.contract import ConciseContract
import json
import web3
class AuthenticationRepository:

    def __init__(self):
        self.context=BCKContext.getinstance()
        contract_source_code = '''
        pragma solidity ^0.4.0;

        contract Message {
            string _value;

            function Message (string value) public{
                _value=value;
            }

            function getValue() view public returns(string){
                return(_value);
            }

            function setInformation(string value) public{
                _value=value;
            }

        }
        '''
        compiled_sol = compile_source(contract_source_code) # Compiled source code
        self.contract_interface = compiled_sol['<stdin>:Message']

    def getMessage(self,contract_address):
        contract_instance = self.context.eth.contract(abi=self.contract_interface['abi'], address=contract_address)
        message=contract_instance.functions.getValue().call()
        return message




    def setMessage(self,contract_address,message):

        contract_instance = self.context.eth.contract(abi=self.contract_interface['abi'], address=contract_address)
        tx_hash=contract_instance.functions.setInformation(message).transact()
        tx_receipt = self.context.eth.waitForTransactionReceipt(tx_hash)
