class BaseAI:
    def choose_move(self, choices):
        raise NotImplementedError("choose_move must be implemented by subclasses")
