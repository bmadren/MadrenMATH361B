# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 16:44:03 2019

@author: benma
"""
#%%
x = 220
def d(x):
    l = []
    for i in range(1,x-1):
        if(x/i == int(x/i)):
            l.append(i)
    return l

m = []   
for j in range(1,300):
    if(sum(d(x)) == j and sum(d(j)) == x):
        m.append(x)
        m.append(j)
    print(m)
