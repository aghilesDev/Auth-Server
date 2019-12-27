from web3 import Web3,eth,personal


#Module that contains the BCKContext class which contains the context of the connection with the BlockChaine
#It's Implemented with Factory pattern to avoid creating multiple-connections with the Blockchain
class BCKContext :
    _instance=None

    def __init__(self):
        raise Exception("it's A factory for an instance call DBContext.getinstance()");


    @classmethod
    def getinstance(cls):

        if cls._instance is None:
            #connect the web3 instance to a Node of the blockchaine
            cls._instance = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
            #unlock the account
            if cls._instance.personal.unlockAccount(cls._instance.eth.accounts[0], 'prg2014'):
                #the server use the account of index 0 which have been unlocked
                cls._instance.eth.defaultAccount=cls._instance.eth.accounts[0]

        return cls._instance
