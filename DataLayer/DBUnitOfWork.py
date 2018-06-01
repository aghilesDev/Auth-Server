from DBContext import DBContext
from DBModel import Base



class UnitOfWork:

    def __init__(self):
        self.context=DBContext.getinstance()
        self.base=Base

    def createTables(self):
        self.base.metadata.drop_all(self.context.engine)
        self.base.metadata.create_all(self.context.engine)



    def commit(self):
        self.context.session.commit()
