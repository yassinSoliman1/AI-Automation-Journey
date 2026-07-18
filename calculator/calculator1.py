print("======CALCULATOR======")
number1 = float(input("enter the first number : "))

oprator = input('''
      *
      +
      /
      -
    choose an operator: ''')

number2 = float(input(" enter the second number : "))

if oprator == '/' and number2 == 0:
    print("a7a eh el enta ktbo dah ")
elif oprator == '*' :
    print(number1*number2)
elif oprator == '+':
    print(number1+number2) 
elif oprator == '/':
    print(number1/number2)
elif oprator == '-':
    print(number1-number2) 
else :
    print("eh ybnel mara el enta ktbo dah")   

other_calc = input(" do you want other calculations ? : [T/N]")   
while other_calc == 't' :
    number1 = float(input("enter the first number : "))

    oprator = input('''
      *
      +
      /
      -
    choose an operator: ''')

    number2 = float(input(" enter the second number : "))

    if oprator == '/' and number2 == 0:
      print("a7a eh el enta ktbo dah ")
    elif oprator == '*' :
        print(number1*number2)
    elif oprator == '+':
        print(number1+number2) 
    elif oprator == '/':
        print(number1/number2)
    elif oprator == '-':
        print(number1-number2) 
    else :
        print("eh ybnel mara el enta ktbo dah")   
    other_calc = input("Do you want another calculation? [T/N]: ")    

else : 
    print("etl3 bara ya ebn el mara ")
