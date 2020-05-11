# -*- coding: utf-8 -*-
"""
Created on Mon May 11 16:37:42 2020

@author: Prabhanshu Aggarwal
"""

class queue():
    
    def __init__(self):
        self.items = []
        
    def isempty(self):
        return self.items == []
    
    def enqueue(self, item):
        return self.items.insert(0, item)
        
    def dequeue(self):
        print(self.items.pop())
        
    def size(self):
        return len(self.items) 