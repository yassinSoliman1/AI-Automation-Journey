
def show_menuu():
    print('''
===== NOTES =====

1. Add Note
2. View Notes
3. Exit''')

def add_note():
    note = input("Enter your note: ")

    with open("note book/notes.txt", "a") as file:
        file.write(note + "\n")

    print("Note added successfully.") 

def view_notes():
    try:
        with open("note book/notes.txt", "r") as file:
            notes = file.read()

            if not notes:
                print("No notes yet.")
            else:
                print(notes)

    except FileNotFoundError:
        print("No notes yet.")

def exit():
    print ("Thank you for using our note book")


while True:
    show_menuu()
    try:
        number = int(input("choose : ")) 
    except ValueError:
        print("Invaled chooies ")
        continue 
    if number == 1 :
        add_note()
    elif number == 2 :
        view_notes()
    elif number == 3 :
        exit()
        break
    else :
        print("Invaled option")

   