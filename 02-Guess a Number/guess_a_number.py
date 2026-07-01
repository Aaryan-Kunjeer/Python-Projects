import random
print("********************** ")
print("Welcome to the Guessing Game!")
print("********************** ")
while True:
    secret_number = random.randint(1, 100)
    attempts = 0
    while True:
        try:
            guess_number = int(input("Guess a number between 1 and 100: "))
        except ValueError:
            print("Invalid Input, Please enter a valid number. ")
            continue
        if guess_number > 100 or guess_number < 1:
            print("Please enter a number between 1 and 100.")
            continue
        attempts += 1
        if guess_number < secret_number:
            print("Too low! Try again.")
        elif guess_number > secret_number:
            print("Too high! Try again.")
        else:
            if attempts == 1:
                print("🎉 Congratulations! You guessed the number", secret_number, "in", attempts, "attempt!")
            else:
                print("🎉 Congratulations! You guessed the number", secret_number, "in", attempts, "attempts!")
            break
    print("Do you want to play again? (yes/no)")
    play_again = input().strip().lower()
    if play_again == "yes":
        continue
    elif play_again == "no":
        print("Thanks for playing! Goodbye!")
        break
    else:
        print("Invalid input. Exiting the game.")
        break