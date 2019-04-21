#!/usr/bin/python3
#CalBMIv3.py
height,weight = eval(input("请输入身高（米）和体重\（公斤）[逗号隔开]："))
bmi = weight / pow(height,2)
print("BMI 数值为:{:.2f}".format(bmi))
who,nat = "",""
if bmi < 18.5:
	who = "偏瘦"
	nat = "偏瘦"
elif 18.5 <= bmi < 24:
	who = "正常"
	nat = "正常"
elif 24 <= bmi < 25:
	who = "正常"
	nat = "偏胖"
elif 25 <= bmi < 28:
	who = "偏胖"
	nat = "偏胖"
elif 28 <= bmi < 30:
	who = '偏胖'
	nat = '肥胖'
else:
	who = '肥胖'
	nat = '肥胖'
print("BMI 指标：国际'{}';国内'{}'".format(who,nat))
	
print("BMI 指标为：国际'{0}'".format(who))
