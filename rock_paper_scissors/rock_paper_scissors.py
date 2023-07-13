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
        hand_val = randint(-1, 1)
        return ('comp', hand_val)

    def get_user_hand(self):
        while True:
            hand = input('Choose Rock (R), Paper (P), or Scissors (S): ').lower()
            if hand == 'r':
                hand_val =  self.hands['rock']
                break
            elif hand == 'p':
                hand_val =  self.hands['paper']
                break
            elif hand == 's':
                hand_val =  self.hands['scissors']
                break
            else:
                print('Invalid input. Please type in R for Rock, P for Paper, or S for Scissors.')
        return ('user', hand_val)

    def get_round_winner(self, comp_hand, user_hand):
        hands = [comp_hand, user_hand]
        if abs(comp_hand[1]) == abs(user_hand[1]):
            return min(hands, key=lambda item:item[1])[0]
        else:
            return max(hands, key=lambda item: item[1])[0]
