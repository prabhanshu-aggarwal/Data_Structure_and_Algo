# -*- coding: utf-8 -*-
"""
Created on Tue May 19 15:09:44 2020

@author: Prabhanshu Aggarwal
"""
#Revrsed List with O(n) time complexity and O(1) Space Complexity

class Node:
     def __init__(self, value):
            self.value = value
            self.next_node = None
            
class LinkedList():
    
    def __init__(self):
        self.head = None
        
    def ReverseList(self):
        previous=None
        current=self.head
        
        while(current is not None):
            next_node=current.next_node
            current.next_node=previous #Reverse the list
            previous = current
            current=next_node
        self.head = previous
            
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

list1.head.next_node=b
b.next_node=c
c.next_node=d
print("Initial List : ")
list1.printList()
list1.ReverseList() 
print("Reversed List : ")
list1.printList()