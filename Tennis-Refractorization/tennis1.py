class TennisGame1:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        """Method to update the points of the player who won the point."""
        #if player_name == "player1": hardcoded player name

        if player_name == self.player1_name:
            self.p1points += 1
        else:
            self.p2points += 1

    def _get_tied_score(self):
        """Method to get the score when both players have the same number of points. Return string type."""
        scores = {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All",
        }
        return scores.get(self.p1points, "Deuce")
    
    def _get_endgame_score(self):
        """Method to get the score when at least one player has 4 or more points. Return string type."""
        delta_result = self.p1points - self.p2points
        leader = self.player1_name if delta_result > 0 else self.player2_name
        if abs(delta_result) == 1:
            return f"Advantage {leader}"
        else:
            return f"Win for {leader}"

    def _get_regular_score(self):
        """Method to get the score when both players have less than 4 points and the total points are less than 6. Return string type."""
        score_names = ["Love", "Fifteen", "Thirty", "Forty"]
        p1_score = score_names[self.p1points]
        p2_score = score_names[self.p2points]
        return f"{p1_score}-{p2_score}"
    

    def score(self):
        """Method to get the current score of the game. Return string type."""
        result = "" 
        
        if self.p1points == self.p2points:
            result = self._get_tied_score()
        elif self.p1points >= 4 or self.p2points >= 4:
            result = self._get_endgame_score()
        else:
            result = self._get_regular_score()

        return result
