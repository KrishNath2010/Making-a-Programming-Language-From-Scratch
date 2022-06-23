# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 10:22:24 2022

@author: Krish Nath
"""
s = "MMMCDXLXXVVVVVVVVVIIIIIIIIIIIIIIIIII"
l = list(s)
number = 0
I_poss = True
X_poss = True
C_poss = True

# Changes the value of number based on what the value is
def normal(val):
    global number, I_poss, X_poss, C_poss
    number += val
    I_poss = True
    X_poss = True
    C_poss = True

# Changes the value of number based on what the value is and what the next and preevious letters are
def poss(n1, n2, val, i, x, c, index):
    global number, I_poss, X_poss, C_poss
    do = True
    if i != True:
        I_poss = True
    if x != True:
        X_poss = True
    if c != True:
        C_poss = True
    if i == True and (I_poss == False):
        number += val
        do = False
    if x == True and (X_poss == False):
        number += val
        do = False
    if c == True and (C_poss == False):
        number += val
        do = False
    if do == True:
        try:
            if(l[index + 1] == n1 or l[index + 1] == n2):
                number -= val
                if i == True:
                    X_poss = False
                if x == True:
                    C_poss = False
            else:
                number += val
        except:
            number += val

# Call the two functions above based on what letters there are
def run(index):
    if l[index] == "I":
        poss("V", "X", 1, True, False, False, index)
    elif l[index] == "V":
        normal(5)
    elif l[index] == "X":
        poss("L", "C", 10, False, True, False, index)
    elif l[index] == "L":
        normal(50)
    elif l[index] == "C":
        poss("D", "M", 100, False, False, True, index)
    elif l[index] == "D":
        normal(500)
    else:
        normal(1000)
    if index < len(l)-1:
        run(index + 1)

run(0)
print("Answer:", number)