
from DBRepository import UserRepository as UserRepo
from DBUnitOfWork import UnitOfWork


uow=UnitOfWork()
uow.createTables()
rep=UserRepo()
user=rep.createUser("aghiles","0x2Be3e8c249cB0Eb95503F8804E2a40D7FaB53445")
uow.commit()





print(user.username)
