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
key_api = os.getenv('API_KEY')


def get_cords(geocode):
    rr = f'{url_2}?apikey={key_api}&geocode={geocode}&format=json'
    request_1 = requests.get(rr)
    js = request_1.json()
    print(js)
    target_pos = js['response']['GeoObjectCollection']['featureMember'][0]['GeoObject'] \
        ['Point']['pos'].split(' ')
    return target_pos


target_pos = get_cords('Москва')
stadion_cords1 = get_cords('Волоколамское ш., 69, Москва')
stadion_cords2 = get_cords('Ленинградский просп., 36, Москва')
stadion_cords3 = get_cords('ул. Лужники, 24, стр. 1, Москва')

req = f"{url}apikey={api_key}&ll={target_pos[0]},{target_pos[1]}&spn=0.1,0.1&theme=dark&pt={stadion_cords1[0]},{stadion_cords1[1]}~" \
    f'{stadion_cords2[0]},{stadion_cords2[1]}'
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
