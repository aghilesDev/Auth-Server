#! /usr/bin/python3.5
from flask import Flask,Response,session
from Validator import SignatureValidator
from TokenGenerator import TokenGenerator as Generator


from AuthenticationHandler import AuthenticationHandler as AuthHandler
from Validator import SignatureProvider as Provider
app = Flask(__name__)
app.secret_key = '2d9-E2.)f&é,A$p@fpa+zSU03êû9_'

#from .api import api  as api_1_0_blueprint
#app.register_blueprint(api_1_0_blueprint, url_prefix='/api/v1.0')




@app.route("/")
def index():
	if session.get('initial',False)==False:
		session['val']=5
		session['initial']=True
	else :
		session['val']+=1




	authHandler=AuthHandler()

	token=authHandler.generateChallenge('Aghiles')

	print(token)

	private=b'\xd7a^\xcb\xae}\x96R\x95H\x19\x1fu[\xb24E\x91\x86Zm\xdd\x8e~\t>P\x0bf\t\xfdw'
	print('ok')
	signature=Provider(private).sign(message=token)#byte vers chaine
	signature#=signature.decode('utf-8')
	print(signature)

	print('ok')

	token=authHandler.AuthentificateToken(token=token,signature=signature.signature)
	print('ok')
	print('token:{}'.format(token))
	generator=Generator()
	data=generator.decryptToken(token=token)
	if(generator.verifyAuthentificationToken(token)):
	    print('identifiant: {}'.format(data.get('id')))


	return '<h1>holle {}  </h1> token     </br>identifiant'.format(session.get('val',30))









if __name__ == "__main__":
	app.run(debug=True)
