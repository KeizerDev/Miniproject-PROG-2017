import datetime
import hashlib
import os
import re
import urllib.request

DOWNLOAD_LOCATION = "data/images/%s.jpg"


def download_image(url, imdb_id):
	"""functie voor het downloaden van de film foto's"""
    store_location = DOWNLOAD_LOCATION % imdb_id

    if not os.path.isfile(store_location):
        response = urllib.request.urlopen(url).read()
        new_image = open(store_location, 'wb')
        new_image.write(response)
        new_image.close()


def get_image_path(imdb_id):
	"""functie voor het download image path"""
    return DOWNLOAD_LOCATION % imdb_id


def ft_url_builder(key, date):
	"""functie voor het url bouwen voor de filmtotaal API"""
    return "http://api.filmtotaal.nl/filmsoptv.xml?apikey=%s&dag=%s&sorteer=0" % (key, date)


def text_to_md5(my_string):
	"""functie die strings hashed naar md5"""
    m = hashlib.md5()
    m.update(my_string.encode('utf-8'))
    return m.hexdigest()


def generate_unique_code(str):
	"""functie die een unieke code genereert"""
    return text_to_md5(str)[0:7]


def get_current_date():
	"""functie die de huidigge datum teruggeeft in format 01-01-2017"""
    return datetime.datetime.now().strftime('%d-%m-%Y')


def get_timestamp():
	"""functie die 2 timestamps geeft van nu en nu + 24 uur"""
    ts_today = datetime.datetime.now()
    ts_tomorrow = ts_today + datetime.timedelta(days=1)

    return {
        "today": int(ts_today.timestamp()),
        "tomorrow": int(ts_tomorrow.timestamp())
    }
