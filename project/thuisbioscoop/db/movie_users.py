import sqlobject
from .connection import conn


class Film_Users(sqlobject.SQLObject):
    _connection = conn
    _connection.debug = True


Film.createTable(ifNotExists=True)