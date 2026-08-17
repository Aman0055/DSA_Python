"""
Topic --->>>>>>>>>>>>  What is List ??

                     Sol :- List is a linear collection of data item known as List item

                     Example 1 : List of marks :
                                30, 41,53,98,76,72

                    Example 2 : List of city names :
                    "Varansi" , "patna", "Gwalior", "Muzaffarpur" , "Delhi", "Mumbai" , "Bhopal"

                    Example 3: List of Employees :
                    "100" , "Aman", "25000"
                    "101", "Vansh" , 40000
                     103x, "Aditya" , 85000

    What is a Node?

Example 1: list of marks (int)
30, 32, 20, 35, 41, 38

[Start] --> [item: --  | next: --]  -->  [item: 30 | next: --]  -->  [item: 32 | next: --]  -->  [item: 20 | next: None]
                     (SLL)                        (Node type)

class Node:
    -> ?
    =


* Singly Linked List

- SLL is a linear data structure.
- It can grow and shrink.
- 
SLL_object

[Start] --> [item | next] --> [item | next] --> [item | next] --> [item | next: None]


Operations on Singly Linked List

insertion
deletion
is_empty
traverse

obj = SLL()
obj.insert_at_start(10)
obj.insert_at_last(20)
obj.insert_at_start(50)
obj.delete_first()

for x in obj:
    print(x)
"""