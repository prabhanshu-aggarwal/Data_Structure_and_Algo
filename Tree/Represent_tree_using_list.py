# -*- coding: utf-8 -*-
"""
Created on Sun May 31 11:37:12 2020

@author: Prabhanshu Aggarwal
"""

#Tree Representation of Binary Tree Using Lists

def BinaryTree(r):
    return [r,[],[]]
    
def InsertLeft(root, newbranch):
    t = root.pop(1)
    
    if len(t)>1:
        root.insert(1, [newbranch,t,[]])
        
    else:
        root.insert(1,[newbranch,[],[]])
    return root
        
def InsertRight(root, newbranch):
    t = root.pop(2)
    
    if len(t)>1:
        root.insert(2, [newbranch,[],t])
        
    else:
        root.insert(2,[newbranch,[],[]])
    return root
        
def getRootVal(root):
    return root[0]

def setRootVal(root,newroot):
    root[0]=newroot
    
def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]



r = BinaryTree(3)
InsertLeft(r,5)
InsertRight(r,6)