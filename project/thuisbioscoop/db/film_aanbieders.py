import sqlobject
from .connection import conn


class Film_Aanbieders(sqlobject.SQLObject):
    _connection = conn
    _connection.debug = True


Film.createTable(ifNotExists=True)