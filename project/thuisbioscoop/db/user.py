import sqlobject
from .connection import conn


class User(sqlobject.SQLObject):
	"""Class voor het databaseobject user"""
    _connection = conn
    emailAddress = sqlobject.StringCol(unique=True)
    name = sqlobject.StringCol()


User.createTable(ifNotExists=True)
