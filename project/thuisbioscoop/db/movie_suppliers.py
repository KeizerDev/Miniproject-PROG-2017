import sqlobject
from .connection import conn


class MovieSuppliers(sqlobject.SQLObject):
    _connection = conn
    _connection.debug = True
    imdb_id = sqlobject.StringCol()
    supplier_id = sqlobject.IntCol()
    expire_date = sqlobject.IntCol()


MovieSuppliers.createTable(ifNotExists=True)
