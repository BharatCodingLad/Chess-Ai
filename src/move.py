class Move:
    def __init__(self, initial, final):
        # initial and final are squares
        self.initial = initial
        self.final = final

    def __eq__(self, other):
        return isinstance(other, Move) and self.initial == other.initial and self.final == other.final

    def __hash__(self):
        return hash((self.initial, self.final))