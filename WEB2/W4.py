import os

import requests
from dotenv import load_dotenv

load_dotenv('jes.env')

access_key = os.getenv('API_KEY')
location = 'ул. Петровка, 38, стр. 1, Москва'
url = 'http://geocode-maps.yandex.ru/1.x/?'

req = f'{url}apikey={access_key}&format=json&geocode={location}'
request = requests.get(req)

js = request.json()

result = js['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty'] \
    ['GeocoderMetaData']['Address']['postal_code']
print(result)
