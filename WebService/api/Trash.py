from flask.ext.httpauth import HTTPBasicAuth

#from ..TokenGenerator
#from ...DataLayer.DBRepository import UserRepository
import sys
sys.path.insert(0,'..')
from TokenGenerator import TokenGenerator as TokenGen



auth = HTTPBasicAuth()

tokenGen=TokenGen()





@auth.verify_password
def verify_password(username,password):
    return tokenGen.verifyAuthentificationToken(username)
