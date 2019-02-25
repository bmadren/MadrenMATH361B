# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 20:58:00 2019

@author: benma
"""

def prime_check(N):
    is_prime = True
    if (N >= 2):
        for i in range(2, N):
            if((N % i) == 0 and N != i):
                is_prime = False
    else:
        return False
    return is_prime

n = 6
plist = []
count = 1
while(n >= len(plist)):
    if(prime_check(count) == True):
        plist.append(count)
    count = count + 1

print("The ", n," prime number is ", plist[-2])           