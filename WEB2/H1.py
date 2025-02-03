import requests
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='jes.env')

# Получаем API-ключ
api_key = os.getenv("API_KEY")


url = 'http://geocode-maps.yandex.ru/1.x/?'
geocode = 'Красная площадь, 1, Москва, 125009'

request = requests.get(f'{url}apikey={api_key}&geocode={geocode}&format=json')

if request:
    js = request.json()

    toponym = js['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
    address = toponym['metaDataProperty']['GeocoderMetaData']['text']

    toponym_cords = toponym['Point']['pos']

    print(f'address: {address}, cords: {toponym_cords}')
