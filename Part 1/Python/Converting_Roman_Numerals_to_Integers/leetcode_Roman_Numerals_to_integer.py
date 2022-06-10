# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 10:22:24 2022

@author: Krish Nath
"""
s="MCMVXIII"
l=list(s)
number=0
I_poss=True
X_poss=True
C_poss=True
for index in range(len(l)):
    if l[index]=="I":
        X_poss=True
        C_poss=True
        if (I_poss==False):
            number+=1
        else:
            try:
                if(l[index+1]=="V"or l[index+1]=="X"):
                    number-=1
                    X_poss=False
                else:
                    number+=1
            except:
                number+=1
    elif l[index]=="V":
        number+=5
        I_poss=True
        X_poss=True
        C_poss=True
    elif l[index]=="X":
        I_poss=True
        C_poss=True
        if (X_poss==False):
            number+=10
        else:
            try:
                if(l[index+1]=="L"or l[index+1]=="C"):
                    number-=10
                    C_poss=False
                else:
                    number+=10
            except:
                number+=10
    elif l[index]=="L":
        number+=50
        I_poss=True
        X_poss=True
        C_poss=True
    elif l[index]=="C":
        I_poss=True
        X_poss=True
        if (C_poss==False):
            number+=100
        else:
            try:
                if(l[index+1]=="D"or l[index+1]=="M"):
                    number-=100
                else:
                    number+=100
            except:
                number+=100
    elif l[index]=="D":
        number+=500
        I_poss=True
        X_poss=True
        C_poss=True
    else:
        number+=1000
        I_poss=True
        X_poss=True
        C_poss=True
print(number)