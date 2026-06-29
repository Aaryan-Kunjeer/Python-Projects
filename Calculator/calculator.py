print("********************\n     Calculator \n********************")
while True:
    print("What do you want to do?")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    try:
        choice = int(input("Enter your choice (1/2/3/4/5): "))
    except ValueError:
        print("Invalid Input, Please enter a number between 1 and 5.")
        continue
    if choice==5:
        print("Thank You For Using Calculator")
        break
    try:
        num1 = int(input("Enter First Number: "))
    except ValueError:
        print("Invalid Input, Please enter a valid number.")
        continue
    try:
        num2 = int(input("Enter Second Number: "))
    except ValueError:
        print("Invalid Input, Please enter a valid number.")
        continue
    if choice==1:
        print("Your Answer Is:", num1, "+", num2, "=", num1 + num2)
    elif choice==2:
        print("Your Answer Is:", num1, "-", num2, "=", num1 - num2)
    elif choice==3:
        print("Your Answer Is:", num1, "*", num2, "=", num1 * num2)
    elif choice==4:
        if num2==0:
            print("Error: Division by zero is not allowed.")
        else:
            print("Your Answer Is:", num1, "/", num2, "=", num1 / num2)    
    else:
        print("Invalid Input,Pls Try 1,2,3,4 or 5")
    print("Do you want to continue? (yes/no)")
    continue_choice=input("Enter your choice: ").lower()
    if continue_choice=="yes":
        print("Ok, Let's Continue")
        continue
    elif continue_choice=="no":
         print("Thank You For Using Calculator")
         break
    else:
        print("Invalid Input,Pls Try yes or no")
    continue