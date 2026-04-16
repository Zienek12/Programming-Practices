class TennisGame2:
    POINT_NAMES = {
        0: "Love",
        1: "Fifteen",
        2: "Thirty",
        3: "Forty",
    }

    TIED_SCORES = {
        0: "Love-All",
        1: "Fifteen-All",
        2: "Thirty-All",
    }

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.p1_score()
        else:
            self.p2_score()

    def score(self):
        if self.p1points == self.p2points:
            return self.TIED_SCORES.get(self.p1points, "Deuce")

        if self.p1points >= 4 or self.p2points >= 4:
            return self._end_game_score()

        return self._regular_score()

    def _end_game_score(self):
        points_delta = self.p1points - self.p2points

        if points_delta == 1:
            return "Advantage player1"
        if points_delta == -1:
            return "Advantage player2"
        if points_delta >= 2:
            return "Win for player1"
        return "Win for player2"

    def _regular_score(self):
        p1_score_name = self.POINT_NAMES[self.p1points]
        p2_score_name = self.POINT_NAMES[self.p2points]
        return p1_score_name + "-" + p2_score_name

    def set_p1_score(self, number):
        for _ in range(number):
            self.p1_score()

    def set_p2_score(self, number):
        for _ in range(number):
            self.p2_score()

    def p1_score(self):
        self.p1points += 1

    def p2_score(self):
        self.p2points += 1
