# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 14:45:18 2022

@author: Krish Nath
"""


import math
class Neg:
    def __init__(self,p):
        self.p = p
    def __repr__(self):
        return "- ( " + repr(self.p) + " )"
    def simplify(self):
        if isinstance(self, Int):
            return Int(-1 * int(self.p.simplify()))
        return Mul.simplify(Mul(Int(-1), self))
class Pow:
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
    def __repr__(self):
        if isinstance(self.p1, Pow)!=True and isinstance(self.p1, Int)!=True and isinstance(self.p1, X)!=True:
            if isinstance(self.p2, Pow)!=True and isinstance(self.p2, Int)!=True and isinstance(self.p2, X)!=True:
                 return "( " + repr(self.p1) + " ) ^ ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) ^ " + repr(self.p2)
        if isinstance(self.p2, Pow)!=True  and isinstance(self.p2, Int)!=True and isinstance(self.p2, X)!=True:
            return repr(self.p1) + " ^ ( " + repr(self.p2) + " )"
        return repr(self.p1) + " ^ " + repr(self.p2)
    def simplify(self):
        simp1 = self.p1.simplify()
        simp2 = self.p2.simplify()
        if isinstance(simp1, Int):
            if simp1.i == 0:
                return Int(0)
            if simp1.i == 1:
                return Int(1)
            if isinstance(simp2, Int):
                return Int(math.pow(simp1.i, simp2.i))
            if isinstance(simp2, Pow):
                if isinstance(simp2.p1, Int):
                    return Pow(Int(math.pow(simp1.i, simp2.p1.i)), simp2.p2.simplify())
                if isinstance(simp2.p2, Int):
                    return Pow(Int(math.pow(simp1.i * simp2.p2.i)), simp2.p1.simplify())
        if isinstance(simp2, Int):
            if simp2.i == 0:
                return Int(1)
            if simp2.i == 1:
                return simp1
            if isinstance(simp1, Int):
                return Int(math.pow(simp1.i, simp2.i))
            if isinstance(simp1, Pow):
                if isinstance(simp1.p1, Int):
                    return Pow(Int(math.pow(simp2.i, simp1.p1.i)), simp2.p2.simplify())
                if isinstance(simp1.p2, Int):
                    return Pow(Int(math.pow(simp2.i, simp1.p2.i)), simp2.p1.simplify())
        return Pow(simp1, simp2)
class Error:
    def __init__(self):
        pass
    def divby0(self):
        return 1/0
class X:
    def __init__(self,poss,val):
        if poss==True:
            self.val=str(val)
        else:
            self.val="no"
        pass

    def __repr__(self):
        if self.val=="no":
            return "X"
        else:
            return self.val

    def simplify(self):
        if self.val=="no":
            return self
        else:
            return Int(int(self.val))


class Int:
    def __init__(self, i):
        self.i = int(i)

    def __repr__(self):
        return str(self.i)

    def simplify(self):
        return self


class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p1, Add) or isinstance(self.p1, Sub) or isinstance(self.p1, Div):
            if isinstance(self.p2, Add) or isinstance(self.p2, Sub) or isinstance(self.p2, Div):
                 return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, Add) or isinstance(self.p2, Sub) or isinstance(self.p2, Div):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
        return repr(self.p1) + " * " + repr(self.p2)

    def simplify(self):
        simp1 = self.p1.simplify()
        simp2 = self.p2.simplify()
        if isinstance(simp1, Int):
            if simp1.i == 0:
                return Int(0)
            if simp1.i == 1:
                return simp2
            if isinstance(simp2, Int):
                return Int(simp1.i * simp2.i)
            if isinstance(simp2, Mul):
                if isinstance(simp2.p1, Int):
                    return Mul(Int(simp1.i * simp2.p1.i), simp2.p2.simplify())
                if isinstance(simp2.p2, Int):
                    return Mul(Int(simp1.i * simp2.p2.i), simp2.p1.simplify())
        if isinstance(simp2, Int):
            if simp2.i == 0:
                return Int(0)
            if simp2.i == 1:
                return simp1
            if isinstance(simp1, Int):
                return Int(simp1.i * simp2.i)
            if isinstance(simp1, Mul):
                if isinstance(simp1.p1, Int):
                    return Mul(Int(simp2.i * simp1.p1.i), simp2.p2.simplify())
                if isinstance(simp1.p2, Int):
                    return Mul(Int(simp2.i * simp1.p2.i), simp2.p1.simplify())
        return Mul(simp1, simp2)
class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p1, Add) or isinstance(self.p1, Sub) or isinstance(self.p1, Mul):
            if isinstance(self.p2, Add) or isinstance(self.p2, Sub) or isinstance(self.p2, Mul):
                return "( " + repr(self.p1) + " ) / ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) / " + repr(self.p2)
        if isinstance(self.p2, Add)  or isinstance(self.p2, Sub)  or isinstance(self.p2, Mul):
            return repr(self.p1) + " / ( " + repr(self.p2) + " )"
        return repr(self.p1) + " / " + repr(self.p2)
    def simplify(self):
        simp1 = self.p1.simplify()
        simp2 = self.p2.simplify()
        if isinstance(simp1, Int):
            if simp1.i == 0:
                return Int(0)
            if isinstance(simp2, Int):
                return Int(simp1.i / simp2.i)
            if isinstance(simp2, Div):
                if isinstance(simp2.p1, Int):
                    return Div(Int(simp1.i / simp2.p1.i), simp2.p2.simplify())
                if isinstance(simp2.p2, Int):
                    return Div(Int(simp1.i / simp2.p2.i), simp2.p1.simplify())
        if isinstance(simp2, Int):
            if simp2.i == 0:
                return Error.divby0()
                #return Int(0)
            if simp2.i == 1:
                return simp1
            if isinstance(simp1, Int):
                return Int(simp1.i / simp2.i)
            if isinstance(simp1, Div):
                if isinstance(simp1.p1, Int):
                    return Div(Int(simp2.i / simp1.p1.i), simp2.p2.simplify())
                if isinstance(simp1.p2, Int):
                    return Div(Int(simp2.i / simp1.p2.i), simp2.p1.simplify())
        return Div(simp1, simp2)
class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)

    def simplify(self):
        simp1 = self.p1.simplify()
        simp2 = self.p2.simplify()
        if isinstance(simp1, Int):
            if simp1.i == 0:
                return simp2
            if isinstance(simp2, Int):
                return Int(simp1.i + simp2.i)
        if isinstance(simp2, Int):
            if simp2.i == 0:
                return simp1
            if isinstance(simp1, Int):
                return Int(simp1.i + simp2.i)
        return Add(simp1, simp2)
class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return repr(self.p1) + " - " + repr(self.p2)
    def simplify(self):
        simp1 = self.p1.simplify()
        simp2 = self.p2.simplify()
        if isinstance(simp1, Int):
            if simp1.i == 0 and isinstance(simp2, Int)!=True:
                return Neg.simplify(simp2)
            if isinstance(simp2, Int):
                return Int(simp1.i - simp2.i)
        if isinstance(simp2, Int):
            if simp2.i == 0:
                return simp1
            if isinstance(simp1, Int):
                return Int(simp1.i - simp2.i)
        return Sub(simp1, simp2)

#poly = Sub( Add( Int(4), Int(3)), Add( X(), Div( Int(0), Add( Sub(X(), X()), Int(1)))))
# e1=Mul(Int(7),(Mul(X(),Mul(X(),X()))))
# e2=Mul(Int(2),Mul(Mul(X(),Mul(X(),X())),Mul(X(),X())))
# e3=Sub((Mul(Int(3),X())),Int(4))
# e4=Mul(Int(2),(Mul(X(),X())))                                                            
# poly2=Div(Add(e1,(Add(e2,e3))),e4)
#poly3=Sub(Int(2),Int(3))
#print(repr(poly))
#print(repr(poly.simplify()))
#poly4=Sub(Int(4),X(True,9))
poly5=Add(Add(Add(Sub(X(False,0),Pow(X(False,0),Int(8))),Int(5)),Int(20)),Int(50))
p5dic={}
p5list=str(poly5).split()
#print(p5list)
#print(repr(poly5.simplify()))
for x in range(len(p5list)):
    y=p5list[x]
    if x==0:
        try:
            y=int(y)
            li=[]
            li.append("+")
            p5dic[y]=li
            continue
        except:
            li=[]
            li.append("+")
            p5dic[y]=li
            #print(p5dic)
            continue
        
    
    #print("y"+y)
    if y=="+" :  
        #print(p5list[x+1])
        try:
            key=int(p5list[x+1])
            if key not in p5dic.keys():
                li=[]
                li.append("+")
                p5dic[key]=li
                #print(p5dic[key])
            else:
                li=[]
                li.append("+")
                p5dic[key]+=li
        except :
            key=p5list[x+1]
            if key not in p5dic.keys():
                li=[]
                li.append("+")
                p5dic[key]=li
            else:
                li=[]
                li.append("+")
                p5dic[key]+=li       
    elif y=="-":
        try:
            key=int(p5list[x+1])
            if key not in p5dic.keys():
                li=[]
                li.append("-")
                p5dic[key]=li
            else:
                li=[]
                li.append("-")
                p5dic[key]+=li
        except :
            key=p5list[x+1]
            if key not in p5dic.keys():
                li=[]
                li.append("-")
                p5dic[key]=li
            else:
                li=[]
                li.append("-")
                p5dic[key]+=li 
                #print(p5dic)
    elif y=="*":
        bef=p5list[x-1]
        af=p5list[x+1]
        if "X" not in bef:
            if "X" not in af: 
                p5dic[p5list[x-1]]=p5dic[p5list[x-1]].remove(p5list[x-2]) 
                key=int(bef)*int(af)
                if p5list[x-2]=="+":
                    if key not in p5dic.keys():
                        li=[]
                        li.append("+")
                        p5dic[key]=li
                    else:
                        p5dic[key]=p5dic[key].append("+")
                else:
                    if key not in p5dic.keys():
                        li=[]
                        li.append("-")
                        p5dic[key]=li
                    else:
                        p5dic[key]=p5dic[key].append("-")
            else:
                 p5dic[p5list[x-1]]=p5dic[p5list[x-1]].remove(p5list[x-2])
                 key=af
                 if p5list[x-2]=="+":
                     if key not in p5dic.keys():
                         li=[]
                         li.append("+"+bef)
                         p5dic[key]=li
                     else:
                         li=[]
                         li.append("+"+bef)
                         p5dic[key]+=li
                 else:
                     if key not in p5dic.keys():
                         li=[]
                         li.append("-"+bef)
                         p5dic[key]=li
                     else:
                         li=[]
                         li.append("-"+bef)
                         p5dic[key]+=li   
                
                
        else:
            if "X" not in af:
                key=bef
                if key not in p5dic.keys():
                    li=[]
                    li.append(p5list[x-2]+af)
                    p5dic[bef]=li
                else:
                    #print(p5dic)
                    #p5dic[bef]=p5dic[bef].remove(p5list[x-2])
                    #print(p5dic[bef])
                    p5dic[bef].pop()
                    #print(p5dic)
                    li=[]
                    li.append(p5list[x-2]+af)
                    #print(p5dic)
                    p5dic[bef]+=li
            else:
                key="X^2"
                if key not in p5dic.keys():
                    li=[]
                    li.append(p5list[x-2])
                    p5dic[key]=li
                else:
                    p5dic[key]=p5dic[key].append(p5list[x-2])
    elif y=="/":
        bef=p5list[x-1]
        af=p5list[x+1]
        if "X" not in bef:
            if "X" not in af: 
                p5dic[p5list[x-1]]=p5dic[p5list[x-1]].remove(p5list[x-2]) 
                key=int(bef)/int(af)
                if p5list[x-2]=="+":
                    if key not in p5dic.keys():
                        li=[]
                        li.append("+")
                        p5dic[key]=li
                    else:
                        p5dic[key]=p5dic[key].append("+")
                else:
                    if key not in p5dic.keys():
                        li=[]
                        li.append("-")
                        p5dic[key]=li
                    else:
                        p5dic[key]=p5dic[key].append("-")
            else:
                 p5dic[p5list[x-1]]=p5dic[p5list[x-1]].remove(p5list[x-2])
                 key="1/"+af
                 if p5list[x-2]=="+":
                     if key not in p5dic.keys():
                         li=[]
                         li.append("+"+bef)
                         p5dic[key]=li
                     else:
                         li=[]
                         li.append("+"+bef)
                         p5dic[key]+=li
                 else:
                     if key not in p5dic.keys():
                         li=[]
                         li.append("-"+bef)
                         p5dic[key]=li
                     else:
                         li=[]
                         li.append("-"+bef)
                         p5dic[key]+=li   
                
                
        else:
            if "X" not in af:
                key=bef
                if key not in p5dic.keys():
                    li=[]
                    dec=str(1/int(af))
                    li.append(((p5dic[p5list[x-1]])[-1])+ dec)
                    p5dic[bef]=li
                else:
                    #print(p5dic)
                    #p5dic[bef]=p5dic[bef].remove(p5list[x-2])
                    p5dic[bef]=[p5dic[bef].pop()]
                    #print(p5dic)
                    li=[]
                    dec=str(1/int(af))
                    li.append(((p5dic[p5list[x-1]])[-1])+ dec)
                    #print(p5dic)
                    p5dic[bef]+=li
            else:
                key=1
                if key not in p5dic.keys():
                    li=[]
                    li.append(p5list[x-2])
                    p5dic[key]=li
                else:
                    p5dic[key]=p5dic[key].append(p5list[x-2])
    elif y=="^":
        bef=p5list[x-1]
        af=p5list[x+1]
        if "X" not in bef:
            if "X" not in af: 
                p5dic[p5list[x-1]]=p5dic[p5list[x-1]].remove(p5list[x-2]) 
                key=math.pow(int(bef),int(af))
                if p5list[x-2]=="+":
                    if key not in p5dic.keys():
                        li=[]
                        li.append("+")
                        p5dic[key]=li
                    else:
                        p5dic[key]=p5dic[key].append("+")
                else:
                    if key not in p5dic.keys():
                        li=[]
                        li.append("-")
                        p5dic[key]=li
                    else:
                        p5dic[key]=p5dic[key].append("-")
            else:
                 p5dic[p5list[x-1]]=p5dic[p5list[x-1]].remove(p5list[x-2])
                 key=bef+"^"+af
                 if p5list[x-2]=="+":
                     if key not in p5dic.keys():
                         li=[]
                         li.append("+")
                         p5dic[key]=li
                     else:
                         li=[]
                         li.append("+")
                         p5dic[key]+=li
                 else:
                     if key not in p5dic.keys():
                         li=[]
                         li.append("-")
                         p5dic[key]=li
                     else:
                         li=[]
                         li.append("-")
                         p5dic[key]+=li   
                
                
        else:
            if "X" not in af:
                p5dic[bef]=list(p5dic[bef].pop())
                key=bef+"^"+af
                p5list[x-2]
                if key not in p5dic.keys():
                    li=[p5list[x-2]]
                    p5dic[key]=li
                else:
                    li=[p5list[x-2]]
                    p5dic[key]+=li
            else:
                key=bef+"^"+af
                if key not in p5dic.keys():
                    li=[]
                    li.append(p5list[x-2])
                    p5dic[key]=li
                else:
                    p5dic[key]=p5dic[key].append(p5list[x-2])
#print(p5dic)
for x in p5dic:
    li=p5dic[x]
    val=0
    for y in li:
        if y=="+":
            val+=1
        elif y=="-":
            val-=1
        elif "+" in y:
            val+=float(y.replace("+","")) 
        elif "-" in y:
            val-=float(y.replace("-","")) 
    p5dic[x]=val
#print(p5dic)
finaldic={}
int_val=0
for x in p5dic:
    try:
        int_val+=x*p5dic[x]
    except:
        finaldic[x]=p5dic[x]
finaldic["int"]=int_val
#print(finaldic)
poly5=Add(Add(Add(Sub(X(False,0),Pow(X(False,0),Int(8))),Int(5)),Int(60)),Int(10))
p5dic={}
p5list=str(poly5).split()
#print(p5list)
#print(repr(poly5.simplify()))
for x in range(len(p5list)):
    y=p5list[x]
    if x==0:
        try:
            y=int(y)
            li=[]
            li.append("+")
            p5dic[y]=li
            continue
        except:
            li=[]
            li.append("+")
            p5dic[y]=li
            #print(p5dic)
            continue
        
    
    #print("y"+y)
    if y=="+" :  
        #print(p5list[x+1])
        try:
            key=int(p5list[x+1])
            if key not in p5dic.keys():
                li=[]
                li.append("+")
                p5dic[key]=li
                #print(p5dic[key])
            else:
                li=[]
                li.append("+")
                p5dic[key]+=li
        except :
            key=p5list[x+1]
            if key not in p5dic.keys():
                li=[]
                li.append("+")
                p5dic[key]=li
            else:
                li=[]
                li.append("+")
                p5dic[key]+=li       
    elif y=="-":
        try:
            key=int(p5list[x+1])
            if key not in p5dic.keys():
                li=[]
                li.append("-")
                p5dic[key]=li
            else:
                li=[]
                li.append("-")
                p5dic[key]+=li
        except :
            key=p5list[x+1]
            if key not in p5dic.keys():
                li=[]
                li.append("-")
                p5dic[key]=li
            else:
                li=[]
                li.append("-")
                p5dic[key]+=li 
                #print(p5dic)
    elif y=="*":
        bef=p5list[x-1]
        af=p5list[x+1]
        if "X" not in bef:
            if "X" not in af: 
                p5dic[p5list[x-1]]=p5dic[p5list[x-1]].remove(p5list[x-2]) 
                key=int(bef)*int(af)
                if p5list[x-2]=="+":
                    if key not in p5dic.keys():
                        li=[]
                        li.append("+")
                        p5dic[key]=li
                    else:
                        p5dic[key]=p5dic[key].append("+")
                else:
                    if key not in p5dic.keys():
                        li=[]
                        li.append("-")
                        p5dic[key]=li
                    else:
                        p5dic[key]=p5dic[key].append("-")
            else:
                 p5dic[p5list[x-1]]=p5dic[p5list[x-1]].remove(p5list[x-2])
                 key=af
                 if p5list[x-2]=="+":
                     if key not in p5dic.keys():
                         li=[]
                         li.append("+"+bef)
                         p5dic[key]=li
                     else:
                         li=[]
                         li.append("+"+bef)
                         p5dic[key]+=li
                 else:
                     if key not in p5dic.keys():
                         li=[]
                         li.append("-"+bef)
                         p5dic[key]=li
                     else:
                         li=[]
                         li.append("-"+bef)
                         p5dic[key]+=li   
                
                
        else:
            if "X" not in af:
                key=bef
                if key not in p5dic.keys():
                    li=[]
                    li.append(p5list[x-2]+af)
                    p5dic[bef]=li
                else:
                    #print(p5dic)
                    #p5dic[bef]=p5dic[bef].remove(p5list[x-2])
                    #print(p5dic[bef])
                    p5dic[bef].pop()
                    #print(p5dic)
                    li=[]
                    li.append(p5list[x-2]+af)
                    #print(p5dic)
                    p5dic[bef]+=li
            else:
                key="X^2"
                if key not in p5dic.keys():
                    li=[]
                    li.append(p5list[x-2])
                    p5dic[key]=li
                else:
                    p5dic[key]=p5dic[key].append(p5list[x-2])
    elif y=="/":
        bef=p5list[x-1]
        af=p5list[x+1]
        if "X" not in bef:
            if "X" not in af: 
                p5dic[p5list[x-1]]=p5dic[p5list[x-1]].remove(p5list[x-2]) 
                key=int(bef)/int(af)
                if p5list[x-2]=="+":
                    if key not in p5dic.keys():
                        li=[]
                        li.append("+")
                        p5dic[key]=li
                    else:
                        p5dic[key]=p5dic[key].append("+")
                else:
                    if key not in p5dic.keys():
                        li=[]
                        li.append("-")
                        p5dic[key]=li
                    else:
                        p5dic[key]=p5dic[key].append("-")
            else:
                 p5dic[p5list[x-1]]=p5dic[p5list[x-1]].remove(p5list[x-2])
                 key="1/"+af
                 if p5list[x-2]=="+":
                     if key not in p5dic.keys():
                         li=[]
                         li.append("+"+bef)
                         p5dic[key]=li
                     else:
                         li=[]
                         li.append("+"+bef)
                         p5dic[key]+=li
                 else:
                     if key not in p5dic.keys():
                         li=[]
                         li.append("-"+bef)
                         p5dic[key]=li
                     else:
                         li=[]
                         li.append("-"+bef)
                         p5dic[key]+=li   
                
                
        else:
            if "X" not in af:
                key=bef
                if key not in p5dic.keys():
                    li=[]
                    dec=str(1/int(af))
                    li.append(((p5dic[p5list[x-1]])[-1])+ dec)
                    p5dic[bef]=li
                else:
                    #print(p5dic)
                    #p5dic[bef]=p5dic[bef].remove(p5list[x-2])
                    p5dic[bef]=[p5dic[bef].pop()]
                    #print(p5dic)
                    li=[]
                    dec=str(1/int(af))
                    li.append(((p5dic[p5list[x-1]])[-1])+ dec)
                    #print(p5dic)
                    p5dic[bef]+=li
            else:
                key=1
                if key not in p5dic.keys():
                    li=[]
                    li.append(p5list[x-2])
                    p5dic[key]=li
                else:
                    p5dic[key]=p5dic[key].append(p5list[x-2])
    elif y=="^":
        bef=p5list[x-1]
        af=p5list[x+1]
        if "X" not in bef:
            if "X" not in af: 
                p5dic[p5list[x-1]]=p5dic[p5list[x-1]].remove(p5list[x-2]) 
                key=math.pow(int(bef),int(af))
                if p5list[x-2]=="+":
                    if key not in p5dic.keys():
                        li=[]
                        li.append("+")
                        p5dic[key]=li
                    else:
                        p5dic[key]=p5dic[key].append("+")
                else:
                    if key not in p5dic.keys():
                        li=[]
                        li.append("-")
                        p5dic[key]=li
                    else:
                        p5dic[key]=p5dic[key].append("-")
            else:
                 p5dic[p5list[x-1]]=p5dic[p5list[x-1]].remove(p5list[x-2])
                 key=bef+"^"+af
                 if p5list[x-2]=="+":
                     if key not in p5dic.keys():
                         li=[]
                         li.append("+")
                         p5dic[key]=li
                     else:
                         li=[]
                         li.append("+")
                         p5dic[key]+=li
                 else:
                     if key not in p5dic.keys():
                         li=[]
                         li.append("-")
                         p5dic[key]=li
                     else:
                         li=[]
                         li.append("-")
                         p5dic[key]+=li   
                
                
        else:
            if "X" not in af:
                p5dic[bef]=list(p5dic[bef].pop())
                key=bef+"^"+af
                p5list[x-2]
                if key not in p5dic.keys():
                    li=[p5list[x-2]]
                    p5dic[key]=li
                else:
                    li=[p5list[x-2]]
                    p5dic[key]+=li
            else:
                key=bef+"^"+af
                if key not in p5dic.keys():
                    li=[]
                    li.append(p5list[x-2])
                    p5dic[key]=li
                else:
                    p5dic[key]=p5dic[key].append(p5list[x-2])
#print(p5dic)
for x in p5dic:
    li=p5dic[x]
    val=0
    for y in li:
        if y=="+":
            val+=1
        elif y=="-":
            val-=1
        elif "+" in y:
            val+=float(y.replace("+","")) 
        elif "-" in y:
            val-=float(y.replace("-","")) 
    p5dic[x]=val
#print(p5dic)
finaldic2={}
int_val=0
for x in p5dic:
    try:
        int_val+=x*p5dic[x]
    except:
        finaldic2[x]=p5dic[x]
finaldic2["int"]=int_val
#print(finaldic2)
poss=True
for x in finaldic:
    if x not in finaldic2.keys():
        poss=False
    elif finaldic[x]!=finaldic2[x]:
        poss=False
print(poss)