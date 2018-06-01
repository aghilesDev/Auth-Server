
from DBRepository import UserRepository as UserRepo
from DBUnitOfWork import UnitOfWork


uow=UnitOfWork()
#uow.createTables()
rep=UserRepo()
user=rep.createUser("Islam","0x5Ec6088d5D323e019495A64379A7d5059e594E32")
uow.commit()
u2=rep.readUser("Aghiles")





print(u2.username)
