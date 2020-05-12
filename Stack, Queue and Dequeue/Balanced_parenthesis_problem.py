# -*- coding: utf-8 -*-
"""
Created on Mon May 11 20:27:23 2020

@author: Prabhanshu Aggarwal
"""
#--------------------Solution 1-------------------------
def balance(mystr):
    if (len(mystr)%2!=0):
        return False
    
    stack=[]
    openlist = set("({[")
    matches = set([("(",")"),  ("[","]"),  ("{","}")])
    for i in mystr:
        if i in openlist:
            stack.append(i)
            
        else:
            if (len(stack)==0):
                return False
            
            last_match = stack.pop()
             
            if (last_match , i) not in matches:
                    return False
                
    return len(stack)==0


#--------------------Solution 2-------------------------
open_list = ["[","{","("] 
close_list = ["]","}",")"] 
  
# Function to check parentheses 
def check(myStr): 
    stack = [] 
    for i in myStr: 
        if i in open_list: 
            stack.append(i) 
        elif i in close_list: 
            pos = close_list.index(i) 
            print(pos)
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])): 
                stack.pop() 
            else: 
                return "Unbalanced"
    if len(stack) == 0: 
        return "Balanced"
    else: 
        return "Unbalanced"