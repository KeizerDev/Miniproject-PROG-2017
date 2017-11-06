import sqlobject
from .connection import conn


class Film(sqlobject.SQLObject):
    _connection = conn

    ft_link = sqlobject.StringCol(length=14, unique=True)
    title = sqlobject.StringCol(length=25)
    year = sqlobject.DateTimeCol(default=None)
    director = sqlobject.StringCol(length=25)
    cast = sqlobject.StringCol(length=50)
    genre = sqlobject.StringCol(length=25)
    country = sqlobject.StringCol(length=25)
    cover_img = sqlobject.StringCol(length=30)
    tagline = sqlobject.StringCol(length=25)
    length = sqlobject.IntCol(length=4)
    synopsis = sqlobject.StringCol(length=100)
    ft_rating = sqlobject.IntCol(length=4)
    ft_votes = sqlobject.IntCol(length=4)
    imdb_id = sqlobject.IntCol(length=10)
    imdb_rating = sqlobject.IntCol(length=4)
    imdb_votes = sqlobject.IntCol(length=6)
    starttime = sqlobject.IntCol(length=11)
    endtime = sqlobject.IntCol(length=11)
    channel = sqlobject.StringCol(length=10)
    movietip = sqlobject.StringCol(length=12)

Film.createTable(ifNotExists=True)
