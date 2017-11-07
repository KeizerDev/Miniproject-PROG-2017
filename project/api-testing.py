import urllib.request

import xmltodict

from thuisbioscoop.db.movie import Movie
from thuisbioscoop.helpers import ft_url_builder

key = "b2yak0qh1og2kt7v3dc7cb5mah27iurf"

url = ft_url_builder(key, "08-11-2017")
response_xml = urllib.request.urlopen(url).read()
response_dict = xmltodict.parse(response_xml)

for movie in response_dict['filmsoptv']['film']:
    store_movie = Movie.select(Movie.q.imdb_id == movie["imdb_id"]).count()

    if not store_movie:
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
                          ft_starttime=movie["starttijd"],
                          ft_endtime=movie["eindtijd"],
                          ft_channel=movie["zender"],
                          ft_movietip=movie["filmtip"])
