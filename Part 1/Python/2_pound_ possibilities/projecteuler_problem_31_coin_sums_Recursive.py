# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 09:39:12 2022

@author: Krish Nath
"""
poss=0
a=0
def main(i):
    if i>200:
        return 0
    global poss, a
    #print(i)
    #print(poss)
    def s(j,i):
        if j > 100:
            return 0
        global poss, a
        if i+(2*j)==200:
            poss+=1
            return 0
            #print(poss)
        if i+(2*j)>200:
            return 0
        def t(k,j,i):
           if k > 40:
               return 0
           global poss, a
           if i+(2*j)+(5*k)==200:
               poss+=1
               return 0
               #print(poss)
           if i+(2*j)+(5*k)>200:
               return 0
           def f(l,k,j,i):
               if l>20:
                   return 0
               global poss, a
               if i+(2*j)+(5*k)+(10*l)==200:
                   poss+=1
                   return 0
                   #print(poss)
               if i+(2*j)+(5*k)+(10*l)>200:
                   return 0
               def fi(m,l,k,j,i):
                   if m>10:
                       return 0
                   global poss, a
                   if i+(2*j)+(5*k)+(10*l)+(20*m)==200:
                       poss+=1
                       return 0
                       #print(poss)
                   if i+(2*j)+(5*k)+(10*l)+(20*m)>200:
                       return 0
                   def si(n,m,l,k,j,i):
                       if n>5:
                           return 0
                       global poss, a
                       if i+(2*j)+(5*k)+(10*l)+(20*m)+(50*n)==200:
                           poss+=1
                           return 0
                           #print(poss)
                       if i+(2*j)+(5*k)+(10*l)+(20*m)+(50*n)>200:
                           return 0
                       def se(o,n,m,l,k,j,i):
                           if o>2:
                               return 0
                           global poss, a
                           if i+(2*j)+(5*k)+(10*l)+(20*m)+(n*50)+(o*100)==200:
                               poss+=1
                               return 0
                           if i+(2*j)+(5*k)+(10*l)+(20*m)+(50*n)>200:
                               return 0 
                           def e(p,o,n,m,l,k,j,i):
                               if p>1:
                                   return 0
                               global poss
                               if i+(2*j)+(5*k)+(10*l)+(20*m)+(n*50)+(o*100)+(p*200)==200:
                                   poss+=1
                                   return 0
                                   #print(poss)
                               #a+=1
                               #if (a%100000==0):
                                   #print("a")
                               return e(p+1,o,n,m,l,k,j,i)
                           e(0,o,n,m,l,k,j,i)
                           return se(o+1,n,m,l,k,j,i)
                       se(0,n,m,l,k,j,i) 
                       return si(n+1,m,l,k,j,i)
                   si(0,m,l,k,j,i) 
                   return fi(m+1,l,k,j,i)
               fi(0,l,k,j,i) 
               return f(l+1,k,j,i)
           f(0,k,j,i) 
           return t(k+1,j,i)
        t(0,j,i)
        return s(j+1,i)
    s(0,i)
    return main(i+1)
main(0)
print("Answer:", end = " ")
print(poss)