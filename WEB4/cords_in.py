import requests
from dotenv import load_dotenv


def grad(loc: str):
    load_dotenv('api.env')
    GEOCODER_API_KEY = 'ENTER KEY'

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
