# Führen Sie diese Anwendung aus!
# Wenn Sie alle Klassen korrekt erstellt haben, muss folgende Anzeige resultieren:
# gehe von Zürich nach Bern
# mit 150 l im Tank
# und transportiere Eier
# -----
# gehe von Chur nach Bellinzona
# mit 60 l im Tank
#
# erstellen Sie die drei Klassen in einer Datei mit Namen classes.py!


from classes import Truck, Automobile

if __name__ == "__main__":
    truck = Truck("Zürich", "Bern", 150, "Eier")
    truck.from_to()
    truck.fuel_avaiable()
    truck.transport()
    print("-----")
    auto = Automobile("Chur", "Bellinzona", 60)
    auto.from_to()
    auto.fuel_avaiable()
