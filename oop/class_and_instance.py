#!/usr/bin/python3.6

class Game(object):
	#类属性
	num = 0

	#实例方法
	def __init__(self):
		#实例属性
		self.name = 'zhanshi'


	#类方法
	@classmethod
	def add_num(cls):
		cls.num += 1

	#静态方法
	@staticmethod
	def print_menu():
		print('*'* 30)
		print('{:^30}'.format("穿越火线V11.1"))
		print('{:^30}'.format("1.开始游戏"))
		print('{:^30}'.format("2.结束游戏"))
		print('*'* 30)

game = Game()
#可以通过类的名字调用类方法
Game.add_num()
print(Game.num)
#也可以通过这个类创建出来的实例对象调用这个类方法
game.add_num()
print(Game.num)

Game.print_menu()   #通过类去调用静态方法
game.print_menu()   #也可以通过实例对象调用静态方法
		
