"""
Singly Circular Linked List

A Singly Circular Linked List is a linked list where each node contains two parts: DATA and NEXT.
 The NEXT pointer of each node points to the next node in the sequence, forming a chain from 
 Node 1 to Node 2 to Node 3. Unlike a normal singly linked list, the NEXT pointer of the 
 last node (Node 3) does not point to NULL; instead, it points back to the first node (Node 1),
forming a circular structure. The HEAD pointer points to the first node (Node 1), 
which acts as the entry point into the list. This circular connection means that starting
from any node, you can traverse the entire list and eventually loop back to the 
starting node, since the last node always points back to the first node.

* Elementary Operations :::
1> Insertion
2> Deletion
3> Traversing 
4> Searching
5> Checking The Empty List 


Difference Between Sll and Circular LL :-->>>>

SLL (Singly Linked List)

Deletion:
1) First - No traversing required
2) Last - Traversing required

Insertion:
1) At start - No traversing required
2) At last - Traversing required

CLL (Circular Linked List)
Insertion:
1) Start - No traversing
2) Last - No traversing

(Diagram: "Last" pointer box points directly to the last node in the linked list.
 Nodes are connected in a chain — item/next → item/next → item/next → item/next — with the 
 last node's next looping back to the first node.)

Deletion:
1) Start - No traversing
2) Last - Traversing
"""

