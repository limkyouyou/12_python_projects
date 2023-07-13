
from random import randint

class GuessNumComp():
    def __init__(self, max_num: int):
        self.max_num = max_num
        self.pool = [i for i in range(1, self.max_num + 1)]

    def get_max_tries(self):
        return self.max_num // 2
    
    def guess_num(self, min_num, max_num):
        return randint(min_num, max_num)
    
    def get_res(self, guess):
        res = input(f'Is {guess} too high (H), too low (L), or correct (C)?: ').lower()
        return res
    
    def execute(self):
        max_tries = self.get_max_tries()
        tries = 1
        min_num = 1
        max_num = self.max_num
        print()
        print(f'Think of a number between 1 to {self.max_num} and see if I can guess it correctly in {max_tries} tries.')
        while tries <= max_tries:
            print()
            print(f'Alright, I have {max_tries - tries + 1} tries left.') if tries < max_tries else print('This is my last try.')
            print()
            guess = self.guess_num(min_num=min_num, max_num=max_num)
            print(f'My guess is {guess}')
            res = self.get_res(guess)
            if res == 'h':
                max_num = guess - 1
            elif res == 'l':
                min_num = guess + 1
            else:
                print()
                print('Amazing! I guessed it correctly ', end='')
                if tries < max_tries:
                    print(f'in {tries} ', end='')
                    if tries == 1:
                        print('try!')
                    else:
                        print('tries!') 
                else:
                    print('on the last try!')
                break
            tries += 1
        else:
            print()
            print('I could not guess your number. Let\'s try again next time')

guess_comp = GuessNumComp(10)
guess_comp.execute()