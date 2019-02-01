# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 19:43:25 2019

@author: benma
"""

#%%
#Input Variables
x = 1
y = 2
z = 3
#List
mylist = []
mylist.append(x + y)
mylist.append((y * z) + (3 * x))
mylist.append(mylist[0]**2)
mylist.append(((2*mylist[1]) - ((1/2)*x))/mylist[0])
mylist.append(7 % 3)
#Modify and sum
mylist[2] = mylist[2] + 3
mylist[4] = mylist[4] * (3/4)
def added(mylist):
    if len(mylist) == 1:
        return mylist[0]
    else:
        return mylist[0] + added(mylist[1:])
print("The sum of all components is ", added(mylist))
