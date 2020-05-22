# -*- coding: utf-8 -*-
"""
Created on Fri May 22 10:27:22 2020

@author: Prabhanshu Aggarwal
"""

#Sum of digits

def sod(n):
    if (n<10):
        return n
    else:
        return n%10 + sod(int(n/10) )