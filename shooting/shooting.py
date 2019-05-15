#!/usr/bin/python3.6
class Person(object):
	'''人的类'''
	def __init__(self,name):
		super(Person,self).__init__()
		self.name = name
		self.gun = None
		self.hp = 100
	def use_bullet(self,cartridge_clip_temp,bullet_temp):
		'''把子弹装到弹夹中'''
		#弹夹.保存子弹（子弹）
		cartridge_clip_temp.storing_bullets(bullet_temp)

	def use_cartridge_clip(self,gun_temp,cartridge_clip_temp):
		'''把弹夹安装到枪中'''
		#枪.保存弹夹（弹夹）
		gun_temp.storing_cartridge_clip(cartridge_clip_temp)
	def use_gun(self,gun_temp):
		self.gun=gun_temp
	def __str__(self):
		if self.gun:
			return "{}的血量为：{},他有枪,{}".format(self.name,self.hp,self.gun)
		else:
			if self.hp>0:
				return "{}的血量为：{},他没有枪".format(self.name,self.hp)
			else:
				return "{}已经挂了.....".format(self.name)

	def kou_ban_ji(self,diren):
		'''让枪发射子弹去打敌人'''
		#枪.开火（敌人）
		self.gun.fire(diren)
	def diao_xue(self,lethality):
		'''根据杀伤力，掉相应的血量'''
		self.hp -= lethality

class Gun(object):
	'''枪类'''
	def __init__(self,name):
		super(Gun,self).__init__()
		self.name = name #用来记录枪的类型
		self.cartridge_clip = None #用来记录弹夹对象的引用

	def storing_cartridge_clip(self,cartridge_clip_temp):
		'''用一个属性来保存这个弹夹对象的引用'''
		self.cartridge_clip = cartridge_clip_temp

	def __str__(self):
		if self.cartridge_clip:
			return "枪的信息为:{},{}".format(self.name,self.cartridge_clip)
		else:
			return "枪的信息为:{},这把枪中没有弹夹".format(self.name)
	def fire(self,diren):
		'''枪从弹夹中获取一发子弹，然后让子弹去击中敌人'''
		#先从弹夹中取子弹
		zidan_temp = self.cartridge_clip.tanchu_zidan()


		#让这个子弹去伤害敌人
		if zidan_temp:
			zidan_temp.dazhong(diren)
		else:
			print("弹夹中没有子弹了....")


class Cartridge_clips(object):
	'''弹夹类'''
	def __init__(self, max_num):
		super(Cartridge_clips,self).__init__()
		self.max_num = max_num #用来记录弹夹的最大容量
		self.bullet_list = [] #用来记录所有子弹的引用

	def storing_bullets(self,bullet_temp):
		'''将子弹存储到弹夹'''
		self.bullet_list.append(bullet_temp)

	def __str__(self):
		return "弹夹的信息为：{}/{}".format(len(self.bullet_list),self.max_num)		
	def tanchu_zidan(self):
		"""弹出最上面的那颗子弹"""
		if self.bullet_list:
			return self.bullet_list.pop()
		else:
			return None

class Bullets(object):
	'''子弹类'''
	def __init__(self,lethality):
		super(Bullets,self).__init__()
		self.lethality = lethality #表示子弹的杀伤力
	def dazhong(self,diren):
		'''让敌人掉血'''
		#敌人.掉血（一颗子弹的威力）
		diren.diao_xue(self.lethality)

def main():
	'''用来控制整个程序的流程'''
	
	#1. 创建老王对象
	laowang = Person('老王')

	#2. 创建一个枪对象
	ak47 = Gun('AK47')

	#3. 创建一个弹夹对象
	cartridge_clip = Cartridge_clips(20)

	#4. 创建一些子弹
	for i in range(15):
		bullet = Bullets(10)


		#5. 老王把子弹安装到弹夹中
		laowang.use_bullet(cartridge_clip,bullet)

	#6. 老王把弹夹安装到枪中
	#老王。安装弹夹到枪中（枪，弹夹）
	laowang.use_cartridge_clip(ak47,cartridge_clip)
	
	#test:测试弹夹的信息
	print(cartridge_clip)
	#test：测试枪的信息
	print(ak47)

	#7. 老王拿枪
	#老王.拿枪（枪）
	laowang.use_gun(ak47)
	#测试老王信息
	print(laowang)

	#8. 创建一个敌人

	gebi_laosong = Person('隔壁老宋')

	print(gebi_laosong)

	#9. 老王开枪打敌人
	#老王.扣扳机（隔壁老宋）
	for i in range(15):
		laowang.kou_ban_ji(gebi_laosong)
		print(gebi_laosong)
		print(laowang)

if __name__ == '__main__':
	main()
