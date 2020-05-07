# -*- coding: utf-8 -*-
"""
Created on Thu May  7 12:44:48 2020

@author: Prabhanshu Aggarwal
"""
#
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
        fnfn