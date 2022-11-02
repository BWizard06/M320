'''
Die Klasse Musician beschreibt einen allgemeinen Musiker, der ein Instrument spielt.
'''
from child_classes import *

class Musician():
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name


    def what_I_do(self):
        '''
        Der Musiker mit Name name sagt, was er für ein Instrument spielt. Das weiss aber nur die konkrete klasse
        '''
        pass


if __name__ == "__main__":
    musicians = []
    musicians.append(Guitarist("Marc"))
    musicians.append(Pianist("Roger"))
    musicians.append(Drummer("Phil"))
    for m in musicians:
        m.what_I_do()
