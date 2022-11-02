class Customer:

    def __init__(self):
        self.__customer_age = 0.0

    def set_age(self, age):
        if age < 0 or age > 120:
                raise AgeValueException(age)
        else:
            print(f"{age} ist ein gültiges Alter")
            self.__customer_age = age

class AgeValueException(Exception):

    def __init__(self, age):
        super().__init__(f"ERROR: {age} ist ein ungültiges Alter!")

if __name__ == "__main__":
    customer = Customer()
    age = int(input("Geben Sie Ihr Alter ein: "))   
    try:
        customer.set_age(age)
    except AgeValueException as age:
        print(age)