from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtWidgets import QWidget
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
        super().__init__()
        self.ui = None
        self.notes_list = ListOfNotes()
        self.model = QtGui.QStandardItemModel(self)
        self.start()

    def start(self):
        self.ui = uic.loadUi('notewidget_test.ui')
        self.ui.show()
        self.set()
        self.setuplistveiw()

    def setuplistveiw(self):
        for note in self.notes_list:
            item = QtGui.QStandardItem(note)
            item.setData(note)
            self.model.appendRow(item)
        self.ui.listView.setModel(self.model)
        self.ui.listView.setMouseTracking(True)

    def set(self):
        self.ui.btn1.clicked.connect(lambda: self.NewNote(number_of_note=1))
        # self.ui.btn2.clicked.connect(lambda: self.check(btn=self.ui.btn2))
        self.ui.btn3.clicked.connect(lambda: self.DeleteNote())
        self.ui.listView.clicked.connect(lambda: self.item_clicked())

    # получил имя выбранного файла и его содержимое
    @QtCore.pyqtSlot()
    def item_clicked(self):
        index = self.ui.listView.selectionModel().currentIndex()
        file_name = index.data()
        print(file_name)
        with open(f"Notes/{file_name}", 'r', encoding='utf-8') as file:
            file = file.read()
            print(file)

    # creating a new note
    def NewNote(self, number_of_note=1):
        file_name = f'{NOTE} {number_of_note}.txt'
        text = self.ui.textEdit.toPlainText()
        if file_name in os.listdir(path):
            file_name = f"{NOTE} {number_of_note + len(os.listdir(path))}.txt"
        with open(f'Notes/{file_name}', 'w', encoding='utf-8') as file:
            file.write(text)

        # update list of notes in ListView widget
        item = QtGui.QStandardItem(file_name)
        item.setData(file_name)
        self.model.appendRow(item)

    # delete existing note
    def DeleteNote(self):
        choice = input('Enter a number of note to delete this note: ')
        os.remove(f'{path}/{NOTE} {choice}.txt')
        ListOfNotes()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    notes = App()
    app.exec_()
    # sys.exit(app.exec_())
