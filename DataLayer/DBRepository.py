from .DBContext import DBContext as Context
from .DBModel import UserModel as User
from sqlalchemy import or_

#this class allow us to the users tables with the CRUD(Create,Read,Update,Delete) paradigm
class UserRepository:
    def __init__(   self):
        self.session=Context.getinstance().session

    def createUser(self,name,contract):
        user=self.session.query(User).filter(or_(User.username==name,User.Contract==contract)).first()
        if user is not  None:
            print("utilisateur existe deja")
            return None
        user=User(username=name,Contract=contract)
        self.session.add(user)
        return user

    def readUser(self,name):
        user=self.session.query(User).filter(User.username==name).first()
        return user

    def readUserById(self,id):
        user=self.session.query(User).filter(User.id==id).first()
        return user

    def updateUser(self,beforeName,name,contract):
        user=self.session.query(User).filter(User.username==beforeName).first()
        if user is None:
            return None
        user.username=name
        user.Contract=contract
        return user


    def deleteUser(self):
        pass
