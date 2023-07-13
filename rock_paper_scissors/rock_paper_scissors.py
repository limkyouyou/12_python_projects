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
            print()
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
        
    def get_score(self):
        return [('computer', self.score['comp']), ('user', self.score['user'])]

    def check_game_result(self, played):
        scores = self.get_score()
        comp, user = scores
        if played == self.ttl_rounds:
            if comp[1] == user[1]:
                return ('tie', user[1])
            else:
                return max(scores, key=lambda item:item[1])
        elif comp[1] == 3:
            return comp
        elif user[1] == 3:
            return user
        return None
    
    def execute(self):
        round_played = 0
        print()
        print(f'Let\'s play best out of {self.ttl_rounds} - Rock, Paper, and Scissors!')
        while True:
            comp_hand = self.get_comp_hand()
            user_hand = self.get_user_hand()
            round_winner = self.get_round_winner(comp_hand=comp_hand, user_hand=user_hand)
            self.score[round_winner] += 1
            round_played += 1
            res = self.check_game_result(played=round_played)
            print()
            print(f'The current score is Computer - {self.score["comp"]} : {self.score["user"]} - User ')
            if res:
                print()
                print(f'End of game! The winner is the {res[0]} with {res[1]} points!')
                break

rps_game = RockPaperScissors(5)
rps_game.execute()