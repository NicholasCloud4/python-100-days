import random

choices = ["rock", "paper", "scissors"]
beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

print("Welcome to Rock Paper Scissors!")

while True:
    user = input("\nType rock, paper or scissors (or 'quit' to exit): ").strip().lower()

    if user == "quit":
        print("Thanks for playing!")
        break

    if user not in choices:
        print("Invalid choice, please try again.")
        continue

    computer = random.choice(choices)
    print(f"You chose {user}, computer chose {computer}.")

    if user == computer:
        print("It's a draw!")
    elif beats[user] == computer:
        print("You win!")
    else:
        print("You lose!")
