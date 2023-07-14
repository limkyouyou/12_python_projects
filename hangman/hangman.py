from random import choice
from string import ascii_lowercase

class Hangman():
    def __init__(self, filename):
        self.filename = filename
        self.hangman_pic = [
            "       +---+\n       |   |\n       O   |\n      /|\  |\n      / \  |\n           |\n     =========",
            "       +---+\n       |   |\n       O   |\n      /|\  |\n      /    |\n           |\n     =========",
            "       +---+\n       |   |\n       O   |\n      /|\  |\n           |\n           |\n     =========",
            "       +---+\n       |   |\n       O   |\n      /|   |\n           |\n           |\n     =========",
            "       +---+\n       |   |\n       O   |\n       |   |\n           |\n           |\n     =========",
            "       +---+\n       |   |\n       O   |\n           |\n           |\n           |\n     =========",
            "       +---+\n       |   |\n           |\n           |\n           |\n           |\n     =========",
          ]
        self.eng_words = []
        self.user_chars = []
        self.target_word = ['a', 'p', 'p', 'l', 'e']
        self.correct_chars = ['_'] * len(self.target_word)
    
    def get_words_list(self):
        with open(self.filename) as file:
            for line in file:
                self.eng_words.append(line.strip())
    
    def pick_word(self):
        self.target_word = list(choice(self.eng_words))
        n = len(self.target_word)
        self.correct_chars = ['_'] * n
    
    def char_input(self):
        while True:
            char = input('Type in an english letter: ').lower()
            if char == '' or char not in ascii_lowercase:
                print('>> That is not a valid letter. Please try again')
                print()
            else:
                if char in self.user_chars:
                    print('>> You\'ve already picked that letter. Plese try another letter.')
                    print()
                else:
                    return char
                
    def check_char(self, char):
        if char in self.target_word:
            return True
        self.user_chars.append(char)
        return False
    
    def is_correct_char(self, char):
        for i in range(len(self.target_word)):
            if self.target_word[i] == char:
                self.correct_chars[i] = char

    def check_score(self):
        if self.target_word == self.correct_chars:
            print()
            print('>> you\'ve won the game!')
            return True
        if len(self.hangman_pic) == 1:
            print()
            print('>> You lost! Try again next time.')
            return True
        return False

    def display_round(self):
        print()
        print('[ ', end='')
        print(', '.join(self.user_chars), end='')
        print(' ]')
        print()
        pic = self.hangman_pic[-1]
        print(pic)
        print()
        print(' '.join(self.correct_chars))
        print()

    def execute(self):
        #self.get_words_list()
        #self.pick_word()
        print()
        print('Welcome to Hangman! Let\'s play a game.')
        while True:
            self.display_round()
            if self.check_score():
                break
            char = self.char_input()
            if self.check_char(char):
                self.is_correct_char(char)
                print('>> That is correct!')
            else:
                self.hangman_pic.pop()
                print('>> That is incorrect.')
            

play_hangman = Hangman('english-nouns.txt')
play_hangman.execute()