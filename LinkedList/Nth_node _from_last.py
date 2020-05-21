# -*- coding: utf-8 -*-
"""
Created on Wed May 20 20:30:15 2020

@author: Prabhanshu Aggarwal
"""

class Node:
     def __init__(self, value):
            self.value = value
            self.next_node = None
            
class LinkedList():
    
    def __init__(self):
        self.head = None
        
    def Nth(self, nval):
        left=self.head
        right=self.head
        inc=0
        while(right is not None):
            if(inc>=nval):
                left = left.next_node
                right=right.next_node
            else:
                right=right.next_node       
            inc+=1        
        print(left.value)
        
    def printList(self): 
        temp = self.head 
        while(temp): 
            print (temp.value)
            temp = temp.next_node
        
    
list1 = LinkedList()
list1.head=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
e=Node(5)
f=Node(6)
g=Node(7)

list1.head.next_node = b
b.next_node = c
c.next_node = d
d.next_node = e
e.next_node = f
f.next_node = g

list1.Nth(5)