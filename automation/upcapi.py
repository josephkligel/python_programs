import requests
import json

baseUrl = 'https://api.upcitemdb.com/prod/trial/lookup'
parameters = {
    'upc': '193015097490',
}
response = requests.get(baseUrl, params=parameters)

content = response.content
info = json.loads(content)
item = info['items']
title = item[0]['title']
brand = item[0]['brand']
print(title, brand, sep='\n')
