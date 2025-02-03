import requests
import os
from dotenv import load_dotenv


load_dotenv(dotenv_path='jes.env')

# Получаем API-ключ
api_key = os.getenv("API_KEY")




url = 'http://geocode-maps.yandex.ru/1.x/?'



for location in ['Барнаул', 'Мелеуз', 'Йошкар-Ола']:
    rr = f'{url}apikey={api_key}&geocode={location}&format=json'

    r = requests.get(rr)

    js = r.json()

    print(js['response']['GeoObjectCollection']['featureMember'][1]['GeoObject']['metaDataProperty']
          ['GeocoderMetaData']['Address']['Components'][2]['name'])
