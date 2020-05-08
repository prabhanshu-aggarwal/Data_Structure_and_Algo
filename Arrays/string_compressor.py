# -*- coding: utf-8 -*-
"""
Created on Fri May  8 13:44:10 2020

@author: Prabhanshu Aggarwal
"""
#Compress the words
#Ex : compress("AAABBCCCCaaaaa")  ==  "A3B2C4a5"
def compress(text):
    
    l = len(text)
    st=""
    c=1
    for i in range(1, l):
        if(text[i]==text[i-1]):
            c += 1
        else:
            st = st+ text[i-1] + str(c)
            c=1
    print(st)
    i=l        
    st = st+ text[i-1] + str(c)
    return st