# -*- coding: utf-8 -*-
"""
Created on Fri May  8 14:01:01 2020

@author: Prabhanshu Aggarwal
"""
#-------------Solution 1------------------
#example: uni_char("abc") == True || uni_char("abcc") == False
from collections import defaultdict
def uni_char(st):
    d = defaultdict(int)
    for i in st:
        d[i] += 1
    
    for num in d:
         if d[num]>1:
                return False
    return True


#-------------Solution 2------------------
def uni_char(st):
    print(unique(st))