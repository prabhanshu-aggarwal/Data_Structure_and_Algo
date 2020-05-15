# -*- coding: utf-8 -*-
"""
Created on Fri May 15 16:52:49 2020

@author: Prabhanshu Aggarwal
"""
#Insertion at the Beginning of the LL
class Node: 
    
    def __init__(self, data_value=None):
        self.data_value=data_value
        self.next_val = None
        
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def value(self):
        v = self.head
        while v is not None:
            print(v.data_value)
            v = v.next_val
               
    def AtBeginning(self, newdata):
        newnode = Node(newdata)
        
    #Change the values
        newnode.next_val = self.head
        self.head = newnode
          
        
list1 = LinkedList()
list1.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
e4 = Node("Thur")  
list1.head.next_val = e2
e2.next_val = e3
e3.next_val = e4

list1.AtBeginning("Sun")
list1.value()