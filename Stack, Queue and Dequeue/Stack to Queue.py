# -*- coding: utf-8 -*-
"""
Created on Tue May 12 22:21:58 2020

@author: Prabhanshu Aggarwal
"""
#Program to use two stack and convert into qeueue
#stack pop in reverse order while queue pop in same order as they enter..

class stack2queue():
    
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
        
    def enqueue(self, item):
        self.in_stack.append(item)
        
    def dequeue(self):
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())
            
        return self.out_stack.pop()
        
        