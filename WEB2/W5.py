import os
import sys

import requests
from dotenv import load_dotenv
import pygame

load_dotenv('jes.env')
api_key = os.getenv('KEY_ACCESS')

map_img = 'map.png'
url = 'https://static-maps.yandex.ru/v1?'
url_2 = 'http://geocode-maps.yandex.ru/1.x/'
geocode = 'Финк'
key_api = os.getenv('API_KEY')

rr = f'{url_2}?apikey={key_api}&geocode={geocode}&format=json'
request_1 = requests.get(rr)
js = request_1.json()
target_pos = js['response']['GeoObjectCollection']['featureMember'][0]['GeoObject'] \
    ['Point']['pos'].split(' ')

req = f'{url}apikey={api_key}&ll={target_pos[0]},{target_pos[1]}&spn=20,20&theme=dark&z=21'
request_1 = requests.get(req)

with open(map_img, 'wb') as f:
    f.write(request_1.content)
    f.close()

img = pygame.image.load(map_img)
screen = pygame.display.set_mode(img.get_size())
screen.blit(img, (0, 0))
pygame.display.flip()

while pygame.event.wait().type != pygame.QUIT:
    pass

pygame.quit()
pygame.display.quit()
os.remove(map_img)
sys.exit()
