#!/usr/bin/python3.5
#-*- coding: utf-8 -
from flask import Flask,Response,session,render_template,jsonify
from .Validator import SignatureValidator,SignatureProvider
from .TokenGenerator import TokenGenerator as Generator
#from flask.ext.script import Manager



from .AuthenticationHandler import AuthenticationHandler as AuthHandler
from .Validator import SignatureProvider as Provider
app = Flask(__name__,template_folder='Views')
app.secret_key = '2d9-E2.)f&é,A$p@fpa+zSU03êû9_'
#manager = Manager(app)

from .api import api
app.register_blueprint(api, url_prefix='/api2')




@app.route("/")
def acceuil():
	p=SignatureProvider(b'\xd7a^\xcb\xae}\x96R\x95H\x19\x1fu[\xb24E\x91\x86Zm\xdd\x8e~\t>P\x0bf\t\xfdw')
	sign=p.sign("eyJleHAiOjE1Mjc5MDEyMzYsImFsZyI6IkhTMjU2IiwiaWF0IjoxNTI3ODk3NjM2fQ.eyJpZCI6MSwiYXV0aGVudGlmaWVkIjpmYWxzZX0.K1EJRj4-cXVtPComc6vPfmFRUlRpqEETD2NamHWG9LE")
	print(sign.signature)
	s={'d':10}
	print
	return render_template('Acceuil.html')









if __name__ == "__main__":
	app.run()
