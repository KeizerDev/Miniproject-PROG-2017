import sqlobject

from .connection import conn


class UserBroadcastSupplier(sqlobject.SQLObject):
    """Class voor het databaseobject user_broadcast_supplier"""
    _connection = conn
    _connection.debug = True
    user_id = sqlobject.IntCol()
    broadcast_supplier_id = sqlobject.IntCol()
    code = sqlobject.StringCol()


UserBroadcastSupplier.createTable(ifNotExists=True)
