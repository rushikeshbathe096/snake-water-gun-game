# Game flow - how game progresses
from player.history import PlayerHistory
from analytics.stats import GameStats

from ai.adaptive_ai import AdaptiveAI
from core.rules import choices, winner

def player_choice():
    user = input("Enter your choice: ")
    return user.strip().lower()

def play_game():
    print("Welcome to Snake Water Gun game")

    history = PlayerHistory()
    stats = GameStats()
    ai = AdaptiveAI(history)

    player = player_choice()
    if player not in choices:
        print("Invalid choice")
        return
    history.record_move(player)
    stats.record_move(player)

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

    stats.record_result(result)

