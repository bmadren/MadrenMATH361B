# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 18:45:45 2019

@author: benma
"""

#%%
import matplotlib.pyplot as plt
import numpy as np

N = 10
def function1(x):
    if x < -2:
        y = -3*(x+2)**2 + 1
    elif -2 <= x < -1:
        y = 1
    elif -1 <= x <= 1:
        y = (x-1)**3 + 3
    elif 1 < x < 2:
        y = np.sin(np.pi*x) + 3
    else:
        y = 3*(np.sqrt(x-2)) + 4
    return y

x = np.linspace(-3, 3, N)
y = np.zeros(N)
for i in range(len(x)):
    y[i] = function1(x[i])
plt.plot(x, y)    
plt.xlabel("x-values")
plt.ylabel("y-values")
plt.title("Piecewise Function")
plt.show()