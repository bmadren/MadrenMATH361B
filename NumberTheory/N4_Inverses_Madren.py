# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 12:57:48 2019

@author: benma
"""
#%%
m = 12
Inv = False
i = 0
for a in range(0, m-1, 1):
    for b in range(0, m-1, 1):
        if((a * b) % m == 1):
            Inv = True
            i = i + 2
if(Inv == True):
    print("The", i, "elements of Z", m, "that have multiplicative inverses are", a, "and",  b)