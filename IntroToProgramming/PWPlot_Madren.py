# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 18:45:45 2019

@author: benma
"""

#%%
import matplotlib.pyplot as plt
import numpy as np

N = 10
def PWFunc(x):
        if (x < -2):
            y = -3*(x+2)**2 + 1
        elif (-2 <= x and x < -1):
            y = 1
        elif (-1 <= x and x <= 1):
            y = (x-1)**3 + 3
        elif (1 < x and x < 2):
            y = np.sin(np.pi*x) + 3
        elif (x >= 2):
            y = 3*(np.sqrt(x-2)) + 4
        return y

x_array = np.linspace(-3, 3, N)
y_array = np.zeros(N)
for i in range(len(x_array)):
    y_array[i] = PWFunc(x_array[i])
plt.plot(x_array, y_array)    
plt.xlabel("x-values")
plt.ylabel("y-values")
plt.title("Piecewise Function")
plt.show()