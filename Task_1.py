# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 21:41:07 2022

@author: Krish Nath
"""

def VALint(i: int) -> int:
    return i
def VALbool(i: bool) -> bool:
    return i
def TMOpr(opr: str, v1, v2):
    if opr == "+":
        return VALint(v1 + v2)
    elif opr == "-":
        return VALint(v1 - v2)
    elif opr == "*":
        return VALint(v1 * v2)
    elif opr == "/":
        return VALint(v1 / v2)
    elif opr == ">=":
        return VALbool(v1 >= v2)
    elif opr == ">":
        return VALbool(v1 > v2)
    elif opr == "<=":
        return VALbool(v1 <= v2)
    elif opr == "<":
        return VALbool(v1 < v2)
    elif opr == "==":
        return VALbool(v1 == v2)
    elif opr == "!=":
        return VALbool(v1 != v2)
#print(TMOpr("-",9,8))    