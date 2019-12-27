from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#Module that contains the DBContext class which contains the context of the connection with the Database
#It's Implemented with Factory pattern to avoid creating multiple-connections with the database
class DBContext:

    _instance=None

    def __init__(self):
        raise Exception("it's A factory for an instance call DBContext.getinstance()");

    @classmethod
    def getinstance(cls):
        if cls._instance is None:
            cls._instance=super(DBContext,cls).__new__(cls)
            #create a connection with database
            cls._instance.engine = create_engine('postgresql://aghiles:prg2014@localhost/AuthDB', echo=False)
            #create a session maker wich allow create sessions
            cls._instance.sessionMaker=sessionmaker(bind=cls._instance.engine)
            cls._instance.session=cls._instance.sessionMaker()
        return cls._instance
