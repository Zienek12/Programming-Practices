class TennisGame1:
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
            self.p1points += 1
        else:
            self.p2points += 1

    def score(self):
        if self.p1points == self.p2points:
            return self.TIED_SCORES.get(self.p1points, "Deuce")

        if self.p1points >= 4 or self.p2points >= 4:
            return self.end_game_score()

        return self.normal_score()

    def end_game_score(self):
        point_difference = self.p1points - self.p2points

        if point_difference == 1:
            return "Advantage player1"
        if point_difference == -1:
            return "Advantage player2"
        if point_difference >= 2:
            return "Win for player1"
        return "Win for player2"

    def normal_score(self):
        player1_score = self.POINT_NAMES[self.p1points]
        player2_score = self.POINT_NAMES[self.p2points]
        return player1_score + "-" + player2_score
