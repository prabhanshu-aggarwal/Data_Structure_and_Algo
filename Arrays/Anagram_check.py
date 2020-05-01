# -*- coding: utf-8 -*-
"""
Created on Fri May  1 20:57:05 2020

@author: Prabhanshu Aggarwal
"""
#Program To Check Anagram
#-------------------------------Solution 1:--------------------------
def anagram(s1, s2):
    
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    
    return sorted(s1)==sorted(s2)


#--------------------------------Solution 2:---------------------------

def anagram(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    
    if len(s1) != len(s2):
        return False
    
    #find the frequency of each letter
    count = {}
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
            
    for letter in s2:
        if letter in count:
            count[letter] -= 1
            
        else:
            count[letter] = 1
            
    for k in count:
        if count[k] != 0:
            return False
        
    return True