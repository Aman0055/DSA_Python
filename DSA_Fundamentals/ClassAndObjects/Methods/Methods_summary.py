"""
Methods :--->>>>

1> Class Method
2> Instance Method
3> Static Method 
"""

class Test:

    x = 5
    def __init__(self, a , b):
        self.a = a
        self.b = b

    def show(self):                 # Instance method
        print(self.a, self.b)

    @staticmethod                    # static method 
    def f2():
        print("Welcome to the programming ::")
    
    @classmethod                    # class method 
    def f3(cls):
        print(cls.x)

t1 = Test(2,3)
t2 = Test(4,5)
t1.show()
t2.show()
Test.f2()
Test.f3()
