'''
Ergänzen Sie hier die 3 Klassen Gutarist, Pianist und Drummer.
Die Ausgabe der Anwendung muss wie folgt aussehen:
ich Marc spiel Gitarre
ich Roger spiel Piano
ich Phil spiel Schlagzeug
'''
from musician import Musician

class Guitarist(Musician):

    def __init__(self, name):
        super().__init__(name)

    def what_I_do(self):
        print(f"ich {self.name} spiel Gitarre")

class Pianist(Musician):
    
    def __init__(self, name):
        super().__init__(name)

    def what_I_do(self):
        print(f"ich {self.name} spiel Piano")

class Drummer(Musician):
        
    def __init__(self, name):
        super().__init__(name)

    def what_I_do(self):
        print(f"ich {self.name} spiel Schlagzeug")