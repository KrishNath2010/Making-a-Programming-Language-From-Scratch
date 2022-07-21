# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 14:45:18 2022

@author: Krish Nath
"""


class Neg:
    def __init__(self,p):
        self.p = p
        
    def __repr__(self):
        return "- ( " + repr(self.p) + " )"
    
    def simplify(self):
        simp = self.p.simplify()
        
        return Mul(Int(-1), simp).simplify()
    
    
class Pow:
    def __init__(self, p1, p2):
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
                return Int(simp1.i ** simp2.i)
            
            if isinstance(simp2, Pow):
                if isinstance(simp2.p1, Int):
                    return Pow(Int(simp1.i ** simp2.p1.i), simp2.p2.simplify())
                
                if isinstance(simp2.p2, Int):
                    return Pow(Int((simp1.i ** simp2.p2.i)), simp2.p1.simplify())
        if isinstance(simp2, Int):
            if simp2.i == 0:
                return Int(1)
            
            if simp2.i == 1:
                return simp1
            
            if isinstance(simp1, Int):
                return Int(simp1.i ** simp2.i)
            if isinstance(simp1, Pow):
                if isinstance(simp1.p1, Int):
                    return Pow(Int(simp1.p1.i ** simp2.i), simp2.p2.simplify())
                
                if isinstance(simp1.p2, Int):
                    return Pow(Int(simp1.p1.i**simp2.i), simp2.p1.simplify())
        return Pow(simp1, simp2)
    def evaluate(self, i):
        simp1 = self.p1.simplify()
        simp2 = self.p2.simplify()
        return Pow(simp1.evaluate(i), simp2.evaluate(i)).simplify()
    
    def max_degree(self):
        simp1 = self.p1.simplify()
        simp2 = self.p2.simplify()
        if isinstance(simp2, Int):
            return simp1.max_degree() * simp2.i
        return max(simp1.max_degree(),simp2.max_degree()) 
class Error:
    def __init__(self, message):
        self.message = message
    
    def __repr__(self):
        return self.message
    
    def divby0(self):
        return 1/0 
    
    
class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

    def simplify(self):
        return self
    def evaluate(self, i):
        return Int(i)
    
    def max_degree(self):
        return 1
class Int:
    def __init__(self, i):
        self.i = int(i)

    def __repr__(self):
        return str(self.i)

    def simplify(self):
        return self
    def evaluate(self, i):
       return self
    def max_degree(self):
       return 0

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
        if isinstance(simp1, Pow):
            if isinstance(simp2, Pow):
                e1=simp1.p1
                e2=simp1.p2
                o1=simp2.p1
                o2=simp2.p2              
                if repr(e1)==repr(o1):
                    if isinstance(e2, Int):
                        if isinstance(o2, Int):
                            return Pow(e1,Int(e2.i+o2.i))
                    if isinstance(e2, X):
                        if isinstance(o2, X):
                            return Pow(e1,Mul(Int(2),X()))
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
            if isinstance(simp2, Add):
                e1=simp2.p1
                e2=simp2.p2
                if isinstance(e1, Int):
                    return Add(Int(e1.i*simp1.i),Mul(simp1,e2))
                if isinstance(e2, Int):
                    return Add(Int(e2.i*simp1.i),Mul(simp1,e1))
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
            if isinstance(simp1, Add):
                e1=simp1.p1
                e2=simp1.p2
                if isinstance(e1, Int):
                    return Add(Int(e1.i*simp2.i),Mul(simp2,e2))
                if isinstance(e2, Int):
                    return Add(Int(e2.i*simp2.i),Mul(simp2,e1))
        if isinstance(simp1, X):
           if isinstance(simp2, X): 
               return Pow(X(),Int(2))
           if isinstance(simp2, Mul):
               e1=simp2.p1
               e2=simp2.p2
               if isinstance(e1, X):
                   return Mul(e2, Pow(X(),Int(2))).simplify()
               if isinstance(e2, X):
                   return Mul(e1, Pow(X(),Int(2))).simplify()
        if isinstance(simp2, X):
           if isinstance(simp1, Mul):
               e1=simp1.p1
               e2=simp1.p2
               if isinstance(e1, X):
                   return Mul(e2, Pow(X(),Int(2))).simplify()
               if isinstance(e2, X):
                   return Mul(e1, Pow(X(),Int(2))).simplify()
        return Mul(simp1, simp2)
    def evaluate(self, i):
        simp1 = self.p1.simplify()
        simp2 = self.p2.simplify()
        return Mul(simp1.evaluate(i), simp2.evaluate(i)).simplify()
    def max_degree(self):
        simp1 = self.p1.simplify()
        simp2 = self.p2.simplify()
        return simp1.max_degree() + simp2.max_degree()

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
                if simp2.i == 0:
                    return Error("Error:Dividing by 0")
                
                return Int(simp1.i / simp2.i)
            
            if isinstance(simp2, Div):
                if isinstance(simp2.p1, Int):
                    return Div(Int(simp1.i / simp2.p1.i), simp2.p2.simplify())
                
                if isinstance(simp2.p2, Int):
                    return Div(Int(simp1.i / simp2.p2.i), simp2.p1.simplify())
        if isinstance(simp2, Int):
            if simp2.i == 0:
                return Error("Error:Dividing by 0")
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
    def evaluate(self, i):
        simp1 = self.p1.simplify()
        simp2 = self.p2.simplify()
        return Div(simp1.evaluate(i), simp2.evaluate(i)).simplify()
    def max_degree(self):
        simp1 = self.p1.simplify()
        simp2 = self.p2.simplify()
        return abs(simp1.max_degree() - simp2.max_degree())

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)

    def simplify(self):
        #print(self.p1)
        #print(self.p2)
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
        if isinstance(simp1, X):
            if isinstance(simp2, X):
                return Mul(Int(2),X()).simplify()
        if isinstance(simp1, Add):
            e1=simp1.p1
            e2=simp1.p2
            if isinstance(simp2, Mul):
                simp1=e1
                e1a=simp2.p1
                e2a=simp2.p2
                if isinstance(simp1, Mul):
                    o1=simp1.p1
                    o2=simp1.p2
                    #print(e1a,e2a,o1,o2)
                    if isinstance(e1a, Pow):
                        if isinstance(o1, Pow):
                            if isinstance(o2, Int):
                                if isinstance(e2a, Int):
                                    if e1a==o1:
                                        return Add(Mul(Int(o2.i+e2a.i),e1a).simplify(),e2).simplify()
                        if isinstance(o2, Pow):
                            if isinstance(o1, Int):
                                if isinstance(e2, Int):
                                    if e1a==o2:
                                        return Add(Mul(Int(o1.i+e2a.i),e1a).simplify(),e2).simplify()
                    if isinstance(e2a, Pow):
                        if isinstance(o1, Pow):
                            if isinstance(o2, Int):
                                if isinstance(e2a, Int):
                                    if e2a==o1:
                                        return Add(Mul(Int(o2.i+e1a.i),e2a).simplify(),e2).simplify()
                        if isinstance(o2, Pow):
                            if isinstance(o1, Int):
                                if isinstance(e1a, Int):
                                    #print("a")
                                    if repr(e2a)==repr(o2):
                                        #print("b")
                                        #print(e2)
                                        #print(Mul(Int(o1.i+e1a.i),e2).simplify())
                                        return Add(Mul(Int(o1.i+e1a.i),e2a).simplify(),e2).simplify()
                if isinstance(e1, Pow):
                    o1=e1.p1
                    o2=e1.p2
                    if isinstance(e2a, Pow):
                        t1=e2a.p1
                        t2=e2a.p2
                        if repr(o1)==repr(t1):
                            if repr(o2)==repr(t2):
                                return Add(Mul(Int(1+e1a.i),e1).simplify(), e2).simplify()
            if isinstance(simp2, Mul):
                simp1=e2
                e1a=simp2.p1
                e2a=simp2.p2
                if isinstance(simp1, Mul):
                    o1=simp1.p1
                    o2=simp1.p2
                    if isinstance(e1a, Pow):
                        if isinstance(o1, Pow):
                            if isinstance(o2, Int):
                                if isinstance(e2a, Int):
                                    if e1a==o1:
                                        return Add(Mul(Int(o2.i+e2a.i),e1a).simplify(),e1).simplify()
                        if isinstance(o2, Pow):
                            if isinstance(o1, Int):
                                if isinstance(e2a, Int):
                                    if e1==o2:
                                        return Add(Mul(Int(o1.i+e2a.i),e1a).simplify(),e1).simplify()
                    if isinstance(e2a, Pow):
                        if isinstance(o1, Pow):
                            if isinstance(o2, Int):
                                if isinstance(e2a, Int):
                                    if e2a==o1:
                                        return Add(Mul(Int(o2.i+e1a.i),e2a).simplify(),e1).simplify()
                        if isinstance(o2, Pow):
                            if isinstance(o1, Int):
                                if isinstance(e2a, Int):
                                    if e2a==o2:
                                        return Add(Mul(Int(o1.i+e1a.i),e2a).simplify(),e1).simplify()
            if isinstance(simp2, Int):
                if isinstance(e1, Int):
                    return Add(e2, Int(simp2.i+e1.i)).simplify()
                if isinstance(e2, Int):
                    return Add(e1, Int(simp2.i+e2.i)).simplify()
            if isinstance(simp2, X):
                if isinstance(e1, X):
                    return Add(e2, Mul(Int(2),X()).simplify()).simplify()
                if isinstance(e2, X):
                    return Add(e1, Mul(Int(2),X()).simplify()).simplify()
            if isinstance(simp2,Add):
                o1=simp2.p1
                o2=simp2.p2
                if isinstance(e1, Int):
                    if isinstance(o1, Int):
                        return Add(Int(e1.i+o1.i), Add(o2,e2).simplify()).simplify()
                    if isinstance(o2, Int):
                        return Add(Int(e1.i+o2.i), Add(o1,e2).simplify()).simplify()
                if isinstance(e2, Int):
                    if isinstance(o1, Int):
                        return Add(Int(e2.i+o1.i), Add(o2,e1).simplify()).simplify()
                    if isinstance(o2, Int):
                        #print(o1)
                        #print(e1)
                        r=Add(o1,e1).simplify()
                        #print(1)
                        return Add(Int(e2.i+o2.i), r).simplify()
                if isinstance(e1, X):
                    if isinstance(o1, X):
                        return Add(Mul(Int(2),X()).simplify(), Add(o2,e2).simplify()).simplify()
                    if isinstance(o2, X):
                        return Add(Mul(Int(2),X()).simplify(), Add(o1,e2).simplify()).simplify()
                if isinstance(e2, X):
                    if isinstance(o1, X):
                        return Add(Mul(Int(2),X()).simplify(), Add(o2,e1).simplify()).simplify()
                    if isinstance(o2, X):
                        return Add(Mul(Int(2),X()).simplify(), Add(o1,e1).simplify()).simplify()
        if isinstance(simp2, Add):
            e1=simp2.p1
            e2=simp2.p2
            if isinstance(simp1, Mul):
                simp2=e1
                e1a=simp2.p1
                e2a=simp2.p2
                if isinstance(simp2, Mul):
                    o1=simp1.p1
                    o2=simp1.p2
                    if isinstance(e1a, Pow):
                        if isinstance(o1, Pow):
                            if isinstance(o2, Int):
                                if isinstance(e2a, Int):
                                    if e1a==o1:
                                        return Add(Mul(Int(o2.i+e2a.i),e1a).simplify(),e2).simplify()
                        if isinstance(o2, Pow):
                            if isinstance(o1, Int):
                                if isinstance(e2a, Int):
                                    if e1a==o2:
                                        return Add(Mul(Int(o1.i+e2a.i),e1a).simplify(),e2).simplify()
                    if isinstance(e2a, Pow):
                        if isinstance(o1, Pow):
                            if isinstance(o2, Int):
                                if isinstance(e2a, Int):
                                    if e2a==o1:
                                        return Add(Mul(Int(o2.i+e1a.i),e2a).simplify(),e2).simplify()
                        if isinstance(o2, Pow):
                            if isinstance(o1, Int):
                                if isinstance(e2a, Int):
                                    if e2a==o2:
                                        return Add(Mul(Int(o1.i+e1a.i),e2a).simplify(),e2).simplify()
            if isinstance(simp1, Mul):
                simp2=e2
                e1a=simp2.p1
                e2a=simp2.p2
                if isinstance(simp2, Mul):
                    o1=simp1.p1
                    o2=simp1.p2
                    if isinstance(e1a, Pow):
                        if isinstance(o1, Pow):
                            if isinstance(o2, Int):
                                if isinstance(e2a, Int):
                                    if e1a==o1:
                                        return Add(Mul(Int(o2.i+e2a.i),e1a).simplify(),e1).simplify()
                        if isinstance(o2, Pow):
                            if isinstance(o1, Int):
                                if isinstance(e2a, Int):
                                    if e1a==o2:
                                        return Add(Mul(Int(o1.i+e2a.i),e1a).simplify(),e1).simplify()
                    if isinstance(e2a, Pow):
                        if isinstance(o1, Pow):
                            if isinstance(o2, Int):
                                if isinstance(e1a, Int):
                                    if e2a==o1:
                                        return Add(Mul(Int(o2.i+e1a.i),e2a).simplify(),e1).simplify()
                        if isinstance(o2, Pow):
                            if isinstance(o1, Int):
                                if isinstance(e1a, Int):
                                    if e2a==o2:
                                        return Add(Mul(Int(o1.i+e1a.i),e2a).simplify(),e1).simplify()
            if isinstance(simp1, Int):
                if isinstance(e1, Int):
                    return Add(e2, Int(simp1+e1)).simplify()
                if isinstance(e2, Int):
                    return Add(e1, Int(simp1+e2)).simplify()
            if isinstance(simp1, X):
                if isinstance(e1, X):
                    return Add(e2, Mul(Int(2),X()).simplify()).simplify()
                if isinstance(e2, X):
                    return Add(e1, Mul(Int(2),X()).simplify()).simplify()
        if isinstance(simp2, Mul):
            e1=simp2.p1
            e2=simp2.p2
            if isinstance(simp1, Mul) :
                o1=simp1.p1
                o2=simp1.p2
                if isinstance(e1, Pow):
                    if isinstance(o1, Pow):
                        if isinstance(o2, Int):
                            if isinstance(e2, Int):
                                if e1==o1:
                                    return Mul(Int(o2.i+e2.i),e1).simplify()
                    if isinstance(o2, Pow):
                        if isinstance(o1, Int):
                            if isinstance(e2, Int):
                                if e1==o2:
                                    return Mul(Int(o1.i+e2.i),e1).simplify()
                if isinstance(e2, Pow):
                    if isinstance(o1, Pow):
                        if isinstance(o2, Int):
                            if isinstance(e2, Int):
                                if e2==o1:
                                    return Mul(Int(o2.i+e1.i),e2).simplify()
                    if isinstance(o2, Pow):
                        if isinstance(o1, Int):
                            if isinstance(e2, Int):
                                if e2==o2:
                                    return Mul(Int(o1.i+e1.i),e2).simplify()
        return Add(simp1, simp2)
    def evaluate(self, i):
        simp1 = self.p1.simplify()
        simp2 = self.p2.simplify()
        return Add(simp1.evaluate(i), simp2.evaluate(i)).simplify()
    def max_degree(self):
        simp1 = self.p1.simplify()
        simp2 = self.p2.simplify()
        return max(simp1.max_degree(), simp2.max_degree())

class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return repr(self.p1) + " - " + repr(self.p2)
    def simplify(self):
        simp1 = self.p1.simplify()
        simp2 = self.p2.simplify()
        return Add(simp1, Neg(simp2).simplify()).simplify()
    def evaluate(self, i):
        simp1 = self.p1.simplify()
        simp2 = self.p2.simplify()
        return Sub(simp1.evaluate(i), simp2.evaluate(i)).simplify()
    def max_degree(self):
        simp1 = self.p1.simplify()
        simp2 = self.p2.simplify()
        return max(simp1.max_degree(), simp2.max_degree())
        
def equals(p1, p2):
   d1 = p1.max_degree()
   d2 = p2.max_degree()

   if d1 != d2:
       return False
   if d1 == 0:
       simp1 = p1.simplify()
       simp2 = p2.simplify()
       if isinstance(simp1, Int) and isinstance(simp2, Int):
           return simp1.i == simp2.i
       # We have a problem...
       raise ValueError
   #print(d1)
   new_p1 = Sub(p1, Pow(X(), Int(d1))).simplify()
   new_p2 = Sub(p2, Pow(X(), Int(d2))).simplify()
   #print(new_p1)
   #print(new_p2)
   return equals(new_p1, new_p2)       
#poly = Sub( Add( Int(4), Int(3)), Add( X(), Div( Int(0), Add( Sub(X(), X()), Int(1)))))
# e1=Mul(Int(7),(Mul(X(),Mul(X(),X()))))
# e2=Mul(Int(2),Mul(Mul(X(),Mul(X(),X())),Mul(X(),X())))
# e3=Sub((Mul(Int(3),X())),Int(4))
# e4=Mul(Int(2),(Mul(X(),X())))                                                            
# poly2=Div(Add(e1,(Add(e2,e3))),e4)
#poly3=Sub(Int(2),Int(3))
#print(repr(poly))
#print(repr(poly.simplify()))
#poly4=Sub(Int(0),X())
# poly5 = Add(Mul( X(), Mul( X(), Int(9))),Int(4)).simplify()
# poly6 = Add(Mul( X(), Mul( X(), Int(9))),Int(4)).simplify()
poly5 = Sub(Add(Mul( X(), Mul( X(), Int(9))),Int(4)),Int(-1))
poly6 = Add(Mul( X(), Mul( X(), Int(9))),Int(5))
#print(repr(poly6.simplify()))
print(equals(poly5.simplify(), poly6.simplify()))
