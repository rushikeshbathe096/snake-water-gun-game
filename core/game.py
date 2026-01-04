#game flow - how game progresses
import random

from core.rules import choices, winner

def player_choice():
	user=input("Enter your choice")
	return user.strip().lower()

def computer_choice():
	return random.choice(choices)

def play_game():
	print("Welcome to Snake Water Gun game")
	player=player_choice()
	if player not in choices:
		print("Invalid choice")
		return

	computer=computer_choice()

	print("Your turn", player)
	print("Computer choice", computer)

	result=winner(player,computer)
	if result=="win":
		print("You win")
	elif result=="lose":
		print("You lose")
	else:
		print("Draw")