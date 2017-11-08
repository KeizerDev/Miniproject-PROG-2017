import hashlib
import urllib.request
import os

DOWNLOAD_LOCATION = "data/images/%s.jpg"


def download_image(url, imdb_id):
    store_location = DOWNLOAD_LOCATION % imdb_id

    if not os.path.isfile(store_location):
        response = urllib.request.urlopen(url).read()
        new_image = open(store_location, 'wb')
        new_image.write(response)
        new_image.close()


def get_image_path(imdb_id):
    return DOWNLOAD_LOCATION % imdb_id


def ft_url_builder(key, date):
    return "http://api.filmtotaal.nl/filmsoptv.xml?apikey=%s&dag=%s&sorteer=0" % (key, date)


def text_to_md5(my_string):
    m = hashlib.md5()
    m.update(my_string.encode('utf-8'))
    return m.hexdigest()


def generate_unique_code(str):
    return text_to_md5(str)[0:7]
