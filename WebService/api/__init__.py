from flask import Blueprint,jsonify,Response,json,request


import sys
sys.path.insert(0,'..')
from WebService.AuthenticationHandler import authHandler,UserRepository,TokenGenerator



api = Blueprint('api', __name__)


tokenGen=TokenGenerator()
userRepo=UserRepository()


def makeReponse(data,code):
    response = Response(
        response=json.dumps(data),
        status=code,
        mimetype='application/json'
    )

    return response


@api.route('/token/<username>')
def getToken(username):
    token=authHandler.generateChallenge(username)
    if token is None:
        return makeReponse({'information':"l'utilisateur n'éxiste pas"},404)
    return makeReponse({'token': token},200)



@api.route('/authentication',methods=['POST'])
def authentifiate():
    token=request.get_json(force=True).get('token',None)
    print('ok{}'.format(token))
    signature=request.json.get('signature',None)
    if token is None or signature is None:
        return makeReponse({'information':"Requete mal formée"},400)
    token=authHandler.AuthentificateToken(token=token,signature=signature)
    if token is None:
        return  makeReponse({'information':"Authentification à échoué"},403)
    print(token)

    return makeReponse({'token':token},200)


@api.route('/connect',methods=['POST'])
def get_connection():
    token=request.get_json(force=True).get('token',None)
    if(token is None):
        return makeReponse({'information':"Authentification demandée"},401)
    if(tokenGen.verifyAuthentificationToken(token) == False):
        return  makeReponse({'information':"Authentification à échoué"},403)
    data=tokenGen.decryptToken(token)
    if(data is None):
        return makeReponse({'information':"Requete mal formée"},400)
    userid=data.get('id',None)
    print(userid)
    user=userRepo.readUserById(userid)
    if(user is None):
        return makeReponse({'information':"l'utilisateur n'éxiste pas"},404)
    return makeReponse({'username':user.username,'contract':user.Contract},200)



    return "{}".format()
