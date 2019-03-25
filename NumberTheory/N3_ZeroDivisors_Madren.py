# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 12:44:21 2019

@author: benma
"""
#%%
m = 12
Div = False
i = 0
for x in range(0, m-1, 1):
    for y in range(0, m-1, 1):
        if((x * y) % m == 0):
            Div = True
            i = i + 2
if(Div == True):
    print("The", i, "zero divisors of Z", m, "are ", x," and ", y)