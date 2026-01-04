import random
from ai.base import BaseAI

class RandomAI(BaseAI):
    def choose_move(self,choices):
        return random.choice(choices)