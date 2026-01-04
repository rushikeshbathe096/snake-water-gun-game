from ai.base import BaseAI
import random

class AdaptiveAI(BaseAI):
    def __init__(self, player_history):
        self.player_history = player_history

    def choose_move(self, choices):
        history = self.player_history.get_history()

        if not history:
            return random.choice(choices)

        most_common = max(set(history), key=history.count)

        counter_moves = {
            "snake": "gun",
            "water": "snake",
            "gun": "water"
        }

        return counter_moves.get(most_common, random.choice(choices))
