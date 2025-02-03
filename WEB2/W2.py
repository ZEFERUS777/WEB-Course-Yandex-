import requests
import requests
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='jes.env')

# Получаем API-ключ
api_key = os.getenv("API_KEY")



url = 'http://geocode-maps.yandex.ru/1.x/?'


for city in ['Хабаровск', 'Уфа', 'Нижний Новгород', 'Калининград']:

    request = requests.get(f'{url}apikey={api_key}&geocode={city}&format=json')

    if request:
        js = request.json()

        print(
            js['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty'][
                'GeocoderMetaData'][
                'Address']['Components'][1]['name'])
