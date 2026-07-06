import random
print("**********************")
print("Welcome to Rock, Paper, Scissors!")
print("**********************")
choices = ["rock", "paper", "scissors"]
def check_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"
    
while True:
    computer_choice = random.choice(choices)
    user_choice = input("Enter your choice (rock, paper, scissors): ").strip().lower()
    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper or scissors.")
        continue
    print("--------------------------")
    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)
    result = check_winner(user_choice, computer_choice)
    print(result)
    print("--------------------------")
    print("Do you want to play again? (yes/no)")
    play_again = input().strip().lower()
    if play_again not in ["yes", "no"]:
        print("Invalid choice. Please enter 'yes' or 'no'.")
    elif play_again == "no":
        print("Thanks for playing!")
        break
    else:
        continue 