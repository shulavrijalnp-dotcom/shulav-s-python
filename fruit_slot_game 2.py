import random

# ------------------- SETTINGS -------------------
options = ["kera", "syau", "suntala", "naspati", "litchi"]
starting_balance = 100
two_match_multiplier = 2   # 2 similar fruits -> double money
three_match_multiplier = 5  # 3 similar fruits -> 5x money


def spin():
    """Return 3 random fruits."""
    return [random.choice(options) for _ in range(3)]


def choose_fruit():
    """Let the player pick a fruit to bet on."""
    print("\nAvailable fruits:")
    for i, fruit in enumerate(options, start=1):
        print(f"  {i}. {fruit}")

    while True:
        pick = input(
            "Choose a fruit (type the name or number): ").strip().lower()

        if pick.isdigit():
            index = int(pick) - 1
            if 0 <= index < len(options):

                return options[index]
            print("Invalid number, try again.")
            continue

        if pick in options:
            return pick

        print("Invalid fruit, try again.")


def check_win(result, player_choice, bet):
    """Count how many spun fruits match the player's choice and return winnings."""
