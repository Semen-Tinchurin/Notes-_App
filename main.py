from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtWidgets import QWidget
import sys
import os


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.path = 'Notes'
        self.NOTE = 'Note №'
        self.ui = None
        self.notes_list = None
        self.model = QtGui.QStandardItemModel(self)
        self.start()

    def start(self):
        self.ui = uic.loadUi('notewidget_test.ui')
        self.ui.show()
        self.set()
        self.setuplistveiw()

    # set up ListView widget
    def setuplistveiw(self):
        self.model.clear()
        self.notes_list = self.ListOfNotes()
        for note in self.notes_list:
            item = QtGui.QStandardItem(note)
            item.setData(note)
            self.model.appendRow(item)
        self.ui.listView.setModel(self.model)
        self.ui.listView.setMouseTracking(True)

    # set up buttons
    def set(self):
        self.ui.btn1.clicked.connect(lambda: self.NewNote(number_of_note=1))
        self.ui.btn2.clicked.connect(lambda: self.EditNote())
        self.ui.btn3.clicked.connect(lambda: self.DeleteNote())
        self.ui.listView.clicked.connect(lambda: self.item_clicked())

    # get name of selected note
    @QtCore.pyqtSlot()
    def item_clicked(self):
        index = self.ui.listView.selectionModel().currentIndex()
        file_name = index.data()
        print(file_name)
        with open(f"Notes/{file_name}", 'r', encoding='utf-8') as file:
            self.ui.textEdit.setPlainText(file.read())
        return file_name

    # creating a new note
    def NewNote(self, number_of_note=1):
        file_name = f'{self.NOTE} {number_of_note}.txt'
        text = self.ui.textEdit.toPlainText()
        if file_name in os.listdir(self.path):
            file_name = f"{self.NOTE} {number_of_note + len(os.listdir(self.path))}.txt"
        with open(f'Notes/{file_name}', 'w', encoding='utf-8') as file:
            file.write(text)

        # update list of notes in ListView widget
        item = QtGui.QStandardItem(file_name)
        item.setData(file_name)
        self.model.appendRow(item)

    # editing an existing note
    def EditNote(self):
        list_of_notes = self.ListOfNotes()
        print(list_of_notes)
        # note_for_editing = int(input('Enter number of note: ')) - 1
        # with open(f"Notes/{list_of_notes[note_for_editing]}", encoding='utf-8') as file:
        #     text = file.read()
        #     print("Content of note: \n", text)
        #     new_text = input(f"New content: ")
        #     with open(f"Notes/{list_of_notes[note_for_editing]}", 'w', encoding='utf-8') as newfile:
        #         newfile.write(new_text)

    # get an existing notes list
    def ListOfNotes(self):
        list_of_notes = os.listdir(self.path)
        return list_of_notes

    # delete existing note
    def DeleteNote(self):
        choice = self.item_clicked()
        os.remove(f'{self.path}/{choice}')
        self.setuplistveiw()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    notes = App()
    app.exec_()
    # sys.exit(app.exec_())
