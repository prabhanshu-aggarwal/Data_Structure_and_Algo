# -*- coding: utf-8 -*-
"""
Created on Sat May 23 19:51:27 2020

@author: Prabhanshu Aggarwal
"""
#reverse_list("hello world!")  ==>  !dlrow olleh


#Reverse of a String using recursion

def reverse_list(string):
    if len(string)==0:
        return 
    
    temp=string[0]
    reverse_list(string[1:])
    print(temp , end = "")
    
    
#Reverse of a String using recursion

def reverse_list(string):
    if len(string)==0:
        return string
    
    return reverse_list(string[1:]) + string[0]