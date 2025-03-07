import os
import sys
import requests

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QLineEdit
from dotenv import load_dotenv


from WEB4.cords_in import grad

load_dotenv('keys.env')
WIDTH, HEIGHT = (800, 600)
GEOCODER_API = os.getenv('GEOCODER_KEY')
STATIC_API = os.getenv('STATIC_API')
URL_STATIC = 'https://static-maps.yandex.ru/1.x/'
URL_GEOCODER = 'https://geocode-maps.yandex.ru/1.x'


class Map_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, WIDTH, HEIGHT)
        self.setWindowTitle('Yandex Maps')

        self.latitude = QLabel('latitude: ', self)
        self.latitude.move(WIDTH // 2 - 200, 20)

        self.latitude_input = QLineEdit(self)
        self.latitude_input.move(self.latitude.x() + 60, self.latitude.y())
        self.latitude_input.resize(100, 23)

        self.longitude = QLabel('longitude: ', self)
        self.longitude.move(self.latitude_input.x() + self.latitude_input.width() + 20, self.latitude.y())

        self.longitude_input = QLineEdit(self)
        self.longitude_input.move(self.longitude.x() + 70, self.longitude.y())
        self.longitude_input.resize(100, 23)

        self.get_map_btn = QPushButton('Enter', self)
        self.get_map_btn.move(self.longitude_input.x() + self.longitude_input.width() + 20,
                              self.longitude_input.y())
        self.get_map_btn.clicked.connect(self.get_map)

        self.map_img_lab = QLabel(self)
        self.map_img_lab.move(0, self.longitude_input.y() + self.longitude_input.height() + 20)
        self.map_img_lab.resize(WIDTH, HEIGHT - 100)  # Adjust size to fit window

    def get_map(self):
        lat = self.latitude_input.text()
        lon = self.longitude_input.text()

        try:
            lat_float = float(lat)
            lon_float = float(lon)
        except ValueError:
            print("Invalid coordinates. Please enter numeric values.")
            return

        spf = grad((lat_float, lon_float), GEOCODER_API)

        req = f"{URL_STATIC}?apikey={STATIC_API}&ll={lon_float},{lat_float}&z=10&l=map&spn={spf[0]},{spf[1]}&z=21&theme=dark"
        response = requests.get(req)

        if response.status_code == 200:
            pixmap = QPixmap()
            pixmap.loadFromData(response.content)
            self.map_img_lab.setPixmap(pixmap)
            self.map_img_lab.resize(pixmap.width(), pixmap.height())
        else:
            print(f"Failed to retrieve map. HTTP Status Code: {response.status_code}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Map_Window()
    window.show()
    sys.exit(app.exec())
