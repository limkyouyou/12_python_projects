from random import randint


class GuessNum():
    def __init__(self, max_num: int):
        self.max_num = max_num
    
    def set_max_tries(self):
        return self.max_num // 2

    def get_rand_num(self):
        if self.max_num: return randint(1, self.max_num)
    
    def get_inputs(self):
        guess = int(input(f'Your guess: '))
        return guess
    
    def play_round(self, rand_num):
        guess = self.get_inputs()
        if guess > rand_num:
            return 1
        elif guess < rand_num:
            return -1
        else:
            return 0
        
    def execute(self):
        max_tries = self.set_max_tries()
        rand_num = self.get_rand_num()
        for i in range(max_tries, 0, -1):
            print(f'Guess a number between 1 and {self.max_num}. You have {i} ', end='')
            print('tries left.') if i > 1 else print('try left.')
            res = self.play_round(rand_num=rand_num)
            if res > 0:
                print('Your number is too high.')
            elif res < 0:
                print('Your number is too low.')
            else:
                print('Congratulation! You\'ve guessed the correct number.')
                break
        else:
            print('You have no more tries left. Try again next time.')

guess_num = GuessNum(max_num=10)
guess_num.execute()