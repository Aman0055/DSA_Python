"""
Pattern 1: Traversal & Counting

Q1 (Basic): Find the length of a singly linked list (iterative).
Q2 (Basic): Find the middle node of a linked list in a single pass (slow/fast pointers).
Shared behavior: Both just walk the list with pointers and track state — no modification of 
links.

Pattern 2: Reversal

Q3 (Basic): Reverse an entire singly linked list.
Q4 (Intermediate): Reverse a linked list between position m and n (partial reversal).
Shared behavior: Both use the classic prev/curr/next pointer-rewiring loop — Q4 just
 adds boundary bookkeeping.

Pattern 3: Fast & Slow Pointers (Cycle Detection Family)

Q5 (Basic): Detect if a linked list has a cycle (Floyd's algorithm).
Q6 (Intermediate): Find the starting node of the cycle, if one exists.
Shared behavior: Same slow/fast pointer setup; Q6 extends Q5 with the math to locate the
 entry point once a cycle is confirmed.

Pattern 4: Merging Two Lists

Q7 (Basic): Merge two sorted linked lists into one sorted list.
Q8 (Intermediate): Merge k sorted linked lists into one sorted list.
Shared behavior: Both compare node values and stitch pointers together — Q8 is 
just Q7
 generalized (divide & conquer or a heap over multiple lists).

Pattern 5: Remove Nth Node / Duplicates

Q9 (Basic): Remove duplicates from a sorted linked list.
Q10 (Intermediate): Remove the N-th node from the end of a linked list in one pass.
Shared behavior: Both use a single forward pass with careful pointer skipping 
(Q10 adds a two-pointer gap technique) and both need a dummy head to handle edge cases
 (removing the head node) cleanly.
"""