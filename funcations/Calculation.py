#!/usr/bin/python3.6
def cmul(*num ):
    sum = 1
    for i in num:
        sum *= i
    return sum

print(eval("cmul({})".format(input())))
