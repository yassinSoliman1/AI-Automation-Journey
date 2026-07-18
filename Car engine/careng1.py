car_game = input(">")
stat = True
while stat is True :
    if car_game == "help" :
        print( '''    start -- to start the car 
    stop -- to stop the car
    quit -- to exit  ''')
    elif car_game == "start":
        print("car is starting .... Ready to goooo!!!!")
    elif car_game == "stop" :
        print("car stoped .")
    elif car_game== "quit" :
       
        print("thank you for trying our engine :)")
        break
    else :
        print(" i can't understand you ")
    car_game = input(">")        
    