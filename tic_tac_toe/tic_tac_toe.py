from player import Computer, User
#board = [
#    [['a', 1, 0], ['b', 1, None], ['c', 1, None]],
#    [['a', 2, None], ['b', 2, None], ['c', 2, None]],
#    [['a', 3, 1], ['b', 3, None], ['c', 3, None]]
#]

#rows = [
#    [('a',1), ('b',1), ('c',1)],
#    [('a',2), ('b',2), ('c',2)],
#    [('a',3), ('b',3), ('c',3)],
#    [('a',1), ('a',2), ('a',3)],
#    [('b',1), ('b',2), ('b',3)],
#    [('c',1), ('c',2), ('c',3)],
#    [('a',1), ('b',2), ('c',3)],
#    [('c',1), ('b',2), ('a',3)]
#]

#board = [str(i) for i in range(9)]
#
#board[6] = 'X'
#board[2] = 'X'
#board[4] = 'O'


#for row in [board[i * 3:(i + 1) * 3] for i in range(3)]:
#    print(('| ' + ' | '.join(row) + ' |'))

#num_board = [[str(i) for i in range(j * 3, (j + 1 ) * 3)] for j in range(3)]
#for row in num_board:
#    print(('| ' + '  | '.join(row) + ' |'))

#available_move = [i for i, spot in enumerate(board) if spot == ' ']

#row_check = [board[i * 3:(i + 1) * 3] for i in range(3) if 'O' not in board[i * 3:(i + 1) * 3]]
##print(row_check)
#col_check = [[board[i], board[i + 3], board[i + 6]] for i in range(3) if 'O' not in [board[i], board[i + 3], board[i + 6]]]
##print(col_check)
#cross_check = [[board[i], board[i + (4 - i)], board[i + 2 * (4 - i)]] for i in [0, 2] if 'O' not in [board[i], board[i + (4 - i)], board[i + 2 * (4 - i)]]]
##print(cross_check)
#total_check = row_check + col_check + cross_check
#print(total_check)
##total_check.sort(key=lambda item:item.count('X'), reverse=True)
#filter_double = list(filter(lambda item:item.count('X') == 2, total_check))
#print(filter_double)
#filter_one = list(filter(lambda item:item.count('X') == 1, total_check))
#print(filter_one)
#flat_filter_one = [x for y in filter_one for x in y if x != 'X']
#print(flat_filter_one)
#from collections import Counter
#flat_filter_one.sort(key=Counter(flat_filter_one).get, reverse=True)
#print(flat_filter_one)
#priority_list = []
#for item in flat_filter_one:
#    if item not in priority_list: priority_list.append(item)
#print(priority_list)

# 1. find winning rows
#  a. manually write all the winning rows
#  b. do for loop and get rows that includes the target position

# 2. priorities
#  a. check my double
#  b. check opponent double
#  c. check my one
#    - check that can get two doubles
#  d. check opponent one
#    - check that can get two doubles

class Tictactoe():
    def __init__(self, p_1, p_2):
        self.board = ['_' for i in range(9)]
        self.p_1 = p_1
        self.p_2 = p_2
        self.players = {
            -1: self.p_1,
            1: self.p_2
        }
        self.current_player = -1

    def available_spots(self):
        return [i for i, spot in enumerate(self.board) if spot != 'X' and spot != 'O']

    def print_board(self):
        for row in [self.board[i * 3: (i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def print_num_board(self):
        res = []
        for i, spot in enumerate(self.board):
            if spot == '_':
                res.append(str(i))
            else:
                res.append(spot)
        for row in [res[i * 3: (i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def place_mark(self, marker, spot):
        self.board[spot] = marker

    def switch_player(self):
        self.current_player *= -1

    def get_row(self, board):
        row_check = [board[i * 3:(i + 1) * 3] for i in range(3)]
        return row_check
        
    def get_col(self, board):
        col_check = [[board[i], board[i + 3], board[i + 6]] for i in range(3)]
        return col_check
    
    def get_cross(self, board):
        cross_check = [[board[i], board[i + (4 - i)], board[i + 2 * (4 - i)]] for i in [0, 2]]
        return cross_check
            
    def check_winner(self):
        get_total = self.get_row(self.board) + self.get_col(self.board) + self.get_cross(self.board)
        for player in self.players:
            check_total = filter(lambda item: self.players[player].marker not in item and '_' not in item, get_total)
            for i in check_total:
                return -(player)
        return False
            
    @classmethod
    def get_player(cls):
        res = []
        for marker in ['X', 'O']:
            while True:
                try:
                    player = input(f'Who will be the "{marker}"? Computer (C) or Human (H): ').lower()
                    if player == 'c' or player == 'h':
                        res.append(player)
                        break
                    raise ValueError
                except ValueError:
                    print('>> Invalid input, enter C for Computer or H for Human.')
        return res
def play():
    print()
    print('>> Welcome to tic-Tac-Toe!')
    print()
    print('>> Please select players. "X" will start first.')

    input_p1, input_p2 = Tictactoe.get_player()
    if input_p1 == 'c':
        p_1 = Computer('X')
    else:
        p_1 = User('X')
    if input_p2 == 'C':
        p_2 = Computer('O')
    else:
        p_2 = User('O')

    game = Tictactoe(p_1=p_1, p_2=p_2)

    available_space = game.available_spots()

    while available_space:
        current_player = game.players[game.current_player]
        print()
        move = current_player.get_move(game=game)
        game.place_mark(marker=current_player.marker, spot=move)
        print()
        game.print_board()
        print(f'>> {current_player.marker} takes square {move}')
        winner = game.check_winner()
        if winner:
            print()
            print(f'>> The winner is {game.players[winner].marker}!')
            return
        available_space = game.available_spots()
        game.switch_player()
    print()
    print('>> The game ends with draw.')



#    players = {
#        -1: p_1,
#        1: p_2
#    }
#    current_player = -1
#    while available_space:
#        pass
    
play()