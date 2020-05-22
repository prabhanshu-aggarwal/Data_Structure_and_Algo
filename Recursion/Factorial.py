# -*- coding: utf-8 -*-
"""
Created on Fri May 22 10:24:04 2020

@author: Prabhanshu Aggarwal
"""

#Factorial
def fact(n):
    
    if n==1:
        return 1
    
    else:
        return n* fact(n-1)
    
        
    
# Memoized Factorial Pseducode
        
# =============================================================================
# function factorial (n is a non-negative integer)
#     if n is 0 then
#         return 1 [by the convention that 0! = 1]
#     else if n is in lookup-table then
#         return lookup-table-value-for-n
#     else
#         let x = factorial(n – 1) times n [recursively invoke factorial
#                                          with the parameter 1 less than n]
#         store x in lookup-table in the nth slot [remember the result of n! for later]
#         return x
#     end if
# end function
# =============================================================================
