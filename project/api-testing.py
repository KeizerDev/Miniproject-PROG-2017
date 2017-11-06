key = "b2yak0qh1og2kt7v3dc7cb5mah27iurf"
baseUrl = "http://api.filmtotaal.nl/filmsoptv.xml?apikey=" + key


fullUrl = baseUrl + "&dag=07-11-2017&sorteer=0"

import urllib.request

response = urllib.request.urlopen(fullUrl).read()

import xml.etree.ElementTree as ET
tree = ET.fromstring(response)

for child in tree:
	print(" --------------- " + child.tag, child[1].text)
	for childTag in child:
		print(" -- " + childTag.tag, childTag.text)