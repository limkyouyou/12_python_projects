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
            'computer': 0,
            'user': 0,
        }

    def get_comp_hand(self):
        hand_val = randint(-1, 1)
        return ('computer', hand_val)

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
                print()
        return ('user', hand_val)

    def get_round_winner(self, comp_hand, user_hand):
        hands = [comp_hand, user_hand]
        if comp_hand[1] != user_hand[1]:
            if abs(comp_hand[1]) == abs(user_hand[1]):
                return min(hands, key=lambda item:item[1])[0]
            return max(hands, key=lambda item: item[1])[0]
        return None
        
    def get_score(self):
        return [('computer', self.score['computer']), ('user', self.score['user'])]

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
    
    def get_hand_string(self, hand_val):
        hand_string = {
            -1: 'rock',
            0: 'paper',
            1: 'scissors,'
        }
        return hand_string[hand_val]
    
    def execute(self):
        round_played = 0
        print()
        print(f'Let\'s play best out of {self.ttl_rounds} - Rock, Paper, and Scissors!')
        while True:
            print()
            print(f'Round {round_played + 1}')
            comp_hand = self.get_comp_hand()
            user_hand = self.get_user_hand()
            comp_hand_str = self.get_hand_string(comp_hand[1])
            user_hand_str = self.get_hand_string(user_hand[1])
            print()
            print(f'Computer -> {comp_hand_str.capitalize()} : {user_hand_str.capitalize()} <- User')
            round_winner = self.get_round_winner(comp_hand=comp_hand, user_hand=user_hand)
            if round_winner:
                print(f'This round winner is the {round_winner.capitalize()}!')
                self.score[round_winner] += 1
            else:
                print('This round is a tie!')
            round_played += 1
            res = self.check_game_result(played=round_played)
            print()
            print(f'The current score is Computer - {self.score["computer"]} : {self.score["user"]} - User ')
            if res:
                print()
                print(f'End of game! ', end='')
                if res[0] != 'tie':
                    print(f'The winner is the {res[0].capitalize()} with {res[1]} points!')
                else:
                    print('The game ends with a tie!')
                break

rps_game = RockPaperScissors(5)
rps_game.execute()