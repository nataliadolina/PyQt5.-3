import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QInputDialog


class generator(QWidget):
    def __init__(self):
        super().__init__()
        self.k = 0
        self.arr = []
        self.n = 0
        self.run()

    def initUI(self):
        self.setGeometry(300, 300, 800, 600)
        self.show()

    def run(self):
        i, okBtnPressed = QInputDialog.getInt(self, "Количество цветов", "Введите количество цветов", 1, 1, 150, 1)
        if okBtnPressed:
            self.k = i
            for j in range(self.k):
                self.run1()

    def run1(self):
        self.n += 1
        i, btn = QInputDialog.getText(self, "Цвет", "Введите цвет в формате RGB\nНапример: 0 0 255 - синий")
        if btn:
            a, b, c = i.split()
            self.arr.append((int(a), int(b), int(c)))
        if self.n == self.k:
            self.initUI()

    def drawFlag(self, qp):
        w = 100
        n = 300 // self.k
        for j in range(self.k):
            qp.setBrush(QColor(*self.arr[j]))
            qp.drawRect(100, w, 400, n)
            w += n

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawFlag(qp)
        qp.end()


app = QApplication(sys.argv)
ex = generator()
sys.exit(app.exec_())
