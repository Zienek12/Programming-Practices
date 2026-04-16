class TennisGame3:
    SCORE_NAMES = ("Love", "Fifteen", "Thirty", "Forty")

    def __init__(self, player1_name, player2_name):
        """
    
        """
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name):
        """
            Method to update the points of the player who won the point.
        """
        if player_name == self.player1_name:
            self.player1_points += 1
        else:
            self.player2_points += 1

    def score(self):
        """
            Method to get the current score of the game. 
            Return string type.
        """
        if self._is_tie():
            return self._tie_score()

        if self._is_endgame():
            return self._endgame_score()

        return self._regular_score()

    def _is_tie(self):
        """
            Check if both players have the same number of points.
            Return boolean type.
        """
        return self.player1_points == self.player2_points

    def _is_endgame(self):
        """
            Check if at least one player has 4 or more points.
            Return boolean type.
        """
        return self.player1_points >= 4 or self.player2_points >= 4

    def _tie_score(self):
        """
            Return appropriate score string when both players have the same number of points.
        """
        if self.player1_points >= 3:
            return "Deuce"
        return f"{self._point_name(self.player1_points)}-All"

    def _endgame_score(self):
        """
            Return appropriate score string when at least one player has 4 or more points.

        """
        diff = self.player1_points - self.player2_points
        leader = self._leader_name()

        if abs(diff) == 1:
            return f"Advantage {leader}"
        return f"Win for {leader}"

    def _regular_score(self):
        """
            Return appropriate score string for regular game states.
        """
        return (
            f"{self._point_name(self.player1_points)}-"
            f"{self._point_name(self.player2_points)}"
        )

    def _leader_name(self):
        """
            Return the name of the leading player.
        """
        return (
            self.player1_name
            if self.player1_points > self.player2_points
            else self.player2_name
        )

    def _point_name(self, points):
        """
            Return the name of the point based on its value.
        """
        return self.SCORE_NAMES[points]