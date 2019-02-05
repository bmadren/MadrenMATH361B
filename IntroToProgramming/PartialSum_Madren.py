# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 19:45:29 2019

@author: benma
"""
#%%
from math import log
N = 30
sum=0
sums=[]

for nn in range(1,N+1):
    sum += (log(nn**4+nn+1)**2)/((nn)**(1/2)+3)
    sums.append(sum)
    
print("The terms are ", sums)

#%%
from math import exp
N=30
sum=0
sums=[]

for nn in range(1,N+1):
    sum += ((exp(nn/100))/(nn**10))
    sums.append(sum)
    
print("The terms are ", sums)

#%%
from math import exp
N=30
sum=0
sums=[]

for nn in range(1,N+1):
    sum += ((nn+1)**2)/(exp(nn))
    sums.append(sum)
    
print("The terms are ", sums)