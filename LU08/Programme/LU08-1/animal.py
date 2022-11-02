import imp


from abc import ABC, abstractmethod

class Animal(ABC): 
    def __init__(self, species):
        self._species = species

    @abstractmethod
    def move(self):
        pass