# Game flow - how game progresses

from ai.random_ai import RandomAI
from core.rules import choices, winner

def player_choice():
    user = input("Enter your choice: ")
    return user.strip().lower()

def play_game():
    print("Welcome to Snake Water Gun game")

    ai = RandomAI()

    player = player_choice()
    if player not in choices:
        print("Invalid choice")
        return

    computer = ai.choose_move(choices)

    print("Your turn", player)
    print("Computer choice", computer)

    result = winner(player, computer)
    if result == "win":
        print("You win")
    elif result == "lose":
        print("You lose")
    else:
        print("Draw")
