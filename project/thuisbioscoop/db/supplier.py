import sqlobject
from .connection import conn


class Supplier(sqlobject.SQLObject):
    _connection = conn

    username = sqlobject.StringCol(unique=True)
    password = sqlobject.StringCol()


Supplier.createTable(ifNotExists=True)
