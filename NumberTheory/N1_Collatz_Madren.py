# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 18:56:51 2019

@author: benma
"""
#%%
an = 10
N = 7
clist = []

def collatz(an, N):
    for i in range(N):
        if(an % 2 == 0):
            an = an / 2
            clist.append(an)
        else:
           an = 3*an + 1
           clist.append(an)
        if(an == 1):
            break
  
collatz(an, N)         
if(clist[-3] == 1 or clist[-2] == 1 or clist[-1] == 1):
    print("The number of terms it took to reach 1 is ", len(clist),".")
else:
    print("1 was never reached after ", N, " terms.")
            