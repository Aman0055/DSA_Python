"""
create a class Employee with the attribute empid, name , salary and also define methods to acess
properties of employee 
"""

class Employee:

    def __init__(self, empId=None, empName=None, empSalary=None):
        self.empId = empId
        self.empName = empName
        self.empSalary = empSalary

    # Create setter method :
    def set_empId(self, empId):
        self.empId = empId
    def setempName(self, empName):
        self.empName = empName
    def set_empSalary(self, empSalary):
        self.empSalary = empSalary

    # Create getter method :
    def get_empId(self):
        return self.empId
    def get_empName(self):
        return self.empName
    def get_empSalary(self):
        return self.empSalary

# call the fn 
e1 = Employee()
e2 = Employee(1,"Ashish", 40000)
e1.set_empId(2)
e1.setempName("Gautam")
e1.set_empSalary(500000)
print(e1.get_empId(), e1.get_empName(), e1.get_empSalary())
print(e2.get_empId(), e2.get_empName(), e2.get_empSalary())
