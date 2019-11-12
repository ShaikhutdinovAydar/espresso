import sys
import random
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.c = 0
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
        r = random.randint(0, 300)
        x = random.randint(0, 500)
        y = random.randint(0, 500)
        r_1 = random.randint(0, 300)
        x_1 = random.randint(0, 500)
        y_1 = random.randint(0, 500)
        self.qp.setBrush(QColor(255, 255, 0))
        self.qp.drawEllipse(x, y, r, r)
        self.qp.drawEllipse(x_1, y_1, r_1, r_1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())