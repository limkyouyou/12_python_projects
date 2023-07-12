
#Mad libs template referenced from https://swantonpubliclibrary.org/sites/default/files/mad%20lib%20star%20wars.jpg - WooJr.com All Rights Reserved

class Madlib:
    def __init__(self):
        self.variables = [('Adjective', 11), ('Noun', 2), ('Plural Noun', 4), ('Place', 1), ('Vehicle', 1), ('Verb', 3), ('Job', 1)]
        self.inputs = {}

    def get_input(self):
        for item in self.variables:
            word_list = []
            for i in range(item[1]):
                word = input(f'{item[0]}: ')
                word_list.append(word)
            self.inputs[item[0].lower()] = word_list

    def get_word(self, word_type: str):
        
        word_list = self.inputs.get(word_type, None)
        word = ''
        if word_list:
            word = word_list.pop()
        return word if word else 'n/a'
    
    def concat(self):
        madlibs = (
            f"Star Wars is a {self.get_word('adjective')} {self.get_word('noun')} of {self.get_word('adjective')} versus evil in a/an {self.get_word('place')} far far away.\n"
            f"There are {self.get_word('adjective')} battles between {self.get_word('adjective')} {self.get_word('vehicle')} in {self.get_word('adjective')} space"
            f" and {self.get_word('adjective')} duels with {self.get_word('plural noun')} called {self.get_word('adjective')} sabers.\n"
            f"{self.get_word('plural noun').capitalize()} called 'droids' are helpers and {self.get_word('plural noun')} to the heroes.\n"
            f"A {self.get_word('adjective')} power called The {self.get_word('noun').capitalize()} {self.get_word('verb')}s people to do {self.get_word('adjective')} things,"
            f" like {self.get_word('verb')} {self.get_word('plural noun')}.\n"
            f"The Jedi {self.get_word('job')} use The Force for the {self.get_word('adjective')} side and the Sith {self.get_word('verb')} it for the {self.get_word('adjective')} side."
        )
        return madlibs
        
    def execute(self):
        self.get_input()
        print(self.concat())

madlib_a = Madlib()
madlib_a.execute()
