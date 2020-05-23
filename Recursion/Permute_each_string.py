# -*- coding: utf-8 -*-
"""
Created on Sat May 23 19:55:11 2020

@author: Prabhanshu Aggarwal
"""
#permute('abc') ==> ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

def permute(s):
    
    out = []
    
    if len(s)==1:
        out = [s]
        
    else:
        
        #for each letter in the string 
        for i, let in enumerate(s):
                
                for perm in permute(s[:i]+s[i+1:]):
                    
                    out+=[let+perm]
                    
    return out