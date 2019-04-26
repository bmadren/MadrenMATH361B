# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 19:09:17 2019

@author: benma
"""
#%%
import numpy as np
#polynomials f and g respresented as lists of coefficients,
#where the ith element of each list is the coefficient of the
#x^i term of each polynomial.
f = [2, 4, 0, -1]
g = [3, 5, 1]
qp = np.zeros([])
lt = []
lt1 = []
s = []
di = []

def deg(f):
    d = len(f) - 1
    return d

def add(f, g, s):
    for i in range(0, len(f)):
        s = [f[i] + g[i]]
    return s

def diff(f, g, di):
    for j in range(0, len(f)):
        di = [f[j] - g[j]]
    return di

def LTQ(F, G):
    ltr = f[-1]
    ltg = g[-1]
    lt.append(qp)
    lt.remove(0)
    lt.append(ltr / ltg)
    return lt

def LTQP(F, G):
    ltr = f[-1]
    ltg = g[-1]
    lt1.append(qp)
    lt1.remove(0)
    lt1.append((ltr // ltg) * g)
    return lt1

def qr(f, g):
    q = []
    r = f
    while(r != 0 and deg(g) <= deg(f)):
        q = add(q, LTQ(f, g), s)
        r = diff(r, LTQP(f, g), di)
    return q, r

q1, r1 = qr(f, g)       
print("Function f: ", f, "Function g: ", g, "Quotient: ", q1, "Remainder: ", r1)