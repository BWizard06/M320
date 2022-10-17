class House:

	def __init__(self, type = "Landhaus"):
		self.__type = type

	@property
	def type(self):
		return self.__type


class HomeOwner:

	def __init__(self, name, house):
		self.__name = name
		self.__my_house = house

	@property
	def name(self):
		return self.__name

	@property
	def house(self):
		return self.__house


	def print(self):
		print(f"{self.__name} besitzt ein {self.__my_house.type} ")


if __name__ == "__main__":
	home = House()
	owner = HomeOwner("Ron", home)
	owner.print()


	


	

		