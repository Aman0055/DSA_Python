"""
Q2 (Basic): Create a Rectangle class with methods to calculate area and perimeter.
"""

class Rectangle:

    def __init__(self, length, breathe):
        self.length = length
        self.breathe = breathe

    def area(self):
        return self.length * self.breathe

    def perimeter(self):
        return 2*(self.length + self.breathe)

obj = Rectangle(145,23)
print(obj.area())
print(obj.perimeter())