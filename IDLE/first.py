
import time

#Data types in python
num = 1 # int
fl = 1.6 #float
string = "!Ivan#444" #str
ls = ["Ivan" ,"Alex",111] #list


#fucns - input, print, type, append, max, min,  operations



                    
x = input("ENTER PASSCODE")
if x=="787":
    print ("Acsess Granted")
    y = input("Enter second passcode")
    if y == "777":
        print("Acsess granted")
    else:
        print("access denied")
    z=input
    time.sleep(1)
    print("you have now entered the database")
    time.sleep(1)
    print("choose option:")
    time.sleep(1)
    answer=input("calculator or quiz")
    if answer == "calculator":
        print("1 Addition")
        print("2 Subtraction")
        print("3 Multiplication")
        print("4 Division")
        print("5 To the power of")
    

        choice = input("Enter your choice") # "1" str

        num1 = float(input ("Enter number 1 : "))
        num2 = float(input ("Enter number 2 : "))
        if choice == "1": # 1 and "1"
            print(num1, "+", num2, "=", (num1 + num2))
        elif choice == "2":
            print(num1, "- ", num2, "=", (num1 - num2))
        elif choice == "3":
            print(num1, "*", num2, "=", (num1 * num2))
        elif choice == "3":
            print(num1, "/", num2, "=", (num1 / num2))
        elif choice == "4":
            if num1 == 0.0 or num2 == 0.0:
                print("divide by zero error")
            else:
                print(num1, "/", num2, "=", (num1 / num2))
        elif choice == "5":
        
              print(num1, "*",num1 , "=", (num1 ** 2))
        else:
            print("I'm not sure I understand")
    answer == input("would you like to try again")
    if answer == "yes":
        print("choose option:")
    time.sleep(1)
    answer=input("calculator or quiz")
   
      
              
