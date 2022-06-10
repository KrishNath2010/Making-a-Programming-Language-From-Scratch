# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 11:37:39 2022

@author: Krish Nath
"""

def fac(a):
    if (a==1 or a==0):
            return 1
    return a*fac(a-1)
sums=-3
for i in range(10000000):
    if (i<100 and i>50) or (i<1000 and i>700) or (i<10000 and i>8000) or (i<100000 and i>90000):
        continue
    use=list(str(i))
    num=0
    if (i%1000000==0):
        print("t")
    for j in use:
        num+=fac(int(j))
    if i==num:
        sums+=i
        print(i)
print(sums)
    