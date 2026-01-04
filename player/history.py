class PlayerHistory:
    def __init__(self):
        self.moves = []

    def record_move(self, move):
        self.moves.append(move)

    def get_history(self):
        return self.moves
