import sqlobject
from .connection import conn


class BroadcastSupplier(sqlobject.SQLObject):
    _connection = conn
    _connection.debug = True
    broadcast_time_id = sqlobject.IntCol(unique=True)
    supplier_id = sqlobject.IntCol()


BroadcastSupplier.createTable(ifNotExists=True)
