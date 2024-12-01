import random

VALID_CHOICES = ["rock", "paper", "scissors", "lizard", "spock"]
SHORT_CHOICES = {"r" : "rock", "p" : "paper", "s" : "scissors", "l" : "lizard", "k" : "spock"}

WINNING_CHOICES = {"rock" : ["scissors", "lizard"],
                    "paper" : ["rock", "spock"],
                    "scissors" : ["paper", "lizard"],
                    "spock" : ["scissors", "rock"],
                    "lizard" : ["paper", "spock"]}

WIN_CONDITION = 3
player_wins = 0
computer_wins = 0

def prompt(message):

    print(f"==> {message}")

def short_input_mapping(selection):

    if selection in SHORT_CHOICES:
        return SHORT_CHOICES[selection]

    return selection

def display_winner(player, computer):

    prompt(f"You chose {player}, computer chose {computer}")

    if computer in WINNING_CHOICES[player]:
        prompt("You win!")
    elif player == computer:
        prompt("It's a tie!")
    else:
        prompt("Computer wins!")

def keep_score(player, computer):

    global player_wins
    global computer_wins
    if computer in WINNING_CHOICES[player]:
        player_wins += 1
        prompt(f'You win this round! ({player_wins} win - first to 3 wins)')
    elif player == computer:
        return
    else:
        computer_wins += 1
        prompt(f'Computer wins this round! ({computer_wins} win - first to 3 wins)')

def declare_winner():

    if player_wins > computer_wins:
        prompt(f'You Win! {player_wins} win vs Computer\'s {computer_wins} win')
    elif computer_wins > player_wins:
        prompt(f'Computer Wins! {computer_wins} win vs your {player_wins} win')
    else:
        prompt(f'It\'s a tie! {computer_wins} win vs your {player_wins} win')

def player_turn():

    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    prompt(f'You can also type: {", ".join(SHORT_CHOICES.keys())}')
    player_choice = input().lower()
    player_choice = short_input_mapping(player_choice)
    return player_choice

while True:

    player_choice = player_turn()

    while player_choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        player_choice = player_turn()

    computer_choice = random.choice(VALID_CHOICES)

    display_winner(player_choice, computer_choice)

    keep_score(player_choice, computer_choice)

    if player_wins == WIN_CONDITION or computer_wins == WIN_CONDITION:
        break

    prompt("Do you want to play again (y/n)?")
    answer = input().lower()

    while answer not in ['n', 'y']:
        prompt("That's not a valid choice")
        prompt("Do you want to play again (y/n)?")
        answer = input().lower()
    
    if answer == 'n':
        break

declare_winner()


# def main ():
    # get player input
    # get cpu input
    # set increment counter, win condition
    # compare player to cpu
    # add increment to counter
    # display round result
    # ask to repeat
    # loop over again until 3 wins
    # declare final winner
    # player_wins = 0
    # computer_wins = 0
    
    # player_choice = player_turn()

    # while player_choice not in VALID_CHOICES:
    #     prompt("That's not a valid choice")
    #     player_choice = player_turn()

    # computer_choice = random.choice(VALID_CHOICES)