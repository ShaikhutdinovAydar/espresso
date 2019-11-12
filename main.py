import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        # Подключение к БД
        con = sqlite3.connect("coffee.sqlite")
        # Создание курсора
        cur = con.cursor()
        # Выполнение запроса и получение всех результатов
        self.result = cur.execute("SELECT * FROM coffees").fetchall()
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(
            ["id", "title", "degree of roasting", "ground in grains", "the description of the taste", "cost",
             "the amount of taste"])
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(self.result):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.resizeColumnsToContents()
        con.commit()
        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
