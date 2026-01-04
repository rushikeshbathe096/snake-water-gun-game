class GameStats:
    def __init__(self):
        self.results = {"win": 0, "lose": 0, "draw": 0}
        self.moves = {"snake": 0, "water": 0, "gun": 0}

    def record_move(self, move):
        if move in self.moves:
            self.moves[move] += 1

    def record_result(self, result):
        if result in self.results:
            self.results[result] += 1

    def get_summary(self):
        return {
            "moves": self.moves,
            "results": self.results
        }
