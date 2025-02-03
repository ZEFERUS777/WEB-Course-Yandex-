import requests

url = 'http://geocode-maps.yandex.ru/1.x/?'
api_key = '40d1649f-0493-4b70-98ba-98533de7710b'
geocode = 'Красная площадь, 1, Москва, 125009'

request = requests.get(f'{url}apikey={api_key}&geocode={geocode}&format=json')

if request:
    js = request.json()

    toponym = js['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
    address = toponym['metaDataProperty']['GeocoderMetaData']['text']

    toponym_cords = toponym['Point']['pos']

    print(f'address: {address}, cords: {toponym_cords}')
