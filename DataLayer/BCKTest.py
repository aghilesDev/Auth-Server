from web3 import Web3,eth,personal
from solc import compile_source
from web3.contract import ConciseContract
import json
import web3
from BCKRepository import AuthenticationRepository



from DBRepository import UserRepository as UserRepo

# Initialising a Web3 instance with an RPCProvider:
#web3rpc = Web3(TestRPCProvider())

# or specifying host and port.
user=UserRepo()
contract=user.readUser('Aghiles').Contract

auth=AuthenticationRepository()
print(auth.getMessage(contract))
auth.setMessage(contract,"0x998692D7a478D2C006330ec2cAB5c0142eE804f5")
