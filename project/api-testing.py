import urllib.request
import datetime
import xmltodict
import os.path

from sqlobject import AND

from thuisbioscoop.db.broadcast_time import BroadcastTime
from thuisbioscoop.db.movie import Movie
from thuisbioscoop.helpers import ft_url_builder, download_image

# TODO: move to config
key = "b2yak0qh1og2kt7v3dc7cb5mah27iurf"

url = ft_url_builder(key, f"{datetime.datetime.now():%d-%m-%Y}")
# url = ft_url_builder(key, "09-11-2017")
response_xml = urllib.request.urlopen(url).read()
response_dict = xmltodict.parse(response_xml)

for movie in response_dict['filmsoptv']['film']:
    stored_movie = Movie.select(Movie.q.imdb_id == movie["imdb_id"]).count()
    stored_broadcast_time = BroadcastTime.select(
        AND(
            BroadcastTime.q.imdb_id == movie["imdb_id"],
            BroadcastTime.q.ft_starttime == movie["starttijd"],
            BroadcastTime.q.ft_endtime == movie["eindtijd"],
            BroadcastTime.q.ft_channel == movie["zender"]
        )
    ).count()

    if not stored_movie:
        new_movie = Movie(ft_link=movie["ft_link"],
                          ft_title=movie["titel"],
                          ft_year=movie["jaar"],
                          ft_director=movie["regisseur"],
                          ft_cast=movie["cast"],
                          ft_genre=movie["genre"],
                          ft_country=movie["land"],
                          ft_cover_img=movie["cover"],
                          ft_tagline=movie["tagline"],
                          ft_length=int(movie["duur"]),
                          ft_synopsis=movie["synopsis"],
                          ft_rating=float(movie["ft_rating"]),
                          ft_votes=int(movie["ft_votes"]),
                          imdb_id=movie["imdb_id"],
                          imdb_rating=float(movie["imdb_rating"]),
                          imdb_votes=int(movie["imdb_votes"]),
                          ft_movietip=movie["filmtip"])

    if not stored_broadcast_time:
        new_broadcast_time = BroadcastTime(imdb_id=movie["imdb_id"],
                                           ft_starttime=movie["starttijd"],
                                           ft_endtime=movie["eindtijd"],
                                           ft_channel=movie["zender"])

    download_image(movie['cover'], movie['imdb_id'])
