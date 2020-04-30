# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 16:24:20 2020

@author: Prabhanshu Aggarwal
"""

import ctypes

class DynamicArray():

    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)
        
    def __len__(self):
        return self.n
    
    def __getitem__(self, k):
        if not 0<= k < self.n:
            return IndexError("K is out of bounds")
    
        return self.A[k]
    
    def append(self, ele):
        if self.n == self.capacity:
            self.__resize(2 * self.capacity)
        
        self.A[self.n] = ele
        self.n = self.n+1
    
    #to add an array at a specified location
    def insertAt(self, item, index):
        if not 0<=index<self.n:
            return IndexError("Out of bound")
        
        if self.n == self.capacity:
            self.__resize(2* self.capacity)
            
        for i in range(self.n-1, index-1, -1):
            self.A[i+1]= self.A[i]
            
        self.A[index] = item
        self.n +=1       
        
        
    #This function deletes item from the end of array 
    def delete(self): 
        if self.n==0: 
            print("Array is empty deletion not Possible") 
            return
          
        self.A[self.n-1]=0
        self.n-=1    
       
    #to delete from an specified index
    def removeAt(self, index):
        if self.n ==0:
            print("nothing to delete")
            return
        
        if not 0<=index<self.n:
            return IndexError("Out of bound")
        
        for i in range(index, self.n-1, 1):
            self.A[i]=self.A[i+1]
            
        self.n -=1
        
    def __resize(self, new_cap):
        B = self.make_array(new_cap)
        
        for k in range(self.n):
            B[k] = self.A[k]
            
        self.A = B
        self.capacity = new_cap
        
    def make_array(self, new_cap):
        return (new_cap * ctypes.py_object)() 
    
    
    
    
    