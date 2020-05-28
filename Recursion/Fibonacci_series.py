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
    
-------------------------------------------------------------------    
#Example 2:
#Fibonacci Using looping Technique(Iteration Method)
 
def fib(n):
    #Pyhton Unpacking
    a,b = 0,1
    
    for i in range(n):
        a,b=b,a+b
        
    return a
	
#--------------------------------------------------	
	
#Example 3: Fib using Memoization 
fib_cache = {}

def fibdyn(n):
    #If we have the cached value, Then return it
    if n in fib_cache:
        return fib_cache[n]
    
    if n==1 or n==0:
        return n
    
    else:
        value = fib(n-2)+fib(n-1)
        
    #Store the cache value and then rturn it.
    fib_cache[n]=value
    return value
    
for i in range(1,10):
    print(i , " : " , fibdyn(i))
	
	#Method 2:Using LRU cache i.e least least recently used

from functools import lru_cache

@lru_cache()
def fibdyn(n):
    
    if n==1 or n==0:
        return n
    
    else:
        return fib(n-2)+fib(n-1)
    
for i in range(1,5):
    print(i , " : " , fibdyn(i))