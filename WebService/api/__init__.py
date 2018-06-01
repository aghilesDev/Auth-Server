from flask import Blueprint

api = Blueprint('api', __name__)

from . import authentication, posts, users, comments, errors



@api.route('/token')
def get_token(username):
    token=authHandler.generateChallenge('Aghiles')



@api.route('/authentication')
def authentifiate():
    token=authHandler.AuthentificateToken(token=token,signature=signature.signature)





@api.route('/posts/')
@auth.login_required
def get_posts():
    pass
