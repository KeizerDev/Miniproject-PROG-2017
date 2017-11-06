from thuisbioscoop.db.film import Film
import urllib.request

key = "b2yak0qh1og2kt7v3dc7cb5mah27iurf"
baseUrl = "http://api.filmtotaal.nl/filmsoptv.xml?apikey=" + key


fullUrl = baseUrl + "&dag=07-11-2017&sorteer=0"

response = urllib.request.urlopen(fullUrl).read()

import xmltodict

doc = xmltodict.parse(response)

for film in doc['filmsoptv']['film']:
	# print(film["ft_link"])
	for keys, values in film.items():
		print(keys, values)
newFilm = Film(ft_link = film["ft_link"])