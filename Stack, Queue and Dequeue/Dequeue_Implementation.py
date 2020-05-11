# -*- coding: utf-8 -*-
"""
Created on Mon May 11 17:06:28 2020

@author: Prabhanshu Aggarwal
"""

class dequeue():
    
    def __init__(self):
        self.items = []
        
    def isempty(self):
        return self.items == []
    
    def addfront(self, item):
        self.items.append(item)
        
    def addrear(self, item):
        self.items.insert(0,item)
        
    def removefront(self):
        return self.items.pop()
        
    def removerear(self):
        print(self.items.pop(0))
        
    def size(self):
        return len(self.items) 