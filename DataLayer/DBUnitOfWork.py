from .DBContext import DBContext
from .DBModel import Base


#Based on the unit of work pattern ,the UnitOfWork class handle the commitment of the data in the database,th supression and the creation of tables
class UnitOfWork:

    def __init__(self):
        self.context=DBContext.getinstance()
        self.base=Base

    def createTables(self):
        self.base.metadata.drop_all(self.context.engine)
        self.base.metadata.create_all(self.context.engine)



    def commit(self):
        self.context.session.commit()
