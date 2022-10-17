# In der Theorie haben Sie gelernt, wie mit der Methode isinstance die
# Zugehörigkeit eines Objekts zu einer Klasse festgestellt werden kann
# und wie mit dem Operator is geprüft wird, ob Referenzen identisch sind.
# Der folgende Code geht noch ein bisschen weiter. Sie sollen den Code
# studieren und sein Verhalten erklären. Dazu kann es notwendig sein,
# dass Sie sich über passende Suchbegriffe im Internet "schlau" machen.
class ObjectIdentity:

    def __init__(self, value):
        """
        Erzeugt ein Objekt mit dem Wert des Parameters value
        :param value: ein beliebiger Text
        """
        self.text = value

    @property
    def text(self):
        """
        Liefert den Wert des Attributs
        :return: aktueller Text
        """
        return self.__text

    @text.setter
    def text(self, value):
        """
        Schreibt den Wert von value ins Attribut.
        :param value: ein beliebiger Text
        """
        self.__text = value


if __name__ == "__main__":
    # erzeugen Sie hier 2 Objekt obj1 und obj2 der Klasse ObjectIdentity.
    # do it
    obj1 = ObjectIdentity("Hallo")
    obj2 = ObjectIdentity("Hallo")

    ##
    # prüfen der Klassenzugehörigkeit von obj1 zur Klasse ObjectIdentity
    # Geben Sie je nach Testergebnis einen passenden Text aus.
    # do it
    if isinstance(obj1, ObjectIdentity):
        print("Objekt 1 ist von der Klasse ObjectIdentity")
    else: 
        print("Das Objekt 1 ist nicht von der Klasse ObjectIdentity")

    ##
    # prüfen Sie, ob die beiden Objekte obj1 und obj2 identisch sind.
    # Geben Sie je nacht Testergebnis einen passenden Text aus.
    # do it
    if obj1 is obj2:
        print("Objekt 1 und 2 sind identisch")
    else: 
        print("Das Objekt1 ist nicht identisch mit Objekt2")

    ##
    # prüfen Sie hier den Inhalt (das Attribut) der beiden Objekte auf Gleichheit.
    # Wenn Ihnen nicht klar ist, wie man das macht, suchen Sie im Internet nach Lösungen.
    # do it
    if obj1.text == obj2.text:
        print("Sie haben den gleichen Inhalt")
    else:
        print("Sie haben nicht den gleichen Inhalt")