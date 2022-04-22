import os

path = 'Notes'
NOTE = 'Note №'


# editing an existing note
def EditNote():
    list_of_notes = ListOfNotes()
    note_for_editing = int(input('Enter number of note: ')) - 1
    with open(f"Notes/{list_of_notes[note_for_editing]}", encoding='utf-8') as file:
        text = file.read()
        print("Content of note: \n", text)
        new_text = input(f"New content: ")
        with open(f"Notes/{list_of_notes[note_for_editing]}", 'w', encoding='utf-8') as newfile:
            newfile.write(new_text)


# get a list of existing notes
def ListOfNotes():
    list_of_notes = os.listdir(path)
    return list_of_notes




# NewNote()
