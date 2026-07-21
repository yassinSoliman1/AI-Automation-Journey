def show_menu() :
    print('''
===== CONTACT BOOK =====

1. Add Contact
2. View Contacts
3. Search Contact
4. Delete Contact
5. Exit
''')

def add_contact (contact_list,name , number):
    contact = {
        "name" : name,
        "number" : number 
    }
    contact_list.append(contact)

def view_contact(contact_list) :
    for index,contact in enumerate(contact_list,start=1):
        print (f"{index} . {contact["name"]} - {contact["number"]}")

def search_contact(contact_list,name):
    for contact in contact_list:
        if contact["name"].lower() == name.lower():
            print("Contact Found")
            print(f"Name : {contact['name']}")
            print(f"Phone : {contact['number']}")

def delete_conatct(contact_list,name):
     for contact in contact_list:
        if contact["name"].lower() == name.lower():
            contact_list.remove(contact)
            print("Contact Deleted Successfully")

def Exit():
    print("see you next time :)")
    
contact_list = []
while True :
    show_menu()
    choose=int(input("Choose = "))
    if choose == 1 :
        name = input("Enter the name : ")
        number = input("Enter the number : ")
        add_contact(contact_list,name,number)
    elif choose == 2 :
        if not contact_list :
            print("No contact value ")
        else :
            view_contact(contact_list)
    elif choose == 3 :
        name = input("Enter the contact name : ")
        if not contact_list :
             print("No contact value ")
        else :
            search_contact(contact_list,name)
    elif choose == 4 :
        name = input("Enter the contact name you want to delete : ")
        if not contact_list :
             print("No contact value ")
        else :
            delete_conatct(contact_list,name)
    elif choose == 5 :
        Exit() 
        break
    else :
        print("Invaled option ")