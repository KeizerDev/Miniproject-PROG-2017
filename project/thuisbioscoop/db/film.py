import sqlobject
from .connection import conn


class Film(sqlobject.SQLObject):
    _connection = conn
    _connection.debug = True
    ft_link = sqlobject.StringCol()
    title = sqlobject.StringCol()
    year = sqlobject.StringCol()
    director = sqlobject.StringCol()
    cast = sqlobject.StringCol()
    genre = sqlobject.StringCol()
    country = sqlobject.StringCol()
    cover_img = sqlobject.StringCol()
    tagline = sqlobject.StringCol()
    length = sqlobject.IntCol()
    synopsis = sqlobject.StringCol()
    ft_rating = sqlobject.FloatCol()
    ft_votes = sqlobject.IntCol()
    imdb_id = sqlobject.StringCol(unique=True)
    imdb_rating = sqlobject.FloatCol()
    imdb_votes = sqlobject.IntCol()
    starttime = sqlobject.StringCol()
    endtime = sqlobject.StringCol()
    channel = sqlobject.StringCol()
    movietip = sqlobject.StringCol()


Film.createTable(ifNotExists=True)
