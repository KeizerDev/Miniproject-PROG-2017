import sqlobject
from .connection import conn


class User(sqlobject.SQLObject):
    _connection = conn

    code = sqlobject.StringCol(length=14, unique=True)
    firstName = sqlobject.StringCol()
    mi = sqlobject.StringCol(length=1, default=None)
    lastName = sqlobject.StringCol()
    date = sqlobject.DateTimeCol()


User.createTable(ifNotExists=True)
