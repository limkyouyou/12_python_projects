from random import choice
from string import ascii_lowercase

class Hangman():
    def __init__(self, filename):
        self.filename = filename
        self.hangman_pic = [
            "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========", 
            "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========", 
            "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="
          ]
        self.eng_words = []
        self.user_chars = []
        self.target_word = None
        self.correct_chars = []
    
    def get_words_list(self):
        with open(self.filename) as file:
            for line in file:
                self.eng_words.append(line.strip())
    
    def pick_word(self):
        self.target_word = list(choice(self.eng_words))
    
    def char_input(self):
        while True:
            char = input('Type in an english letter: ').lower()
            if char not in ascii_lowercase:
                print('That is not a valid letter. Please try again')
            else:
                if char in self.user_chars:
                    print('You\'ve already picked that letter. Plese try another letter.')
                else:
                    return char
                
    def check_char(self, char):
        if char in self.target_word:
            return True
        self.user_chars.append(char)
        return False
    
    def check_score(self):
        
            