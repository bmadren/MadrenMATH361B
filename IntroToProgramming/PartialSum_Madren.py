# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 19:45:29 2019

@author: benma
"""
#%%
import numpy as np
from math import log
N = 50
x = np.zeros([N])
term = 0
for nn in range(1, N):
    term += (log(nn**4+nn+1)**2)/((nn)**(1/2)+3)
    x[nn] = term
    
print("The first 15 terms are ", x[:15], " and the last 15 terms are ", x[-15:])

#%%
import numpy as np
from math import exp
N = 50
x = np.zeros([N])
term = 0
for nn in range(1, N):
    term += ((exp(nn/100))/(nn**10))
    x[nn] = term
    
print("The first 15 terms are ", x[:15], " and the last 15 terms are ", x[-15:])

#%%
import numpy as np
from math import exp
N = 50
x = np.zeros([N])
term = 0
for nn in range(1, N):
    term += ((nn+1)**2)/(exp(nn))
    x[nn] = term
    
print("The first 15 terms are ", x[:15], " and the last 15 terms are ", x[-15:])