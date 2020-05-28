# -*- coding: utf-8 -*-
"""
Created on Sun May 24 13:36:35 2020

@author: Prabhanshu Aggarwal
"""
#Example -1 :
#Fibonacci starts with 1

def fib(n):
    
    if n==1 or n==0:
        return n
    
    else:
        return fib(n-2)+fib(n-1)
    
#Fibonacci starts with 0

def fib(n):
    
    if n==1 or n==2:
        return n-1
    
    else:
        return fib(n-2)+fib(n-1)
    
    
#Example 2:
#Fibonacci Using looping Technique(Iteration Method)
 
def fib(n):
    #Pyhton Unpacking
    a,b = 0,1
    
    for i in range(n):
        a,b=b,a+b
        
    return a