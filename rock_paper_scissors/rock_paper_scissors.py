
class RockPaperScissors():
    def __init__(self, rounds: int, ):
        self.rounds = rounds
        self.hands = {
            'rock': -1,
            'paper': 0,
            'scissors': 1,
        }
        self.score = {
            'comp': 0,
            'user': 0,
        }

    