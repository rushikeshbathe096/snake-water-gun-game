choices=["snake" , "water" , "gun"]

def winner(player,computer):
	if player==computer:
		return "draw"
	if( (player =="snake" and computer =="water") or (player=="water" and computer=="gun") or (player=="gun" and computer=="snake")):
		return "win"
	return "lose"
