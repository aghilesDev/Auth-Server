from web3 import Web3,eth,personal

class BCKContext :
    _instance=None

    def __init__(self):
        raise Exception("it's A factory for an instance call DBContext.getinstance()");


    @classmethod
    def getinstance(cls):

        if cls._instance is None:
            cls._instance = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
            if cls._instance.personal.unlockAccount(cls._instance.eth.accounts[0], 'astabene69'):
                cls._instance.eth.defaultAccount=cls._instance.eth.accounts[0]
                

        return cls._instance
