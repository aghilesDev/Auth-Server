from flask import Blueprint

api = Blueprint('api', __name__)

from . import authentication, posts, users, comments, errors



@api.route('/token')
def get_token(username):
    token=authHandler.generateChallenge('Aghiles')
    if token is None
        return unauthorized('Invalid credentials')
    return jsonify({'token': token})



@api.route('/authentication')
def authentifiate():
    token=authHandler.AuthentificateToken(token=token,signature=signature.signature)
    if token is None
        return unauthorized('Authentication failed')
    return jsonify({'token': token})





@api.route('/posts/')
@auth.login_required
def get_posts():
    pass
