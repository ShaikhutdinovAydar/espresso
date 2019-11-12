import sys
import random
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.c = 0
        self.setGeometry(0, 0, 600, 600)
        self.setWindowTitle('Git и желтые окружности')
        self.btn = QPushButton('Создать', self)
        self.btn.clicked.connect(self.up)

    def up(self):
        self.c = 1
        self.update()

    def paintEvent(self, event):
        if self.c != 0:
            self.qp = QPainter()
            self.qp.begin(self)
            self.create_cyrcle()
            self.qp.end()

    def create_cyrcle(self):
        for i in range(10):
            rad = random.randint(0, 300)
            x = random.randint(0, 500)
            y = random.randint(0, 500)
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            self.qp.setBrush(QColor(r, g, b))
            self.qp.drawEllipse(x, y, rad, rad)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
