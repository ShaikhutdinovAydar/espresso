import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QTableWidgetItem
from ui_1 import Ui_Form
import csv


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loadTable('Data.csv')

    def loadTable(self):
        
        self.tableWidget.setColumnCount(len(title))
        self.tableWidget.setHorizontalHeaderLabels(title)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(reader):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(elem))
        self.tableWidget.resizeColumnsToContents()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())