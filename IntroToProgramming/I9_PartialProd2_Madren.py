# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 15:48:21 2019

@author: benma
"""
#%%
import numpy as np
a_n = lambda n: 1 + (1/(n**3))

N = 20
x = np.zeros([N])
term = 1

for nn in range(1, N):
    term = term * a_n(nn)
    x[nn] = term
    
print("The first 15 terms are ", x[:15], " and the last 15 terms are ", x[-15:])