import sqlobject
from .connection import conn


class Movie(sqlobject.SQLObject):
    """Class voor het databaseobject movie"""
    _connection = conn
    ft_link = sqlobject.StringCol()
    ft_title = sqlobject.StringCol()
    ft_year = sqlobject.StringCol()
    ft_director = sqlobject.StringCol()
    ft_cast = sqlobject.StringCol()
    ft_genre = sqlobject.StringCol()
    ft_country = sqlobject.StringCol()
    ft_cover_img = sqlobject.StringCol()
    ft_tagline = sqlobject.StringCol()
    ft_length = sqlobject.IntCol()
    ft_synopsis = sqlobject.StringCol()
    ft_rating = sqlobject.FloatCol()
    ft_votes = sqlobject.IntCol()
    imdb_id = sqlobject.StringCol(unique=True)
    imdb_rating = sqlobject.FloatCol()
    imdb_votes = sqlobject.IntCol()
    ft_movietip = sqlobject.StringCol()


Movie.createTable(ifNotExists=True)
