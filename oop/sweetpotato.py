#!/usr/bin/python3
class SweetPotato:

    def __init__(self):
        self.CookedString = "生的"
        self.CookedLevel = 0
        self.condiments = []
    def __str__(self):
        return "地瓜状态：%s(%d)，添加的作料有：%s"%(self.CookedString,self.CookedLevel,str(self.condiments))

    def cook(self,Cooked_time):

        self.CookedLevel += Cooked_time

        if self.CookedLevel >=0 and self.CookedLevel < 3:
            self.CookedString = "生的"
        elif self.CookedLevel >=3 and self.CookedLevel < 5:
            self.CookedString = "半生不熟"
        elif self.CookedLevel >=5 and self.CookedLevel < 8:
            self.CookedString = "烤熟了"
        elif self.CookedLevel >= 8:
            self.CookedString = "烤糊了"

    def AddCondiments(self,item):
        self.condiments.append(item)

#创建了一个地瓜对象
di_gua = SweetPotato()

#开始烤地瓜
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.AddCondiments("大蒜")
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
di_gua.AddCondiments("孜然")
print(di_gua)
di_gua.cook(1)
di_gua.AddCondiments("香油")
print(di_gua)

