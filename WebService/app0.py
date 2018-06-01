#! /usr/bin/python3.5
from flask import Flask,Response,session
import json
import web3
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = '2d9-E2.)f&é,A$p@fpa+zSU03êû9_'

app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://aghiles:prg2014@localhost/AuthDB'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    Contract=db.Column(db.String(50), unique=True, index=True)
    def __repr__(self):
        return '<User %r>' % self.username



#db.create_all()

#aghiles=User(username='Aghiles',Contract='0x5Ec6088d5D323e019495A64379A7d5059e594E32')
#db.session.add(aghiles)
#db.session.commit()
aghiles=User.query.filter_by(username='AGHILES').first()
if(aghiles!=None):
	aghiles.username='Aghiles'
	print('{}'.format(aghiles.Contract))
	db.session.commit()



@app.route("/")
def index():
	if session.get('initial',False)==False:
		session['val']=5
		session['initial']=True
	else :
		session['val']+=1

	return '<h1>helle {}</h1>'.format(session.get('val',30))


def mapper(obj,myClass):
	p=myClass()
	if p.__dict__.keys()==obj.__dict__.keys():
		p.__dict__=obj.__dict__
	else:
		p=None
	return p





if __name__ == "__main__":
	app.run(debug=True)




    #! /usr/bin/python3.5
    from flask import Flask,Response,session
    from Validator import SignatureValidator
    from TokenGenerator import TokenGenerator as Generator


    from AuthenticationHandler import AuthenticationHandler as AuthHandler
    from Validator import SignatureProvider as Provider
    app = Flask(__name__)
    app.secret_key = '2d9-E2.)f&é,A$p@fpa+zSU03êû9_'

    from api import api  as api_1_0_blueprint
    app.register_blueprint(api_1_0_blueprint, url_prefix='/api/v1.0')




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
