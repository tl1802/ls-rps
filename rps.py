import random

VALID_CHOICES = ["rock", "paper", "scissors"]



def display_winner(player, computer):
    prompt(f"You chose {player}, computer chose {computer}")

    if ((player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")):
        prompt("You win!")
    elif ((player == "rock" and computer == "paper") or
          (player == "paper" and computer == "scissors") or
          (player == "scissors" and computer == "rock")):
        prompt("Computer wins!")
    else:
        prompt("It's a tie!")

def prompt(message):
    print(f"==> {message}")

while True:
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice = input()

    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        choice = input()

    computer_choice = random.choice(VALID_CHOICES)

    display_winner(choice, computer_choice)

    while True:
        prompt("Do you want to play again (y/n)?")
        answer = input().lower()

        if answer.startswith('n') or answer.startswith('y'):
            break
        else:
            prompt("That's not a valid choice")

    if answer[0] == 'n':
        break

# 1. it should not work - can't call prompt function because it hasn't been defined yet
# you get a NameError
# It actually does work - don't remember where, but functions are hoisted? 
# or maybe the functions coexist in memory, the order they're defined doesn't matter
# they exist simultanexouly and can be called at anytime so long as they are defined
# before they are called
# all functions have to be defined in the top of the program in any order

# 2. Since the name of the function is display_winner, it should only display, and not return
# and this is true. If it were to return a string instead, all we have to do is capture the
# return value in a variable. Then we can print that variable later.

# 3. One thing we can do use to set the outer while loop to a variable. We can create a variable
# and set it to a truthy value, for example 1. It runs while truthy. For the case where we want
# the function to stop, we can reassign the variable to a falsy value such as 0. This will stop 
# the program.