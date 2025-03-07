import os

import requests
from dotenv import load_dotenv



def grad(loc, GEOCODER_API_KEY: str):
    if type(loc) == str:
        geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
        response = requests.get(geocoder_api_server, params={
            'apikey': GEOCODER_API_KEY,
            'geocode': loc,
            'format': 'json'
        })

        json_response = response.json()

        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]

        # Получаем координаты охватывающего прямоугольника
        envelope = toponym['boundedBy']['Envelope']
        lower_corner = list(map(float, envelope['lowerCorner'].split()))
        upper_corner = list(map(float, envelope['upperCorner'].split()))
        delta_lon_deg = upper_corner[0] - lower_corner[0]
        delta_lat_deg = upper_corner[1] - lower_corner[1]

        return delta_lon_deg, delta_lat_deg
    else:
        cor = str(loc).replace('(', '').replace(')', '').split(',')
        geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
        response = requests.get(geocoder_api_server, params={
            'apikey': GEOCODER_API_KEY,
            'geocode': f'{cor[0]},{cor[1]}',
            'format': 'json'
        })

        json_response = response.json()

        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]

        # Получаем координаты охватывающего прямоугольника
        envelope = toponym['boundedBy']['Envelope']
        lower_corner = list(map(float, envelope['lowerCorner'].split()))
        upper_corner = list(map(float, envelope['upperCorner'].split()))
        delta_lon_deg = upper_corner[0] - lower_corner[0]
        delta_lat_deg = upper_corner[1] - lower_corner[1]

        return delta_lon_deg, delta_lat_deg

def cords(loc: str, GEOCODER_API_KEY: str):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
    response = requests.get(geocoder_api_server, params={
        'apikey': GEOCODER_API_KEY,
        'geocode': loc,
        'format': 'json'
    })

    json_response = response.json()

    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]

    x, y = toponym['Point']['pos'].split()

    return x,y

