#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 17:42:08 2020

@author: oscargalindo
"""

import numpy as np

def replace(S,a,b):
#    return S.replace(a,b,-1)
    resultString = ''
    for char in S:
        if char == a:
            resultString += b
        else:
            resultString += char
    return resultString


def divisors(n):
    divisors = []
    for x in range(1, n+1):
        if (n%x) == 0.0:
            divisors.append(x)
    return divisors
        

def set_largest_to_zero(A):
    maximum = float('-inf')
    coordinates_x, coordinates_y = 0,0
    prov_x, prov_y = 0,0
    for l in A:
        prov_y = 0
        for elemen in l:
            if elemen > maximum:
                coordinates_x = prov_x
                coordinates_y = prov_y
            prov_y += 1
        prov_x += 1
    A[coordinates_x][coordinates_y] = 0
    return A
        
      
#S = replace('data structures', 'a', 's')
#print(S)    # dsts structures
    
d = divisors(20)
print(d)   #  [1, 2, 4, 5, 10, 20]
d = divisors(23)
print(d)   #  [1, 23]

L = [1, 5, 8, 7, 9, 3, 0, 4, 2, 6]  
A = np.array(L).reshape(2,5) 
print(A)   
set_largest_to_zero(A)
print(A)
''' 
Output: 
[[1 5 8 7 0]
 [3 0 4 2 6]]
'''



