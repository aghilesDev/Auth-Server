from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String

Base = declarative_base()

#It's a model of the representation of the users table,it store the data took from the database
class UserModel(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(64), unique=True, index=True)
    Contract=Column(String(50), unique=True, index=True)
    def __repr__(self):
        return '<User %r>' % self.username
