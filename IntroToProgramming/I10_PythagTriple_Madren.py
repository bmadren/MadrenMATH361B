# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 15:00:57 2019

@author: benma
"""
#%%
import numpy as np
N = 500000
pytrips = np.zeros( [0,4] )
flag = ""

for c in range(1,N):
    for b in range(1,c-1):
        for a in range(1,b-1):
            L = a**2 + b**2
            R = c**2
            abc = a+b+c
            if L == R:
                pytrips = np.vstack( [pytrips, np.array([a,b,c,abc])] )
            if abc == 1026:
                flag = "break"
                break
        if flag == "break":
            break
    if flag == "break":
        break
print("The Pythagorean Triple where a+b+c=1026 is", pytrips[-8])
