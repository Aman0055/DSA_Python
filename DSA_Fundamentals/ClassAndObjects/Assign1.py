"""
__init__() --> method in python : 

class test :
    def __init__(self):
        self.a = 5   # instance object variable
        self.b = 6
        # return type 

t1 = test()   # ----> __init__(t1)


Note : here a and b are instance object variables 
"""


class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
t1 = Test(3,4)
t2 = Test(5,6) 
print(t1.a, t1.b)
print(t2.a, t2.b)