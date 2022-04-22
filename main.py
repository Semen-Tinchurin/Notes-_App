import os

path = 'Notes'
NOTE = 'Note №'


# creating a new note
def NewNote(number_of_note=1):
    file_name = f'{NOTE} {number_of_note}.txt'
    text = input('Enter a note: ')
    if file_name in os.listdir(path):
        file_name = f"{NOTE} {number_of_note + len(os.listdir(path))}.txt"
    with open(f'Notes/{file_name}', 'w', encoding='utf-8') as file:
        file.write(text)


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
    print('Created notes:')
    for item in list_of_notes:
        print(item)
    return list_of_notes


# delete existing note
def DeleteNote():
    choice = input('Enter a number of note to delete this note: ')
    os.remove(f'{path}/{NOTE} {choice}.txt')
    ListOfNotes()
