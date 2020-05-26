# -*- coding: utf-8 -*-
"""
Created on Sun May 24 17:20:33 2020

@author: Prabhanshu Aggarwal
"""

from  threading import *

def fun():
    for i in range(6):
        print("child executing...  ", current_thread().getName()) #current_thread().getName() == To get the thread name
    
t1 = Thread(target=fun)
t1.start()
t1.join()   #it will stop parent thread to run before the child thread
print("parent thread says bye.....  ", current_thread().getName())



#With Extending Thread Class
import threading
class A(threading.Thread):
    def run(self):
        for x in range(5):
            print("Child Executing..")
            
obj=A()
obj.start()
obj.join()
print("Parent")
        
		
#Without Extending Thread Class
from  threading import *
class A():
    def fun(self):
        for x in range(5):
            print("Child Executing..")
obj=A()            
t1=Thread(target=obj.fun)
t1.start()
t1.join()
print("Parent")
        