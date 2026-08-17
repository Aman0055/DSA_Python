# SLL Creation :

# Note as per the question segement we develop the class :::
"Question 1>: Define a class Node to describe a node of a singly linked list ?"
"Question 2>: Define a class SLL to impliment a singly linked list with __init__() method to create initialise start reference variable"
"Question 3>: Define method is empty() to check if the linked list is empty in SLL class"
"Question 4>: In class SLL, define a method insert_at_start() to insert an element at the starting of the list ??"
"Question 5>: In class SLL, define a method insert_at_last() to insert an element at the end of the list??"
"Question 6>: In class SLL, define a method search() to find node with specified element value"
"Question 7>: In class SLL, define a method insert_after() , to insert a new node after a given node of the list??"
"Question 8>: In a class SLL, define a method to print all elements in a list "
"Question 9>: In class SLL, implement iterator for SLL to acceess all the elements of the list in a sequence"
"Question 10>: In class SLL, define a method delete_first(), to delete first element from the list"
"Question 11>: In class SLL, define a method delete_last(), to delete the last element from the list"

class Node:

    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class SLL:

    def __init__(self,start=None):
        self.start = start
    def is_empty(self):
        return self.start == None
    def insert_at_start(self, data):
        n = Node(data,self.start)
        self.start = n
    def insert_at_last(self, data):
        n = Node(data)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        else:
            self.start = n
    def search(self,data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None
    def insert_after(self,temp,data):
        if temp is not None:
            n = Node(data, temp.next)
            temp.next=n
    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=' ')
            temp = temp.next

    # Check string method for show the reference of class object
    def __str__(self):
        temp = self.start
        result = []
        while temp is not None:
            result.append(str(temp.item))
            temp = temp.next
        return ' -> '.join(result)

    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None

    def delete_item(self,data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item == data:
                self.start = None
        else :
            temp = self.start
            if temp.item == data:
                self.start = temp.next
            else :
                while temp.next is not None:
                    if temp.next.item == data:
                        temp.next = temp.next.next
                        break
                    temp=temp.next
    def __iter__(self):
        return SLLIter(self.start)
#Class Iterator :
class SLLIter:
    def __init__(self, start):
        self.current =start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data
# Driver Class 
myList = SLL()
myList.insert_at_start(20)
myList.insert_at_start(10)
myList.insert_at_last(40)
myList.insert_after(myList.search(20),25)
myList.print_list()
myList.delete_item(25)
print()
myList.print_list()
print(myList)
for x in myList:
    print(x, end=' ')
print()

