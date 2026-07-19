state = True
to_do_list = []
while state == True :
    
    user_info= int(input('''
===== TO-DO LIST =====

1. Add Task
2. View Tasks
3. Remove Task
4. Exit

Choose:
'''))
    if user_info == 1 :
        user_task = input(" Enter you task : ")
        to_do_list.append(user_task)
    elif user_info == 2 :
         if not to_do_list  :
             print("No task yet ")
         else :
             for index, task in enumerate(to_do_list, start=1):
              print(f"{index}. {task}") 
    elif user_info == 3:
      if not to_do_list:
        print("No task to be removed")
      else:
        for index, task in enumerate(to_do_list, start=1):
            print(f"{index}. {task}")
        task_number = int(input("Enter task number to remove: "))
        if task_number < 1 or task_number > len(to_do_list):
            print("Invalid task number.")
        else:
            removed_task = to_do_list.pop(task_number - 1)
            print(f'"{removed_task}" has been removed successfully.') 
    elif user_info == 4 :
        print ( ".... Exit  Have a good day :) ") 
        break
    else :
        print("Invaled option ")
    
