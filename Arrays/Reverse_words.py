# -*- coding: utf-8 -*-
"""
Created on Fri May  8 12:42:50 2020

@author: Prabhanshu Aggarwal
"""
        
#-------------Solution 1------------------   
def rev_words(text): 
    for str in reversed(text.split()):
        print(str , end =" ")
    
        
#-------------Solution 2------------------     
def rev_words(text):
    return " ".join(reversed(text.split()))


        
#-------------Solution 3------------------   
def rev_words(text):
    return " ".join(text.split()[::-1])