from random import randint

class RockPaperScissors():
    def __init__(self, ttl_rounds: int, ):
        self.ttl_rounds = ttl_rounds
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

    def get_user_hand(self):
        while True:
            hand = input('Choose Rock (R), Paper (P), or Scissors (S): ').lower()
            if hand == 'r':
                return self.hands['rock']
            elif hand == 'p':
                return self.hands['paper']
            elif hand == 's':
                return self.hands['scissors']
            else:
                print('Invalid input. Please type in R for Rock, P for Paper, or S for Scissors.')
        