# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 11:37:39 2022

@author: Krish Nath
"""

# Not used anymore
def fac(a) :
    if (a == 1 or a==0):
            return 1
    return a * fac(a - 1)

# Makes a list of factorials from 0-9
def make_fac_list(num, l):
    if num == 10:
        return l
    l.append(num * l[num - 1])
    return make_fac_list(num + 1, l)
fac_list = make_fac_list(1, [1])
#print(fac_list)

# Creates sum of factorials of all numbers in a number list
def sum_of_factorial_of_digits(index, number_list):
    global fac_list
    fact_sum = fac_list[number_list[index]]
    #print(fact_sum, index)
    if index < len(number_list) - 1:
        fact_sum += sum_of_factorial_of_digits(index + 1, number_list)
        #print(fact_sum, index)
    return fact_sum

# Makes a list of digits from a number
def make_number_list(num, num_list):
    #print(num_list)
    #print(num)
    if num <= 0:
        #print(num_list)
        return num_list
    digit = num % 10
    num_list.append(digit)
    return make_number_list(num // 10, num_list)

sums = -3
def main():
    global sums
    #if i>3000:
        #return sums
    for i in range(10000000):
        # Ignore numbers that we are sure will not have the property we are looking for
        if (i == 0) or (i < 100 and i > 50) or (i < 1000 and i > 700) or (i < 10000 and i > 8000) or (i < 100000 and i > 90000):
            #return main(i+1)
            continue

        num = i
        number_list = make_number_list(num, [])
        #print(number_list)
        
        # Print to track progress
        if (i % 1000000 == 0):
            print("Tracking:", i)

        num = sum_of_factorial_of_digits(0, number_list)
        if i == num:
            sums += i
            print("Found:", i)
    return sums
    #if i < 3000:
        #return main(i + 1)
#n_list = make_number_list(1223, [])
#print(n_list)
#num=sum_of_factorial_of_digits(0, [1, 2, 3, 4, 5], 0)
#print(num)
print("Answer:", main())
