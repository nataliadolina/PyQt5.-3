import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from random import choice


class car(QWidget):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)
        self.name = 'car.png'
        self.x = -10
        self.y = 0
        self.arr = ['car.png', 'car1.png', 'car2.png', 'car3.png']
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 800, 800)
        self.setWindowTitle('Машинка')
        self.pixmap = QPixmap(self.name).scaled(200, 100)
        self.lbl_picture = QLabel(self)
        self.lbl_picture.move(self.x, self.y)
        self.lbl_picture.setPixmap(self.pixmap)
        self.lbl_picture.resize(200, 100)

    def mouseMoveEvent(self, event):
        self.x, self.y = event.x(), event.y()
        if self.x <= 0:
            self.x = 10
        if self.x >= 600:
            self.x = 600
        if self.y <= 0:
            self.y = 10
        if self.y >= 700:
            self.y = 700

        self.lbl_picture.move(self.x, self.y)
        self.lbl_picture.setPixmap(self.pixmap)

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Space:
            i = self.arr.index(self.name)
            self.name = choice(self.arr)
            while self.arr.index(self.name) == i:
                self.name = choice(self.arr)
            self.pixmap = QPixmap(self.name).scaled(200, 100)
            self.lbl_picture.setPixmap(self.pixmap)


app = QApplication(sys.argv)
ex = car()
ex.show()
sys.exit(app.exec_())
