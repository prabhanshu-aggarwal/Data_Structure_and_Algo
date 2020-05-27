#Monkey Patching
# In Python, the term monkey patch refers to dynamic (or run-time) 
#modifications of a class or module. 
#In Python, we can actually change the behavior of code at run-time.
class A():
    def ex(self):
        print("Hello")

#mon_f is my patch function
def mon_f(self):
    print("monkey is called")
    
A.ex=mon_f
obj=A()
obj.ex()