class Animal:
	def eat(self):
		print('-eat--')

class Dog(Animal):
	pass

a = Animal()
a.eat()

wangcai = Dog()
wangcai.eat()
