# -*- coding: utf-8 -*-
"""
Created on Fri May  8 11:30:38 2020

@author: Prabhanshu Aggarwal
"""

#Find the maximum continuous sum 
def large_cont_sum(arr):
    
    if len(arr)==0:
        return 0
    
    current_sum = max_sum = arr[0]
    
    for num in arr[1:]:
        #we done this for negative numbers
        current_sum = max(current_sum+num , num)
        max_sum = max(current_sum, max_sum)
        
    return max_sum