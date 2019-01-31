# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 19:43:25 2019

@author: benma
"""

#%%
#Input Variables
x
y
z
#List
mylist = []
mylist.append(x + y)
mylist.append(y * z + 3 * x)
mylist.append(index(0)**2)
mylist.append((2*index(1) - x/2)/index(0))
mylist.append(7 % 3)

mylist.append(index(2) + 3, index(2))
mylist.append(index(4) * (3/4), index(4))
print("The sum of all components is ", sum(mylist))
