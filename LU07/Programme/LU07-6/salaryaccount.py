from bankaccount import BankAccount
from customer import Customer

class SalaryAccount(BankAccount):
    
    def __init__(self, owner: Customer, first_deposit, interest, overdraw):
        super().__init__(owner, first_deposit, interest)
        self._type = "Salary Account"
        self.__overdraw = overdraw

    @property
    def overdraw(self):
        return self.__overdraw

    @overdraw.setter    
    def overdraw(self, amount):
        self.__overdraw += amount

# es muss noch kontrolliert werden, ob es auch über den Überzug geht
    def withdraw_money(self, amount):
        print(f"\tBezug von {self.type}")
        if self.balance - amount >= 0:
            self._balance -= amount
        else:
            self._balance -= amount
            self.overdraw += abs((self.balance - amount))
        print(f"\tSaldo = {self.balance}")

    def print(self):
        super().print()
        print(f"Überziehung: {self.overdraw}")
    