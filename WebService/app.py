#! /usr/bin/python3.5
from flask import Flask,Response,session,render_template
from Validator import SignatureValidator
from TokenGenerator import TokenGenerator as Generator


from AuthenticationHandler import AuthenticationHandler as AuthHandler
from Validator import SignatureProvider as Provider
app = Flask(__name__,template_folder='Views')
app.secret_key = '2d9-E2.)f&é,A$p@fpa+zSU03êû9_'

from api import api
app.register_blueprint(api_1_0_blueprint, url_prefix='/api')




@app.route("/")
def acceuil():
	return render_template('Accueil.html')









if __name__ == "__main__":
	app.run(debug=True)
