class TennisGame2:
    # Class variable to map points to their corresponding score names.
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        """
            Method to update the points of the player who won the point.
            Return None.
        """
        if player_name == self.player1_name:
            self.p1_score()
        else:
            self.p2_score()
        

    def score(self):
        """
            Method to get the current score of the game. 
            Return string type.
        """
        if self.p1points == self.p2points:
            if self.p1points >= 3:
                return "Deuce"
            return f"{self._point_name(self.p1points)}-All"

        if self.p1points >= 4 or self.p2points >= 4:
            diff = self.p1points - self.p2points
            leader = self.player1_name if diff > 0 else self.player2_name

            if abs(diff) == 1:
                return f"Advantage {leader}"
            return f"Win for {leader}"

        return f"{self._point_name(self.p1points)}-{self._point_name(self.p2points)}"

    def _point_name(self, points):
        """
            Method to get the name of the score based on the points. 
            Return string type.
        """
        return self.SCORE_NAMES[points]


    """Methods to update the points of each player."""
    def p1_score(self):
        self.p1points += 1

    def p2_score(self):
        self.p2points += 1