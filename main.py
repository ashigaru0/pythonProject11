import sys

import requests
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)  # Загружаем дизайн
        self.getImage()
        self.initUI()

    def getImage(self):
        map_request = f"http://static-maps.yandex.ru/1.x/?ll={37.530887},{55.703118}&spn=0.002,0.002&l=map"
        response = requests.get(map_request)

        if not response:
            print("Ошибка выполнения запроса:")
            print(map_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)

        # Запишем полученное изображение в файл.
        self.map_file = "map.png"
        with open(self.map_file, "wb") as file:
            file.write(response.content)

    def initUI(self):
        self.lineEdit.

        self.setWindowTitle('Отображение карты')
        self.map_image = QPixmap(self.map_file).scaledToWidth(769)
        self.label.setPixmap(self.map_image)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())