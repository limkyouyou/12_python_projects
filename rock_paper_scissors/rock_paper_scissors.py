from random import randint

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

    def get_comp_hand(self):
        hand = randint(-1, 1)
        return hand
        