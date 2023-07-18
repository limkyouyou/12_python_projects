
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
    def __init__(self):
        self.num_board = [str(i) for i in range(9)]
        self.players = {
            1: 'X',
            2: 'O'
        }
        self.current_player = 1

    def available_spots(self):
        return [i for i, spot in enumerate(self.num_board) if spot != 'X' and spot != 'O']

    def spot_input(self):
        while True:
            try:
                spot = int(input('Choose a spot: '))
                if spot in self.available_spots():
                    return spot
                else:
                    raise ValueError
            except ValueError:
                print('invalid spot, try again')

    def print_board(self):
        for row in [self.num_board[i * 3: (i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def place_mark(self, player):
        spot = self.spot_input()
        self.num_board[spot] = self.players[player]

    def exectue(self):
        self.print_board()
        self.place_mark(self.current_player)
        self.print_board()
    
test = Tictactoe()
test.exectue()