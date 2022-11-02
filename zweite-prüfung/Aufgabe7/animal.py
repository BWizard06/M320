
from abc import ABC, abstractmethod

class Animal:
    '''
    Ein allgemeines Tier, das weiss, dass es einer Spezies angehört und einen Laut von sich geben kann.
    '''
    def __init__(self, species):
        self._species = species


    @property
    def species(self):
        return self._species

    @abstractmethod
    def I_sound_like_that(self):
        pass
#----------------------------------------------------
# hier die Klassen für Bird, Cow, Lion und Wolf erstellen.

class Bird(Animal):

    def I_sound_like_that(self):
        print(f"{self.species}: zwitschert")

class Cow(Animal):
    
    def I_sound_like_that(self):
        print(f"{self.species}: muht")

class Lion(Animal):
        
    def I_sound_like_that(self):
        print(f"{self.species}: brüllt")

class Wolf(Animal):
        
    def I_sound_like_that(self):
        print(f"{self.species}: heult")
    


#-----------------------------------------------------
if __name__ == "__main__":
    animal = None
    print("Wie tönt ein Tier?")
    print("Geben Sie einen Buchstaben ein, um sich das Tier anzuhören.")
    print("\tB für Vogel (bird)")
    print("\tC für Kuh (cow)")
    print("\tL für Löwe (lion)")
    print("\tW für Wolf (wolf)")
    value = input("Bitte Ihre Wahl: ")
    # und nun die Ausgabe auswerten.
    # Wird ein gütltiges Zeichen erkannt, kann auf Grund der Eingabe das
    # passende Objekt erzeugt werden. Dazu das Attribut animal benutzen.
    # Das Tier kann dann seinen Laut von sich geben. Dabei die Regeln guter OOP berücksichtigen!
    # Wird ein ungültiges Zeihen geliefert, muss eine sinnvolle Fehlermeldung ausgegeben werden.
    if value == "B":
        animal = Bird("Vogel")
    elif value == "C":
        animal = Cow("Kuh")
    elif value == "L":
        animal = Lion("Löwe")
    elif value == "W":
        animal = Wolf("Wolf")
    else:
        print(f"{value} ist eine ungültige Eingabe!")
        exit(1)

    animal.I_sound_like_that()