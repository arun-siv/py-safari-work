#'http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop=14787&route=22'

import urllib.request
from xml.etree.ElementTree import XML

url = 'http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop=14787&route=22'

u = urllib.request.urlopen(url)
data = u.read()

xml_data = XML(data)

for pt in xml_data.findall('.//pt'):
    print(pt.text)