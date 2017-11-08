import sqlobject
import datetime

from sqlobject import AND, OR

from thuisbioscoop.db.broadcast_time import BroadcastTime
from thuisbioscoop.db.movie import Movie

# def total_users(users, valid_users):
#     valid_key(expire_date > current_date)
#     users =
#     valid_users = users and valid_key(expire_date > current_date)
#
# def users_film():
#     users =

def supplier_films():
    # suppliers = BroadcastTime.select(BroadcastTime.q.ft_channel)
    # movie_title = Movie.select(Movie.q.ft_title)
    movie_id_1 = Movie.select(Movie.q.imdb_id)
    movie_id_2 = BroadcastTime.select(BroadcastTime.q.imdb_id)
    if movie_id_1 == movie_id_2:
        print(Movie.selectBy(code = movie_id_1).locate.ft_title + 'op' + BroadcastTime.selectBy(code = movie_id_2).locate.ft_channel)
    else:
        return

# def valid_key(expire_date, current_date):
#     expire_date = BroadcastTime.select(BroadcastTime.q.ft_endtime)
#     current_date = {datetime.datetime.now():"%d-%m-%Y"}
#     if expire_date > current_date:
#
#     else:
