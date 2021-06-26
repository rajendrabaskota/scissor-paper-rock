class Game:
    def __init__(self, id):
        self.id = id
        self.p1_went = False
        self.p2_went = False
        self.ready = False
        self.moves = ['', '']
        self.wins = [0, 0]
        self.ties = 0

    def get_player_move(self, p):
        """
        :param p: [0, 1]
        :return: move
        """
        return self.moves[p]

    def player(self, player, move):
        self.moves[player] = move
        if player == 0:
            self.p1_went = True
        else:
            self.p2_went = True

    def connected(self):
        return self.ready

    def both_went(self):
        return self.p1_went and self.p2_went

    def winner(self):
        p1 = self.moves[0].upper()[0]
        p2 = self.moves[1].upper()[0]

        winner = -1
        if p1 == "R" and p2 == "S":
            winner = 0
        elif p1 == "R" and p2 == "P":
            winner = 0
        elif p1 == "S" and p2 == "P":
            winner = 0
        elif p2 == "R" and p1 == "S":
            winner = 1
        elif p2 == "R" and p1 == "P":
            winner = 1
        elif p2 == "S" and p1 == "P":
            winner = 1

        return winner

    def reset(self):
        self.p1_went = False
        self.p2_went = False
