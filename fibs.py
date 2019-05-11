#!/usr/bin/python3.6
def fbi(n):
    fbis = [1,1]
    for i in range(n-2):
        fbis.append(fbis[-2]+fbis[-1])
    return str(fbis)

n = eval(input())
print(fbi(n))
