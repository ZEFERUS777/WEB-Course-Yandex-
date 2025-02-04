import os
import pygame
import requests
from dotenv import load_dotenv

# Инициализация PyGame
pygame.init()

# Конфигурационные константы
ENV_FILE = 'jes.env'
MAP_IMAGE_FILE = 'map.png'
API_GEOSEARCH_URL = 'http://geocode-maps.yandex.ru/1.x/'
API_STATIC_MAPS_URL = 'https://static-maps.yandex.ru/v1'
LOCATION_NAME = 'ул. Петровка, 38, стр. 1, Москва'

def load_environment_variables():
    """Загрузить переменные окружения из файла"""
    load_dotenv(ENV_FILE)
    return {
        'api_key': os.getenv('API_KEY'),
        'map_key': os.getenv('KEY_ACCESS')
    }

def fetch_coordinates(api_key: str, location: str) -> tuple[str, str]:
    """Получить координаты для указанного адреса"""
    params = {
        'apikey': api_key,
        'geocode': location,
        'format': 'json'
    }

    response = requests.get(API_GEOSEARCH_URL, params=params)
    response.raise_for_status()

    geo_data = response.json()
    feature = geo_data['response']['GeoObjectCollection']['featureMember'][0]
    return feature['GeoObject']['Point']['pos'].split()

def download_map_image(api_key: str, longitude: str, latitude: str) -> str:
    """Загрузить статическое изображение карты"""
    map_params = {
        'll': f'{longitude},{latitude}',
        'spn': '0.002,0.002',
        'apikey': api_key,
        'theme': 'dark'
    }

    response = requests.get(API_STATIC_MAPS_URL, params=map_params)
    response.raise_for_status()

    with open(MAP_IMAGE_FILE, 'wb') as file:
        file.write(response.content)

    return MAP_IMAGE_FILE

def display_map(image_path: str):
    """Отобразить карту в окне PyGame"""
    try:
        image = pygame.image.load(image_path)

        screen = pygame.display.set_mode(image.get_size())
        pygame.display.set_caption('Yandex Map')
        screen.blit(image, image.get_rect())
        pygame.display.flip()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False
    finally:
        pygame.quit()

def main():
    """Основная функция приложения"""
    try:
        # Инициализация окружения
        env_vars = load_environment_variables()

        # Получение координат
        longitude, latitude = fetch_coordinates(
            api_key=env_vars['api_key'],
            location=LOCATION_NAME
        )

        # Загрузка и отображение карты
        map_file = download_map_image(
            api_key=env_vars['map_key'],
            longitude=longitude,
            latitude=latitude
        )
        display_map(map_file)

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")
    except (KeyError, IndexError) as e:
        print(f"Ошибка обработки данных: {e}")
    finally:
        if os.path.exists(MAP_IMAGE_FILE):
            os.remove(MAP_IMAGE_FILE)

if __name__ == '__main__':
    main()