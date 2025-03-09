import os
import sys

import requests
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QKeyEvent
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QLineEdit, QStatusBar
from dotenv import load_dotenv

from WEB4.cords_in import grad

load_dotenv('keys.env')
WIDTH, HEIGHT = (650, 550)
GEOCODER_API = os.getenv('GEOCODER_KEY')
STATIC_API = os.getenv('STATIC_API')
URL_STATIC = 'https://static-maps.yandex.ru/1.x/'
URL_GEOCODER = 'https://geocode-maps.yandex.ru/1.x'


class Map_Window(QMainWindow):
    def __init__(self):
        """inited window menu"""
        super().__init__()
        self.setGeometry(500, 300, WIDTH, HEIGHT)
        self.setWindowTitle('Yandex Maps')

        """широта"""
        self.latitude = QLabel('latitude: ', self)
        self.latitude.move(WIDTH // 2 - 200, 20)

        """широта ввод"""
        self.latitude_input = QLineEdit(self)
        self.latitude_input.setGeometry(self.latitude.x() + 60, self.latitude.y(), 100, 23)  # задаю размер и позицию

        """долгота"""
        self.longitude = QLabel('longitude: ', self)
        self.longitude.move(self.latitude_input.x() + self.latitude_input.width() + 20, self.latitude.y())

        """долгота ввод"""
        self.longitude_input = QLineEdit(self)
        self.longitude_input.setGeometry(self.longitude.x() + 70, self.longitude.y(), 100, 23)  # задаю размер и позицию

        """кнопка получения карты и обработчик при нажатии"""
        self.get_map_btn = QPushButton('Enter', self)
        self.get_map_btn.move(self.longitude_input.x() + self.longitude_input.width() + 20,
                              self.longitude_input.y())
        self.get_map_btn.clicked.connect(self.get_map)

        """карта"""
        self.map_img_lab = QLabel(self)
        self.map_img_lab.move(10, self.longitude_input.y() + self.longitude_input.height() + 20)
        self.map_img_lab.resize(WIDTH, HEIGHT - 100)

        """масштаб карты"""
        self.scale = 0.1

        self.status = QStatusBar(self, visible=True)
        self.setStatusBar(self.status)

    def get_map(self):
        lat = self.latitude_input.text()  # получение текста из поля широты
        lon = self.longitude_input.text()  # получение текста из поля долготы

        """обработчик ошибки при вводе неверных значений"""
        try:
            lat_float = float(lat)
            lon_float = float(lon)
        except ValueError:
            print("Invalid coordinates. Please enter numeric values.")
            return

        spf = grad((lat_float, lon_float), GEOCODER_API)

        req = f"{URL_STATIC}?apikey={STATIC_API}&ll={lon_float},{lat_float}&z=10&l=map&spn={self.scale},{self.scale}&z=21&theme=dark"
        response = requests.get(req)

        if response.status_code == 200:
            pixmap = QPixmap()
            pixmap.loadFromData(response.content)
            self.map_img_lab.setPixmap(pixmap)
            self.map_img_lab.resize(pixmap.width(), pixmap.height())
            print('successfully! ', self.scale)
            self.status.showMessage(f'successfully!  {self.scale}')
        else:
            print(f"Failed to retrieve map. HTTP Status Code: {response.status_code}")

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key.Key_PageUp and self.scale <= 0.8:
            self.scale *= 1.5
        elif event.key() == Qt.Key.Key_PageDown and self.scale > 0.0011561019943888407:
            self.scale /= 1.5
        self.get_map()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Map_Window()
    window.show()
    sys.exit(app.exec())
