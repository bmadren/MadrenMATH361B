# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 12:05:44 2019

@author: benma
"""
#%%
import numpy as np
import math as m
from math import e
N = 100
n = 1
TOL = 1e-4
z0 = 1
l = [z0 + 1]
f = lambda n : m.tan(n) - n - 2#(1/100)*(n**4 + (e - 2 - m.sqrt(2))*(n**3) + (2*m.sqrt(2) - m.sqrt(2)*e - 3 - 2*e)*(n**2) + (2*m.sqrt(2)*e + 3*m.sqrt(2) - 3*e)*n + 3*m.sqrt(2)*e)
fp = lambda n : (1/m.cos(n))**2 - 1#(1/100)*(4*n**3 + 3*(e - 2 - m.sqrt(2))*(n**2) + 2*(2*m.sqrt(2) - m.sqrt(2)*e - 3 - 2*e)*n + (2*m.sqrt(2)*e + 3*m.sqrt(2) - 3*e))
while (np.abs(l[-1] - z0) > TOL and n < N):
    l.append(z0)
    z0 = z0 - (f(z0) / fp(z0))
    n += 1
    if (np.abs(l[-1] - z0) < TOL):
        print('Iterations stopped due to reaching tolerance')
    if (n == N - 1):
        print('Iterations stopped due to max number')
print(l, np.abs(l[-1] - z0))
