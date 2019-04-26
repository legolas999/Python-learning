class Dog:
	def __init__(self,new_name):
		self.name = new_name
		self.__age = 0
	def get_age(self):
		return self.__age

dog =Dog("black")
print(dog.name)
print(dog.get_age())
