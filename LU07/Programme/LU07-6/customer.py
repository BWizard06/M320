from person import Person

class Customer(Person):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.__accounts = []

    def current_assets(self):
        assets = 0
        for account in self.__accounts:
            assets += account.balance
        return assets

    @property
    def account_number(self):
        return len(self.__accounts)

    def bank_account(self, index):
        return self.__accounts[index]

    def add_bank_account(self, account):
        self.__accounts.append(account)

    def print(self):
        super().print()
        print(f"Angaben zu den Konti:")
        for account in self.__accounts:
            print(f"\t{account.type}")
        
