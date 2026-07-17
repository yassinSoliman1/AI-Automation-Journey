print("hello ento Guess game guess the secret number to win choose from 1 to 10")
secret_number = 9
number_of_trys = 3
guess_count = 0
while guess_count < number_of_trys :
    guess_count+=1
    user_number=int(input("Guess: "))
    if user_number == secret_number :
        print(" congratulation thats the right Number ") 
        break
else:
    print('''
Game over
          fuck you hahahaha
''')
    