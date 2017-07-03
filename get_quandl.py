

import urllib.request as ur
import json

def get_price(symbol, ur=ur):
    url = "https://www.quandl.com/api/v3/datasets/NSE"
    key = "yLjZiVk6gxEvZwWiWTaP"
    u = ur.urlopen("{}/{}.json?api_key={}&limit=1".format(url,symbol,key))
    data = u.read()
    json_data = json.loads(data.decode("utf8"))
    return json_data

