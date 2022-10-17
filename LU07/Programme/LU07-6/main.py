from cmath import pi
from bankaccount import BankAccount
from customer import Customer
from salaryaccount import SalaryAccount

if __name__ == "__main__":
    customer = Customer("Pia", 23)
    customer.adress = "Hochdorf"
    account1 = BankAccount(customer, 1000.0, 1.25)
    account2 = SalaryAccount(customer, 1000.0, 2.25, 500)
    customer.print()

    print("\nVon jedem Konto 750.0 beziehen")
    account1.withdraw_money(750.0)
    account2.withdraw_money(750.0)
    print(f"Aktuelles Vermögen: {customer.current_assets()}")

    print("\nVon jedem Konto noch einmal 400.0 beziehen")
    account1.withdraw_money(400.0)
    account2.withdraw_money(400.0)
    print(f"Aktuelles Vermögen: {customer.current_assets()}")

    print("\nEnde Monat: der Lohn wird eingezahlt")
    account2.pay_in_money(3000.0)
    print(f"Aktuelles Vermögen: {customer.current_assets()}")


