from customer import Customer

class BankAccount: 


    def __init__(self, owner: Customer, first_deposit: float, interest: float):
        self.__owner = owner
        self._balance = first_deposit
        self.__interest = interest
        self._type = "Standard Bank Account"
        owner.add_bank_account(self)

    def withdraw_money(self, amount):
        if amount > self._balance:
            print(f"\tBezug von {self.type}")
            print(f"\tFehler: Bezug ist zu hoch für Saldo von {self.balance}")
        else:
            print(f"\tBezug von {self.type}")
            self._balance -= amount
            print(f"\tSaldo = {self.balance}")

    def pay_in_money(self, amount):
        self._balance += amount
    
    @property
    def balance(self):
        return self._balance
    
    @property
    def owner(self):
        return self.__owner

    @property
    def type(self):
        return self._type

    @property
    def interest(self):
        return self.__interest

    @interest.setter
    def interest(self, value):
        self.__interest = value

    def print(self):
        print("""Kundennamen: {self.owner.name}
Saldo: {self.balance}
Zinssatz: {self.interest}""")

