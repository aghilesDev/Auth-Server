from Validator import SignatureValidator#,SignatureProvider
from TokenGenerator import TokenGenerator
import sys
sys.path.insert(0,'../DataLayer')

from DBRepository import UserRepository
from BCKRepository import AuthenticationRepository as AuthRepo





class AuthenticationHandler:

    def __init__(self,userRepo=UserRepository,signatureValidator=SignatureValidator,tokenGenerator=TokenGenerator,authRepo=AuthRepo):
        self.userRepo=userRepo()
        self.signatureValidator=signatureValidator()
        self.tokenGen=tokenGenerator()
        self.authRepo=authRepo()
        pass


    def generateChallenge(self,username):
        user=self.userRepo.readUser(username)
        if(user is None):
            #error
            print('erreur')
        token=self.tokenGen.generateChallengeToken(user.id)
        return token



    def AuthentificateToken(self,token,signature):


        if(self.tokenGen.verifyChallengeToken(token) is False):
            return None #token non valide
        data=self.tokenGen.decryptToken(token)
        userid=data.get('id')
        user=self.userRepo.readUserById(userid)
        if(user is None):
            return None #user n'existe pas
        publicKey=self.authRepo.getMessage(user.Contract)
        if self.signatureValidator.validate(publicKey=publicKey,token=token,signature=signature):#la chaine de caractere du token
            return self.tokenGen.generateAuthentificationToken(user.id) #l'utilisateur est authentifier on lui donne un token d'authentification
        return None #signature ne correspond pas

authHandler=AuthenticationHandler()
