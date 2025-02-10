import os
import sys
from io import BytesIO

import requests
from PIL import Image
from dotenv import load_dotenv

from cords_in import cords, grad

addf = " ".join(sys.argv[1:])
load_dotenv('api.env')
stat = os.getenv('STATIC_API')

org_key = os.getenv('ORG')

url = 'https://search-maps.yandex.ru/v1/'

url2 = 'https://static-maps.yandex.ru/v1'

x, y = cords(addf).split(' ')
address = f'{x},{y}'

search_params = {
    "apikey": org_key,
    "text": "аптека",
    "lang": "ru_RU",
    "ll": address,
    "type": "biz"
}

r = requests.get(url, params=search_params)
json_response = r.json()

organization = json_response["features"][0]

org_name = organization["properties"]["CompanyMetaData"]["name"]

org_address = organization["properties"]["CompanyMetaData"]["address"]

point = organization["geometry"]["coordinates"]
org_point = f"{point[0]},{point[1]}"

sp1, sp2 = grad(addf)
cc = f'{sp1},{sp2}'
zx, zy = cords(addf).split(' ')

r2 = requests.get(f'{url2}?apikey={stat}&ll={zx},{zy}&pt={org_point},vkbkm&spn={cc}&theme=dark')
im = BytesIO(r2.content)
opened_img = Image.open(im)
opened_img.show()
