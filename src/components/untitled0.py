#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 17:19:28 2020

@author: oscargalindo
"""


import numpy as np

def swap_first_and_last(L):
    temp = L[0]
    L[0] = L[-1]
    L[-1] = temp
    return L
 
def diagonal(A):
    #Your code goes here
    D = np.zeros((len(A),len(A)))
    for elementNum in range(len(A)):
        D[elementNum][elementNum] = A[elementNum]
    return D
    
def greater_than_list(L,x):
    for e in L:
        print(x,e)
        print(e <= x)
        if(e <= x):
            L.remove(e)
    return L

# L = [1, 5, 8, 7, 9, 3, 0, 4, 2, 6]  
# swap_first_and_last(L)
# print(L)   # [6, 5, 8, 7, 9, 3, 0, 4, 2, 1]


# A = np.array([2,4,6,8])
# D = diagonal(A)
# print(D)

# ''' 
# Output: 
# [[2. 0. 0. 0.]
#  [0. 4. 0. 0.]
#  [0. 0. 6. 0.]
#  [0. 0. 0. 8.]]
# '''

L = [1, 9, 3, 0, 4, 2, 5, 8, 7, 6]
L3 = greater_than_list(L,3)
print(L3) # [9, 4, 5, 8, 7, 6]

# L7 = greater_than_list(L,7)
# print(L7) # [9, 8]
      
# L13 = greater_than_list(L,13)
# print(L13) # []






