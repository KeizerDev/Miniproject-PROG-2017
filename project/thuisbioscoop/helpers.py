import hashlib


def ft_url_builder(key, date):
    return "http://api.filmtotaal.nl/filmsoptv.xml?apikey=%s&dag=%s&sorteer=0" % (key, date)


def text_to_md5(my_string):
    m = hashlib.md5()
    m.update(my_string.encode('utf-8'))
    return m.hexdigest()


def generate_unique_code(str):
    return text_to_md5(str)[0:7]

print(generate_unique_code("reoas"))