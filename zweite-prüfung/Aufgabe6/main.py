from abc import ABC, abstractmethod

class BottleCollection:

    def __init__(self):
        self.__bottles = []

    def add_bottle(self, bottle):
        self.__bottles.append(bottle)

    def inventory(self):
        return self.__bottles

class Bottle(ABC):
    
    def __init__(self, shutter_type, content):
        self._shutter_type = shutter_type
        self._content = content

    @abstractmethod
    def open_bottle(self):
        pass

    @property
    def shutter_type(self):
        return self._shutter_type

    @property
    def content(self):
        return self._content

class WineBottle(Bottle):

    def __init__(self, shutter_type, content):
        super().__init__(shutter_type, content)

    def open_bottle(self):
        print(f"öffnen: {self.shutter_type} ziehen")

class BeerBottle(Bottle):
    
    def __init__(self, shutter_type, content):
        super().__init__(shutter_type, content)

    def open_bottle(self):
        print(f"öffnen: {self.shutter_type} anheben")

class WaterBottle(Bottle):

    def __init__(self, shutter_type, content):
        super().__init__(shutter_type, content)

    def open_bottle(self):
        print(f"öffnen: {self.shutter_type} aufdrehen")

if __name__ == "__main__":

    collection = BottleCollection()
    
    wein = WineBottle("Korken", "Wein")
    bier = BeerBottle("Kronenkorken", "Bier")
    wasser = WaterBottle("Drehverschluss", "Wasser")

    collection.add_bottle(wein)
    collection.add_bottle(bier)
    collection.add_bottle(wasser)

    for bottle in collection.inventory():
        print(f"{bottle.shutter_type}-Flasche mit {bottle.content}")
        bottle.open_bottle()




    

    
