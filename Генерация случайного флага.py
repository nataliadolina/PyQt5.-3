import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtWidgets import QInputDialog
from random import choice


class generator(QWidget):
    def __init__(self):
        super().__init__()
        self.k = 0
        self.run()

    def initUI(self):
        self.setGeometry(300, 300, 800, 600)
        self.show()

    def run(self):
        i, okBtnPressed = QInputDialog.getInt(self, "Количество цветов", "Введите количество цветов", 1, 1, 250, 1)
        if okBtnPressed:
            self.k = i
            self.initUI()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawFlag(qp)
        qp.end()

    def drawFlag(self, qp):
        arr1 = []
        arr2 = []
        arr3 = []
        n = 300 // self.k
        w = 100
        for j in range(self.k):
            r = choice(range(1, 256))
            arr1.append(r)
            r = choice(range(1, 256))
            arr2.append(r)
            r = choice(range(1, 256))
            arr3.append(r)
        for j in range(self.k):
            qp.setBrush(QColor(arr1[j], arr2[j], arr3[j]))
            qp.drawRect(100, w, 400, n)
            w += n


app = QApplication(sys.argv)
ex = generator()
sys.exit(app.exec_())
