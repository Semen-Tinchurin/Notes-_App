from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QMessageBox, qApp, QAbstractItemView
import sys
import os


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.path = 'Notes'
        self.NOTE = 'Note '
        self.ui = None
        self.notes_list = None
        self.model = QtGui.QStandardItemModel(self)
        qApp.setStyleSheet("QMessageBox{background-color:rgb(255, 245, 124);}")
        self.start()

    def start(self):
        self.ui = uic.loadUi('notewidget.ui')
        self.ui.show()
        self.set()
        self.setuplistveiw()

    # set up ListView widget
    def setuplistveiw(self):
        self.model.clear()
        self.notes_list = sorted(os.listdir(self.path), key=lambda name: len(name))
        for note in self.notes_list:
            item = QtGui.QStandardItem(note)
            item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            item.setData(note)
            self.model.appendRow(item)
        self.ui.listView.setModel(self.model)
        self.ui.listView.setMouseTracking(True)

    # set up buttons
    def set(self):
        self.ui.btn1.clicked.connect(lambda: self.NewNote())
        self.ui.btn2.clicked.connect(lambda: self.EditNote())
        self.ui.btn3.clicked.connect(lambda: self.DeleteNote())
        self.ui.listView.clicked.connect(lambda: self.item_clicked())
        self.ui.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def create_messagebox(self, text):
        messagebox = QMessageBox()
        messagebox.setText(text)
        messagebox.setWindowTitle('Error')
        messagebox.setWindowIcon(QIcon('icons/warning.png'))
        messagebox.setStandardButtons(QMessageBox.Ok)
        messagebox.exec_()

    # get name of selected note
    @QtCore.pyqtSlot()
    def item_clicked(self):
        index = self.ui.listView.selectionModel().currentIndex()
        file_name = index.data()
        with open(f"Notes/{file_name}", 'r', encoding='utf-8') as file:
            self.ui.textEdit.setPlainText(file.read())
        return file_name

    # creating a new note
    def NewNote(self):
        if self.ui.textEdit.toPlainText() != '':
            index = 1
            file_name = f'{self.NOTE}{index}.txt'
            text = self.ui.textEdit.toPlainText()
            for f_name in os.listdir(self.path):
                if f_name == file_name or file_name in os.listdir(self.path):
                    index += 1
                    file_name = f'{self.NOTE}{index}.txt'
            with open(f'Notes/{file_name}', 'w', encoding='utf-8') as file:
                file.write(text)

            # update list of notes in ListView widget
            item = QtGui.QStandardItem(file_name)
            item.setData(file_name)
            self.model.appendRow(item)
            self.ui.textEdit.clear()
        else:
            self.create_messagebox(text='Empty note')

    # edit an existing note
    def EditNote(self):
        try:
            new_text = self.ui.textEdit.toPlainText()
            with open(f'Notes/{self.item_clicked()}', 'w', encoding='utf-8') as file:
                file.write(new_text)
            self.setuplistveiw()
            self.ui.textEdit.clear()
        except:
            self.create_messagebox(text='Select a note')

    # delete existing note
    def DeleteNote(self):
        try:
            choice = self.item_clicked()
            os.remove(f'{self.path}/{choice}')
            self.ui.textEdit.clear()
            self.setuplistveiw()
        except:
            self.create_messagebox(text='Select a note')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    notes = App()
    app.exec_()
    # sys.exit(app.exec_())
