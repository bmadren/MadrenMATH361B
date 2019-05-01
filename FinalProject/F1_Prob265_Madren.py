# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 12:10:32 2019

@author: benma
"""
#%%
N = 5
nbs = 2**N
h = []
j = []
k = []
m = []
c = 0
c1 = h + j
d = 0
d1 = k + m

def r(c1, d1):
    for j in range(1, nbs, 1):
        d1 = c1 * j
    return d1
    
for i in range(1, nbs, 1):
   if (h == j and len(h) < N and len(j) < N):
       h.append(0)
       h.append(1)
       j.append(0)
       j.append(1)
   c = c + 4
   if (k == m and len(k) < N and len(m) < N):
       k.append(0)
       k.append(1)
       m.append(0)
       m.append(1)
   d = d + 4
   if(c1 == r(c1, d1)):
       break
       continue
    
print("There are ", c, " binary circles. The elements are ", h, j, ".")
