import sqlobject
import datetime

from sqlobject import AND, OR

from thuisbioscoop.db.broadcast_time import BroadcastTime
from thuisbioscoop.db.movie import Movie

time = datetime.datetime.now()
current_date = time.strftime("%Y-%m-%d %H:%M")

def valid_key():
    expire_time = BroadcastTime.select(BroadcastTime.q.ft_endtime)
    expire_date = expire_time.strftime("%Y-%m-%d %H:%M")
    global current_date
    if expire_date > current_date:

    else:
        return

def supplier_films():
    # suppliers = BroadcastTime.select(BroadcastTime.q.ft_channel)
    # movie_title = Movie.select(Movie.q.ft_title)
    global current_date
    movie_id_1 = Movie.select(Movie.q.imdb_id)
    movie_id_2 = BroadcastTime.select(BroadcastTime.q.imdb_id)
    if movie_id_1 == movie_id_2:
        for start_time in BroadcastTime.selectBy(code = movie_id_2).locate.starttime:
            if start_time > current_date:
                print(Movie.selectBy(code = movie_id_1).locate.ft_title + 'op' + BroadcastTime.selectBy(code = movie_id_2).locate.ft_channel)
    else:
        return

# def total_users(users, valid_users):
#     valid_key(expire_date > current_date)
#     users =
#     valid_users = users and valid_key(expire_date > current_date)

# def users_film():
#     users =
