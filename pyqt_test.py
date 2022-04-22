from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QWidget, QPushButton
import sys
from main import *


# def application():
#     app = QApplication(sys.argv)
#     app.setWindowIcon(QtGui.QIcon('icon.png'))
#     window = QMainWindow()
#     menu_bar = window.menuBar()
#     option = menu_bar.addMenu('File')
#     option.addAction('New note')
#     option.addAction('Edit note')
#     option.addAction('Delete note')
#
#     window.setWindowTitle("Notes App")
#     window.setGeometry(1000, 150, 300, 400)
#
#     window.show()
#     sys.exit(app.exec_())
#
#
# if __name__ == '__main__':
#     application()

class App(QWidget):
    def __init__(self):
        self.ui = None
        self.start()

    def start(self):
        self.ui = uic.loadUi('notewidget_test.ui')
        self.ui.show()
        self.set()

    def set(self):
        self.ui.btn1.clicked.connect(lambda: NewNote(number_of_note=1))
        self.ui.btn2.clicked.connect(lambda: self.check(btn=self.ui.btn2))
        self.ui.btn3.clicked.connect(lambda: DeleteNote())

    def check(self, btn):
        print('Clicked button', btn)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    notes = App()
    app.exec_()
    # sys.exit(app.exec_())
