import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class runningButton(QWidget):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)
        self.x = 100
        self.y = 50
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 800, 800)
        self.setWindowTitle('Убегающая кнопка')
        self.a = QPushButton(self)
        self.a.setText('Не догонишь')
        self.a.resize(200, 100)
        self.a.move(self.x, self.y)

    def mouseMoveEvent(self, event):
        x1, y1 = event.x(), event.y()
        if abs(x1 - self.x - 200) < 30:
            self.x = self.x - 10
            if y1 - self.y - 100 < 0:
                self.y = self.y + 10
            else:
                self.y = self.y - 10
        elif abs(x1 - self.x) < 30:
            self.x = self.x + 10
            if y1 - self.y - 100 < 0:
                self.y = self.y + 10
            else:
                self.y = self.y - 10
        if abs(y1 - self.y - 200) < 30:
            self.y = self.y - 10
            if x1 - self.x - 100 < 0:
                self.x = self.x + 10
            else:
                self.x = self.x - 10
        elif abs(y1 - self.y) < 30:
            self.y = self.y + 10
            if x1 - self.x - 100 < 0:
                self.x = self.x + 10
            else:
                self.x = self.x - 10
        if self.x <= 0:
            self.x = abs(x1 - 10)
        if self.x >= 600:
            self.x = abs(x1 - 600)
        if self.y <= 0:
            self.y = abs(y1 - 10)
        if self.y >= 700:
            self.y = abs(y1 - 700)
        self.a.move(self.x, self.y)


app = QApplication(sys.argv)
ex = runningButton()
ex.show()
sys.exit(app.exec_())
