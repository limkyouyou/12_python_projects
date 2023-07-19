from player import Computer, User

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
    def get_player(cls, marker):
        while True:
            try:
                player = input(f'Who will be the "{marker}"? Computer (C) or Human (H): ').lower()
                if player == 'c' or player == 'h':
                    return player
                raise ValueError
            except ValueError:
                print('>> Invalid input')

    @classmethod
    def execute(cls):
        print()
        print('>> Welcome to tic-Tac-Toe!')
        print()
        print('>> Please select players. "X" will start first.')

        players = []
        for mark in ('X', 'O'):
            input = Tictactoe.get_player(mark)
            if input == 'c':
                difficulty = Computer.get_diff_input()
                players.append(Computer(marker=mark, difficulty=difficulty))
            else:
                players.append(User(marker=mark))

        p_1, p_2 = players
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

if __name__ == '__main__':
    Tictactoe.execute()