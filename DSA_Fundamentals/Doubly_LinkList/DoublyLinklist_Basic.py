"""
Doubly Linked List

Doubly Linked List is a linear data structure.

Structure:
- It starts with a "Start" pointer that points to the first node.
- Each node contains three parts: prev, item, next
  - prev: pointer to the previous node
  - item: the actual data stored in the node
  - next: pointer to the next node
- The prev of the first node and the next of the last node point to X (null), indicating 
the ends of the list.

Example layout:
Start -> [X | item | next] <-> [prev | item | next] <-> [prev | item | X]

Elementry Operations :::--->>>
* Insertion
* Deletion
* Traversing
* Searching
* Checking for empty list
"""