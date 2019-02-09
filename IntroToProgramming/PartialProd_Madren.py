# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 22:08:34 2019

@author: benma
"""

#%%
import numpy as np
N = 50
x = np.zeros([N])
term = 1
for nn in range(2, N):
    term *= (nn**3 - 1)/(nn**3 + 1)
    x[nn] = term
    
print("The first 15 terms are ", x[:15], " and the last 15 terms are ", x[-15:])

#%%
import numpy as np
from math import exp
N = 50
x = np.zeros([N])
term = 1
for nn in range(1, N):
    term *= (exp(nn/100))/(nn**10)
    x[nn] = term
    
print("The first 15 terms are ", x[:15], " and the last 15 terms are ", x[-15:])

#%%
import numpy as np
from math import exp
N = 50
x = np.zeros([N])
term = 1
for nn in range(1, N):
    term *= (exp(nn/10))/(nn**100)
    x[nn] = term
    
print("The first 15 terms are ", x[:15], " and the last 15 terms are ", x[-15:])