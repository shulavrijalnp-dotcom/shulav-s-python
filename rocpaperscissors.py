import random


def get_choices():

    options = ["rock", "paper", "scissors"]

    player_choices = input("enter the choice(rock, paper, scissors: ")
    computer_choices = random.choice(options)
    choices = {"player": player_choices, "computer": computer_choices}
    return choices


def check_winner(choices):
    player = choices["player"]
    computer = choices["computer"]

    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"


choices = get_choices()

result = check_winner(choices)
print(result)
