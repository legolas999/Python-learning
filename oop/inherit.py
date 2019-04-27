#!/usr/bin/python3.6
class Animal:
	def eat(self):
		print('-eat--')

class Dog(Animal):   #Dog类是Animal的子类
	def bark(self):
		print("{:=^30}".format("旺旺叫"))

class Xiaotanquan(Dog):  #Xiaotanquan类是Dog类的子类
	def fly(self):
		print("---flying---")

a = Animal()
a.eat()

wangcai = Dog()
print("调用父类的方法")
wangcai.eat()
wangcai.bark()

xiaotq = Xiaotanquan()
xiaotq.fly()
print("调用父类的方法")
xiaotq.bark()
print("调用父类的父类的方法")
xiaotq.eat()
#查看类调用方法的顺序
print(Xiaotanquan.__mro__)

