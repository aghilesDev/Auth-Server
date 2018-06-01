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
