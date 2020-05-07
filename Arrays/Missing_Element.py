# -*- coding: utf-8 -*-
"""
Created on Thu May  7 12:44:48 2020

@author: Prabhanshu Aggarwal
"""
#-------------Solution 1------------------
def dfinder(arr1, arr2):
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)
    l = len(arr1)
    print(l)
    print(arr1)
    print(arr2)
    for i in range(0,l):
        #used for last element
        if(arr1[i]==arr1[l-1]):
            print((arr1[i]))
            break
            
        if(arr1[i]!=arr2[i]):
            print((arr1[i]))
            break
        
#-------------Solution 2------------------       
from collections import defaultdict
def dfinder(arr1, arr2):
    #used so we key dont need to be already present
    d = defaultdict(int)
    for num in arr2:
        d[num] += 1
    
    for num in arr1:
        if(d[num]==0):
            return num
        else:
            d[num]-=1
    