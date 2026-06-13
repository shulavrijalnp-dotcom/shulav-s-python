import random


def number_choices():
    options = ["0", "1", "2", "3", "4", "5"]
    human_choices = input("enter your number below 5 or equal to 5 ( : ")
    Ai_choices = random.choice(options)
    choices = {"player": human_choices, "ai": Ai_choices}

    return choices


def add(choices):
    player = int(choices["player"])
    ai = int(choices["ai"])
    total = player + ai
    return total


choices = number_choices()
result = add(choices)
print(f"You chose: {choices['player']}")
print(f"Computer chose: {choices['ai']}")
print(result)
