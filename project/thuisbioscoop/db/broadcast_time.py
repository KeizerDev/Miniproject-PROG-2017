import sqlobject
from .connection import conn


class BroadcastTime(sqlobject.SQLObject):
    _connection = conn
    _connection.debug = True
    imdb_id = sqlobject.StringCol()
    ft_starttime = sqlobject.StringCol()
    ft_endtime = sqlobject.StringCol()
    ft_channel = sqlobject.StringCol()


BroadcastTime.createTable(ifNotExists=True)
