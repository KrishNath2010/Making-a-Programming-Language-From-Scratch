# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 18:26:26 2022

@author: Krish Nath
"""

poss=0
a=0
for i in range(201):
    for j in range(101): 
        if i+2*j==200:
            poss+=1
            #print(poss)
            continue
        if i+2*j>200:
            continue
        for k in range(41):
           if i+2*j+5*k==200:
               poss+=1
               #print(poss)
               continue
           if i+2*j+5*k>200:
               continue
           for l in range(21):
               if i+2*j+5*k+10*l==200:
                   poss+=1
                   #print(poss)
                   continue
               if i+2*j+5*k+10*l>200:
                   continue
               for m in range(11):
                   if i+2*j+5*k+10*l+20*m==200:
                       poss+=1
                       #print(poss)
                       continue
                   if i+2*j+5*k+10*l+20*m>200:
                       continue
                   for n in range(5):
                       if i+2*j+5*k+10*l+20*m+50*n==200:
                           poss+=1
                           #print(poss)
                           continue
                       if i+2*j+5*k+10*l+20*m+50*n>200:
                           continue
                       for o in range(3):
                           for p in range(2):
                               if i+2*j+5*k+10*l+20*m+n*50+o*100+p*200==200:
                                   poss+=1
                                   #print(poss)
                               a+=1
                               #if (a%1000000==0):
                                   #print("a")
print(poss)