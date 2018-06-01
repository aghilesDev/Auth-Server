from web3.auto import w3
from eth_account.messages import defunct_hash_message






class SignatureValidator:




    def validate(self,publicKey,token,signature):
        message_hash = defunct_hash_message(text=token)
        result=w3.eth.account.recoverHash(message_hash, signature=signature)
        print(result)
        if(result==publicKey):
            return True
        return False

class SignatureProvider:

    def __init__(self,privateKey):
        self._privateKey=privateKey

    def sign(self,message):
        message_hash = defunct_hash_message(text=message)
        signed_message = w3.eth.account.signHash(message_hash, private_key=self._privateKey)
        return signed_message
