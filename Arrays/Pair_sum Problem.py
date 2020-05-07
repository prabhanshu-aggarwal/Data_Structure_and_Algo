# -*- coding: utf-8 -*-
"""
Created on Thu May  7 11:55:28 2020

@author: Prabhanshu Aggarwal
"""

def pair_sum(arr , k):
    seen =set()
    output =set()
    
    for num in arr:
        target = k-num
        if target not in seen:
            seen.add(num)
        else:
            output.add(((min(num, target)), max(num, target)))
    print((output))
    print(list(output))
    return '\n'.join(map(str, list(output)))
            
        
        