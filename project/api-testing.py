from thuisbioscoop.db.film import Film
import urllib.request

key = "b2yak0qh1og2kt7v3dc7cb5mah27iurf"
baseUrl = "http://api.filmtotaal.nl/filmsoptv.xml?apikey=" + key

fullUrl = baseUrl + "&dag=07-11-2017&sorteer=0"

response = urllib.request.urlopen(fullUrl).read()

import xmltodict

doc = xmltodict.parse(response)

for film in doc['filmsoptv']['film']:
    print(film['titel'])
    newFilm = Film(ft_link=film["ft_link"],
                   title=film["titel"],
                   year=film["jaar"],
                   director=film["regisseur"],
                   cast=film["cast"],
                   genre=film["genre"],
                   country=film["land"],
                   cover_img=film["cover"],
                   tagline=film["tagline"],
                   length=int(film["duur"]),
                   synopsis=film["synopsis"],
                   ft_rating=float(film["ft_rating"]),
                   ft_votes=int(film["ft_votes"]),
                   imdb_id=film["imdb_id"],
                   imdb_rating=float(film["imdb_rating"]),
                   imdb_votes=int(film["imdb_votes"]),
                   starttime=film["starttijd"],
                   endtime=film["eindtijd"],
                   channel=film["zender"],
                   movietip=film["filmtip"])