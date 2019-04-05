# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 15:43:09 2019

@author: benma
"""

#%%
import numpy as np

P = 11

def prime_check(N):
    for i in range(N):
        is_prime = True
        if (N >= 2):
            for i in range(2, N):
                if((N % i) == 0 and N != i):
                    is_prime = False
            return is_prime

count = np.zeros([0, 2])
for p in range(2, P):
    count1 = 0
    if(prime_check(p) == True):
        for i in range(0, p, 1):
            for j in range(0, p, 1):
                if(i == j**2):
                    count1 = count1 + 1
        count = np.vstack([count, np.array([p, count1])])
print("Number of quadratic residues in Zp: ", count)
                    
neg_one = np.zeros([0, 2])
for p in range(2, P):
    n1 = 0
    if(prime_check(p) == True):
        for a in range(0, p, 1):
            if((p-1) == a**2):
               n1 = 1
        neg_one = np.vstack([count, np.array([p, n1])])
print("Is -1 a quadratic residue in Zp?: ", neg_one)
                
        


        

