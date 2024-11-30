import random

VALID_CHOICES = ["rock", "paper", "scissors", "lizard", "spock"]
SHORT_CHOICES = {"r" : "rock", "p" : "paper", "s" : "scissors", "l" : "lizard", "k" : "spock"}

WINNING_CHOICES = {"rock" : ["scissors", "lizard"],
                    "paper" : ["rock", "spock"],
                    "scissors" : ["paper", "lizard"],
                    "spock" : ["scissors", "rock"],
                    "lizard" : ["paper", "spock"]}

LOSING_CHOICES = {"rock" : ["paper", "spock"],
                    "paper" : ["lizard", "scissors"],
                    "scissors" : ["rock", "spock"],
                    "spock" : ["paper", "lizard"],
                    "lizard" : ["scissors", "rock"]}

player_wins = 0
computer_wins = 0

def prompt(message):
    print(f"==> {message}")

def short_input_mapping(selection):
    if selection in SHORT_CHOICES:
        return SHORT_CHOICES[selection]
    else:
        return selection

def display_winner(player, computer):
    prompt(f"You chose {player}, computer chose {computer}")

    if computer in WINNING_CHOICES[player]:
        prompt("You win!")
    elif computer in LOSING_CHOICES[player]:
        prompt("Computer wins!")
    else:
        prompt("It's a tie!")

def keep_score(player, computer):
    if computer in WINNING_CHOICES[player]:
        global player_wins
        player_wins += + 1
        prompt(f'You win this round! ({player_wins} win - first to 3 wins)')
    elif computer in LOSING_CHOICES[player]:
        global computer_wins
        computer_wins += 1
        prompt(f'Computer wins this round! ({computer_wins} win - first to 3 wins)')

def declare_winner():
    if player_wins > computer_wins:
        prompt(f'You Win! {player_wins} win vs Computer\'s {computer_wins} win')
    else:
        prompt(f'Computer Wins! {computer_wins} win vs your {player_wins} win')

while True:
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    prompt(f'You can also type {", ".join(SHORT_CHOICES.keys())}')
    player_choice = input().lower()
    player_choice = short_input_mapping(player_choice)

    while player_choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
        prompt(f'You can also type {", ".join(SHORT_CHOICES.keys())}')
        player_choice = input().lower()
        player_choice = short_input_mapping(player_choice)

    computer_choice = random.choice(VALID_CHOICES)

    display_winner(player_choice, computer_choice)

    keep_score(player_choice, computer_choice)

    if player_wins == 3 or computer_wins == 3:
        break

    while True:
        prompt("Do you want to play again (y/n)?")
        answer = input().lower()

        if answer.startswith('n') or answer.startswith('y'):
            break
        else:
            prompt("That's not a valid choice")

    if answer[0] == 'n':
        break

declare_winner()
