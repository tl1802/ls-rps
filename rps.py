import random

VALID_CHOICES = ["rock", "paper", "scissors","lizard", "spock"]
SHORT_CHOICES = {"r" : "rock", "p" : "paper", "s" : "scissors", "l" : "lizard", "k" : "spock"}

WINNING_COMBOS = {"rock" : ["scissors", "lizard"],
                    "paper" : ["rock", "spock"],
                    "scissors" : ["paper", "lizard"],
                    "spock" : ["scissors", "rock"],
                    "lizard" : ["paper", "spock"]}

WIN_CONDITION = 3

def prompt(message):
    """adds arrow to each message"""
    print(f"==> {message}")

def short_input_mapping(selection):
    """maps short one char inputs to choices"""
    if selection in SHORT_CHOICES:
        return SHORT_CHOICES[selection]

    return selection

def display_round_winner(player, computer, win_counter):
    """checks WINNING_COMBOS to see who won and displays score""" 
    if computer in WINNING_COMBOS[player]:
        prompt(f'You win this round! ({win_counter[0]} win to {win_counter[1]} wins)')
    elif player == computer:
        prompt(f"It's a tie! ({win_counter[0]} win to {win_counter[1]} wins)")
    else:
        prompt(f'Computer wins this round! ({win_counter[0]} win to {win_counter[1]} wins)')

def keep_score(player, computer, win_counter):
    """checks WINNING_COMBOS and updates the scoreboard"""
    if computer in WINNING_COMBOS[player]:
        return [win_counter[0] + 1, win_counter[1]]
    elif player == computer:
        return win_counter
    else:
        return [win_counter[0], win_counter[1] + 1]

def declare_grand_winner(win_counter):
    """declare grand winner by comparing scores"""
    if win_counter[0] > win_counter[1]:
        prompt(f'You Win! {win_counter[0]} win vs Computer\'s {win_counter[1]} win')
    elif win_counter[1] > win_counter[0]:
        prompt(f'Computer Wins! {win_counter[1]} win vs your {win_counter[0]} win')
    else:
        prompt(f'It\'s a tie! {win_counter[1]} win vs your {win_counter[0]} win')

def player_turn():
    """gets the player's choice"""
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    prompt(f'You can also type: {", ".join(SHORT_CHOICES.keys())}')
    player_choice = input().lower()
    player_choice = short_input_mapping(player_choice)
    return player_choice

def main ():
    """executes main function"""
    win_counter = [0, 0]

    while True:

        player_choice = player_turn()

        while player_choice not in VALID_CHOICES:
            prompt("That's not a valid choice")
            player_choice = player_turn()

        computer_choice = random.choice(VALID_CHOICES)
        prompt(f"You chose {player_choice}, Computer chose {computer_choice}")

        win_counter = keep_score(player_choice, computer_choice, win_counter)

        display_round_winner(player_choice, computer_choice, win_counter)

        if WIN_CONDITION in win_counter:
            declare_grand_winner(win_counter)
            break

        prompt("Do you want to play again (y/n)?")
        answer = input().lower()

        while answer not in ['n', 'y']:
            prompt("That's not a valid choice")
            prompt("Do you want to play again (y/n)?")
            answer = input().lower()

        if answer == 'n':
            declare_grand_winner(win_counter)
            break

main()
