# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 14:47:48 2019

@author: benma
"""
#%%
import math as m


def prime_check(N):
    for i in range(int(N)):
        is_prime = True
        if (N >= 2):
            for i in range(2, int(N)):
                if((N % i) == 0 and N != i):
                    is_prime = False
                else:
                    return False
            return is_prime

N = 10000

for i in range(9,N,2):
    if(prime_check(i) == False):
        GOB = True
    #Need to find p prime and c int such that i = p + 2*(c**2)
    for p in range(1,i):
        if(prime_check(p) == False):
            continue
    for c in range(1,N,1):
        if(c != m.sqrt((i-p)/2)):
            GOB = False
    if(GOB == False):
        print("The smallest counterexample for GOC is ", i)
        break
            