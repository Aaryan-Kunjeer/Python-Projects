import random
import string
print("**********************")
print("Welcome to the Password Generator!")
print("**********************")
while True:
    characters=string.ascii_letters + string.digits + string.punctuation
    try:
        length=int(input("Enter the Length of the password you want to generate: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        continue
    if length <= 0:
        print("Password length must be a positive integer.")
        continue
    password = ""
    for i in range(length):
        password += random.choice(characters)
    print("Your generated password is: ", password)

    generate_again = input("Do you want to generate another password? (yes/no): ").strip().lower()
    if generate_again not in ["yes", "no"]:
        print("Invalid input. Please enter 'yes' or 'no'.")
        continue
    elif generate_again == "no":
        print("Thank you for using the Password Generator!")
        break
    else:
        continue
    


