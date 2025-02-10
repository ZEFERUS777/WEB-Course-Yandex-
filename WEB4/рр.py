import os
from dotenv import load_dotenv

import requests
import json

from WEB1.W2 import print_structure
from WEB2.H1 import geocode

load_dotenv('api.env')

API_KEY = os.getenv('GEOCODER_KEY')
static_keu = os.getenv('STATIC_API')
print(API_KEY)

geocodeer_url = 'https://geocode-maps.yandex.ru/1.x/'
geo = 'Москва'


query = f'{geocodeer_url}?apikey={API_KEY}&geocode={geo}&format=json'
