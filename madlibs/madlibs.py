
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

    def get_word_gen(self, word_type: str):
        word_list = self.inputs.get(word_type, None)
        return (word for word in word_list) if word_list else None
    
    def concat(self):
        adj = self.get_word_gen('adjective')
        noun = self.get_word_gen('noun')
        place = self.get_word_gen('place')
        vehicle = self.get_word_gen('vehicle')
        pl_noun = self.get_word_gen('plural noun')
        verb = self.get_word_gen('verb')
        job = self.get_word_gen('job')
        madlibs = (
            f"Star Wars is a {next(adj) if adj else 'n/a'} {next(noun) if noun else 'n/a'} of {next(adj) if adj else 'n/a'} versus evil in a/an {next(place) if place else 'n/a'} far far away.\n"
            f"There are {next(adj) if adj else 'n/a'} battles between {next(adj) if adj else 'n/a'} {next(vehicle) if vehicle else 'n/a'} in {next(adj) if adj else 'n/a'} space"
            f" and {next(adj) if adj else 'n/a'} duels with {next(pl_noun) if pl_noun else 'n/a'} called {next(adj) if adj else 'n/a'} sabers.\n"
            f"{next(pl_noun).capitalize() if pl_noun else 'n/a'} called 'droids' are helpers and {next(pl_noun) if pl_noun else 'n/a'} to the heroes.\n"
            f"A {next(adj) if adj else 'n/a'} power called The {next(noun).title() if noun else 'n/a'} {next(verb) if verb else 'n/a'}s people to do {next(adj) if adj else 'n/a'} things,"
            f" like {next(verb) if verb else 'n/a'} {next(pl_noun) if pl_noun else 'n/a'}.\n"
            f"The Jedi {next(job) if job else 'n/a'} use The Force for the {next(adj) if adj else 'n/a'} side and the Sith {next(verb) if verb else 'n/a'} it for the {next(adj) if adj else 'n/a'} side."
        )
        return madlibs
        
    def execute(self):
        self.get_input()
        print(self.concat())

madlib_a = Madlib()
madlib_a.execute()
