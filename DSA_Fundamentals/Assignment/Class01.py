"""
Q1 (Basic): Create a Student class with attributes (name, roll_no, marks) and
 a method to display details.
"""
class Student:

    def __init__(self,name,roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        return(f"The details of student :name ->{self.name}, roll_no -> {self.roll_no}, marks ->{self.marks}")

obj = Student("Aman", 4, 87.34)
print(obj.display())