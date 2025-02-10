import os
import sys
import math
from io import BytesIO
import requests
from PIL import Image
import json
from dotenv import load_dotenv

from cords_in import grad

os.chdir(os.path.dirname(os.path.abspath(__file__)))

load_dotenv('api.env')

# Получаем параметры из переменных окружения
GEOCODER_API_KEY = 'ENTER KEY'
STATIC_MAPS_API_KEY = 'ENTER KEY'

# Формируем запрос к геокодеру
toponym_to_find = " ".join(sys.argv[1:])

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
response = requests.get(geocoder_api_server, params={
    'apikey': GEOCODER_API_KEY,
    'geocode': toponym_to_find,
    'format': 'json'
})

if not response.ok:
    print("Ошибка выполнения запроса:")
    print(response.text)
    sys.exit(1)

# Сохраняем JSON-ответ для отладки
json_response = response.json()
with open('res.json', 'w', encoding='utf-8') as f:
    json.dump(json_response, f, ensure_ascii=False, indent=4)

# Извлекаем топоним
toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]

# Получаем координаты центра
toponym_coordinates = toponym["Point"]["pos"]
toponym_longitude, toponym_latitude = toponym_coordinates.split(" ")


delta_lon_deg, delta_lat_deg = grad(toponym_to_find)
# Формируем параметры для карты
map_params = {
    "ll": f"{toponym_longitude},{toponym_latitude}",
    "spn": f"{delta_lon_deg},{delta_lat_deg}",
    "l": "map",
    "apikey": STATIC_MAPS_API_KEY
}

# Запрашиваем карту
map_api_server = "https://static-maps.yandex.ru/v1"
response = requests.get(map_api_server, params=map_params)

# Показываем карту
if response.ok:
    Image.open(BytesIO(response.content)).show()
else:
    print("Ошибка при получении карты:")
    print(response.text)