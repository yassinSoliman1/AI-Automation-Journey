import json
def show_menuu():
    print('''
===== Student Manager =====

1. Add Student
2. View Students
3. Exit''')

def add_students(): 
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))

    new_student = {
        "name": name,
        "age": age
    }

    try:
        with open("students.json", "r") as file:
            students = json.load(file)

    except FileNotFoundError:
        students = []

    students.append(new_student)

    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

    print("Student added successfully.") 

def view_student():
    try:
        with open("students.json", "r") as file:
            students = json.load(file)

            if not students:
                print("No students yet.")
            else:
                for student in students:
                    print(f"name : { student['name'] } ")
                    print(f"age: {student['age']}")
                    print("*"*20)

    except FileNotFoundError:
        print("No students yet.")

def exit():
    print ("Thank you for using our student manger system :)")


while True:
    show_menuu()
    try:
        number = int(input("choose : ")) 
    except ValueError:
        print("Invaled chooies ")
        continue 
    if number == 1 :
        add_students()
    elif number == 2 :
        view_student()
    elif number == 3 :
        exit()
        break
    else :
        print("Invaled option")

print("THIS IS STUDENT MANAGER")        

   