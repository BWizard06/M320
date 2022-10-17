class BankAccount:
    """
    Der Bezug ist solange möglich, wie auf dem
    Konto ein Saldo vorliegt der nicht negativer als
    der definierte Überzug ist. D.h. dass ein Kunde
    auch einen negativen Saldo haben kann, aber
    eben nur in begrenztem Mass.
    """

    def __init__(self, max_overdraft, customer):
        """
        :param overdraft:
        :param customer:
        """

        self.__balance = 0.0
        self.__overdraft = max_overdraft
        self.__customer = customer

    def booking(self, amount):
        """
        :param amount:
        :return:
        """
        self.__balance += amount

    def get_money(self, amount):
        if amount > (self.__balance + self.__overdraft):
            return amount == 0.0
        else:
            self.__balance -= amount
        return amount


    def get_balance(self):
        return self.__balance

    def get_overdraft(self):
        return self.__overdraft

    def get_customer(self):
        return self.__customer






class Bottle:
    """
    Das Fassungsvermögen wird bei der Erzeugung
    einmalig gesetzt, darum gibt es keine set‐
    Methode.
    Mit fuellen() wird die Flasche immer bis zum
    Fassungsvermögen gefüllt. Bei entnehmen()
    wird maximal die angegeben Menge
    entnommen. Weist die Trinkflasche weniger
    Inhalt auf, wird einfach der Rest ausgegeben.
    """

    def __init__(self, color, capacity):
        """
        :param color:
        :param capacity:
        """
        self.__color = color
        self.__capacity = capacity
        self.__quantity_available = 0.0

    def get_color(self):
        return self.__color

    def get_quantity_available(self):
        return self.__quantity_available

    def get_capacity(self):
        return self.__capacity

    def open_bottle(self):
        pass

    def close_the_bottle(self):
        pass

    def fill_bottle(self):
        self.__quantity_available = self.__capacity

    def get_liquid(self, amount):
        if amount > self.__quantity_available:
            amount = self.__quantity_available
            self.__quantity_available = 0.0
        else:
            self.__quantity_available -= amount
        return amount


