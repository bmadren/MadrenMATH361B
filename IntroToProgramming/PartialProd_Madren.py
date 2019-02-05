# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 22:08:34 2019

@author: benma
"""

#%%
N = 30
product=1
products = []

for nn in range(2,N+1):
    product *= (nn**3 - 1)/(nn**3 + 1)
    products.append(product)
    
print("The terms are ", products)

#%%
from math import exp
N = 30
product=1
products = []

for nn in range(2,N+1):
    product *= (exp(nn/100))/(nn**10)
    products.append(product)
    
print("The terms are ", products)