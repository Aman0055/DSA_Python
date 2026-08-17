"""
Q3 (Basic): Create a Car class with a constructor and a method that prints "engine started."
"""
class Car:
    def __init__(self):
        print ("Welcome to the Car Showroom !")
    def show(self):
        print("Engine Started")

obj = Car()
obj.show()