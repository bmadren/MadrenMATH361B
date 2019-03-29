# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 16:34:29 2019

@author: benma
""" 
#%%
def d(x):
    l = []
    for i in range(1,x-1):
        if(x/i == int(x/i)):
            l.append(i)
    print(l)
d(10)