# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 12:29:09 2019

@author: benma
"""

#%%
N = 50
m = 4
terms = [0] * N
multiples_m= []
index_multiples = []

for n in range(N):
    if n == 0:
        terms[0] = 0
    elif n == 1:
        terms[1] = 1
    elif (n != 1) or (n != 2):
        terms[n] = terms[n-1] + terms[n-2]
        
for i in range(len(terms)):
    if(terms[i] % m == 0):
        multiples_m.append(terms[i])
        index_multiples.append(i)
        
percent_m = (len(multiples_m))/(len(terms)) * 100
        
print(len(multiples_m))
print("The values ", multiples_m, " are all divisible by ", m)
print("The percentage of the first", N, "terms that are multiples of", m, "is", percent_m, "percent")