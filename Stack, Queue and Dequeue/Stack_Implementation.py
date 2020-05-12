# -*- coding: utf-8 -*-
"""
Created on Mon May 11 15:20:54 2020

@author: Prabhanshu Aggarwal
"""

class stack():
    
    def __init__(self):
        self.items = []
    
    def isempty(self):
        return self.items==[]
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def ispeek(self):
        return self.items.item[len(self.items)-1]
        
    def size(self):
        return len(self.items)S