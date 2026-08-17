"""
Assignment-8: Stack extending list

Define a class Stack to implement stack data structure by extending list class.
Define a method is_empty() to check if the stack is empty in Stack class.
In Stack class, define push() method to add data onto the stack.
In Stack class, define pop() method to remove top element from the stack.
In Stack class, define peek() method to return top element on the stack.
In Stack class, define size() method to return size of the stack that is number of items
present in the stack.
Implement a way to restrict use of insert() method of list class from stack object.
"""

class Stack(list):

    def is_empty(self):
        return len(self)==0
    def push(self, data):
        self.append(data)
    def pop(self):
        if not self.is_empty():
            super().pop()
        else:
            raise IndexError("Stack is empty !")
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else :
            raise IndexError("Stack is empty !")
    def size(self):
        return len(self)
    def insert(self, index, data):
        raise AttributeError("No attribute 'Insert', in Stack !")

s1 = Stack()
# s1.insert(0,10)
s1.push(10)
s1.push(20)
s1.push(30)
print("Top element :", s1.peek())
print()       