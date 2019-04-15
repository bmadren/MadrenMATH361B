# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 14:56:05 2019

@author: benma
"""
#%%
#polynomial p respresented as a list of coefficients,
#where the ith element of the list is the coefficient of the
#x^i term of the polynomial.
p = [2, 4, 0, -1]
g = []
d = []
i = []
t = []
#Evaluate
def P(x):
    for i in range(len(p)):
        l = x**i
        g.append(p[i]*l)
    return sum(g)
#Derivative
def deriv(x):
    for ii in range(len(p)):
        k = x**(ii - 1)
        m = p[ii] * ii
        d.append(m*k)
    return sum(d)
#Definite Integral
def integ(x, y):
    for j in range(len(p)):
        n = x**(j + 1)
        h = p[j] * (1/(j + 1))
        i.append(h*n)
    for c in range(len(p)):
        r = y**(c + 1)
        s = p[c] * (1/(c + 1))
        t.append(s*r)
    return (sum(i) - sum(t))
    
print(P(2), deriv(2), integ(3, 2))