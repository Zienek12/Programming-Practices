class TennisGame3:
    POINT_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        self.p1_n = player1_name
        self.p2_n = player2_name
        self.p1 = 0
        self.p2 = 0

    def won_point(self, n):
        if n == "player1":
            self.p1 += 1
        else:
            self.p2 += 1

    def score(self):
        if self._is_regular_score():
            return self._regular_score()
        return self._late_game_score()

    def _is_regular_score(self):
        return self.p1 < 4 and self.p2 < 4 and self.p1 + self.p2 < 6

    def _regular_score(self):
        player1_score = self.POINT_NAMES[self.p1]
        if self.p1 == self.p2:
            return player1_score + "-All"

        player2_score = self.POINT_NAMES[self.p2]
        return player1_score + "-" + player2_score

    def _late_game_score(self):
        if self.p1 == self.p2:
            return "Deuce"

        leading_player = self.p1_n if self.p1 > self.p2 else self.p2_n
        point_difference = abs(self.p1 - self.p2)

        if point_difference == 1:
            return "Advantage " + leading_player
        return "Win for " + leading_player
