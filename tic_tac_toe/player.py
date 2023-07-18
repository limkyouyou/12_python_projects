
from collections import Counter
from random import choice

class Player():
    def __init__(self, marker):
        self.marker = marker
      
    def get_move(self, game):
        pass
    
class User(Player):
    def __init__(self, marker):
        self.marker = marker

    def get_move(self, game):
        while True:
            try:
                spot = int(input('Choose a spot: '))
                if spot in game.available_spots():
                    return spot
                else:
                    raise ValueError
            except ValueError:
                print('invalid spot, try again')
    

class Computer(Player):
    def __init__(self, marker):
        super().__init__(marker)

    def get_opponent(self, marker, game):
        for key, value in game.players.items():
            if value != marker:
                return key

    def get_total_list(self, game):
        num_board =  [i if spot == '_' else spot for i, spot in enumerate(game.board)]
        return game.get_row(num_board) + game.get_col(num_board) + game.get_cross(num_board)
    
    def filter_list(self, total_list, marker, opponent):
        return [x for x in total_list if opponent not in x and marker in x]

    def filter_double(self, filtered_list, marker):
        res = []
        double_list = list(filter(lambda item:item.count(marker) == 2, filtered_list))
        if double_list:
            flat_double = [x for y in double_list for x in y if x != marker]
            flat_double.sort(key=Counter(flat_double).get, reverse=True)
            for item in flat_double:
                if item not in res: res.append(item)
        return res
    
    def filter_single(self, filtered_list, marker):
        res = []
        single_list = list(filter(lambda item:item.count(marker) == 1, filtered_list))
        if single_list:
            flat_single = [x for y in single_list for x in y if x != marker]
            flat_single.sort(key=Counter(flat_single).get, reverse=True)
            for item in flat_single:
                if item not in res: res.append(item)
        return res

    def get_move(self, game):
        opponent = self.get_opponent(self.marker, game)
        opponent_marker = game.players[opponent]
        total_list = self.get_total_list(game=game)

        my_list = self.filter_list(total_list=total_list, marker=self.marker, opponent=opponent_marker)
        my_double_list = self.filter_double(filtered_list=my_list, marker=self.marker)
        my_single_list = self.filter_single(filtered_list=my_list, marker=self.marker)
        
        opponent_list = self.filter_list(total_list=total_list, marker=opponent_marker, opponent=self.marker)
        opponent_double_list = self.filter_double(filtered_list=opponent_list, marker=opponent_marker)
        opponent_single_list = self.filter_single(filtered_list=opponent_list, marker=opponent_marker)

        priority_list = my_double_list + opponent_double_list + my_single_list + opponent_single_list
        if priority_list:
            return priority_list[0]
        return choice([x for x in range(9) if x % 2 == 0])