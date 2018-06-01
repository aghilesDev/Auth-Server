from flask.ext.httpauth import HTTPBasicAuth
from ..Validator import SignatureValidator,SignatureProvider
from ..TokenGenerator
from ...DataLayer.DBRepository import UserRepository
auth = HTTPBasicAuth()






@auth.verify_password
def verify_password(token,signedToken):
    token



if email == '':
g.current_user = AnonymousUser()
return True
user = User.query.filter_by(email = email).first()
if not user:
return False
g.current_user = user
return user.verify_password(password)
