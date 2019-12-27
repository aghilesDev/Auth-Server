from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app


#TokenGenerator is a class wich handle the generation,validation and decryptage of challange tokens and authentication tokens
class TokenGenerator:
    def generateChallengeToken(self,id,expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'id': id,'authentified':False}).decode('utf-8')

    def generateAuthentificationToken(self,id,expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'id': id,'authentified':True}).decode('utf-8')


    def decryptToken(self,token):
        token=token.encode('utf-8')
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        return data

    def verifyChallengeToken(self,token):
        data=self.decryptToken(token=token)
        if data == None:
            return False
        if data.get('authentified') == True:
            return False
        return True

    def verifyAuthentificationToken(self,token):
        data=self.decryptToken(token=token)
        if data == None:
            return False
        if data.get('authentified') == False:
            return False
        return True
