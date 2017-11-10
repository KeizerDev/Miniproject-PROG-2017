import sqlobject
from .connection import conn


class Supplier(sqlobject.SQLObject):
	"""Class voor het databaseobject supplier"""
    _connection = conn

    username = sqlobject.StringCol(unique=True)
    password = sqlobject.StringCol()


Supplier.createTable(ifNotExists=True)
