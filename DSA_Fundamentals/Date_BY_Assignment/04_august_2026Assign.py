"""
# Today's Assignment — OOPs

## 🟢 Basic (7)

1. Create a `Car` class with `brand`, `model`, and `mileage`. Add a method `display_info()` that prints all details in a formatted string.
2. Create a `BankAccount` class with a class variable `bank_name = "SBI"` shared by all objects, and instance variables `account_holder` and `balance`.
3. Explain the difference between a class attribute and an instance attribute with a small `Team` class example.
4. Create a `Rectangle` class that takes `length` and `width` and has methods `area()` and `perimeter()`.
5. Create a `Product` class with a method `apply_gst(rate)` that updates and returns the price after adding GST.
6. What is abstraction? Demonstrate it using a `Vehicle` class where internal `__engine_status` is hidden and only accessible via a `start_engine()` method.
7. Create two classes `Engine` and `Car`, where `Car` "has-a" `Engine` (composition) — demonstrate starting the car through the engine object.

## 🟡 Intermediate (5)

1. Create a base class `Shape` with a method `area()`, and derived classes `Square`, `Circle`, `Triangle` that override it. Loop through a list of shape objects and call `area()` on each (polymorphism).
2. Demonstrate the use of `super()` in a derived class `SavingsAccount` that inherits from `BankAccount`, calling the parent constructor before adding an `interest_rate` attribute.
3. Create an abstract base class `Notification` (using `abc`) with an abstract method `send(message)`, implemented differently in `EmailNotification` and `SMSNotification` classes.
4. Explain the difference between method overloading and method overriding. Show a workaround for overloading in Python using default arguments in a `Calculator` class.
5. Implement `__eq__` and `__lt__` in a `Product` class so that product objects can be compared by price, and can be sorted using `sorted()`.

## 🔴 Advance (3)

1. Design an "Online Food Ordering System" using OOP — classes for `Restaurant`, `MenuItem`, and `Order`, with proper encapsulation and a method to calculate the total order bill.
2. Implement the Singleton design pattern: a `Logger` class that ensures only one instance of it can ever be created, no matter how many times it's instantiated.
3. Build a small "School Management System" showing multilevel inheritance (`Person` → `Staff` → `Teacher`) with method overriding at each level, and a method that prints the full inheritance chain of any given object using `__class__.__mro__`.

# Today's Assignment — Exception Handling

## 🟢 Basic (7)

1. Write a program that takes two numbers and performs division, handling `ZeroDivisionError` and printing a friendly custom message.
2. Write a program that converts a list of user-entered strings to floats, handling `ValueError` for any invalid entry (skip and continue).
3. Explain what happens when an exception is NOT caught — write an example and describe how to read the traceback.
4. Write a program that accesses a list by index and handles `IndexError` by returning `None` instead of crashing.
5. Write a program using `try-except-else` where the `else` block only runs if a file read succeeds without error.
6. Explain the purpose of the `finally` block using an example where a database connection is always closed regardless of an exception.
7. Write a program that raises a `ValueError` manually using `raise` when a user enters a negative amount for a withdrawal.

## 🟡 Intermediate (5)

1. Create a custom exception `InsufficientBalanceError` and use it in a `withdraw(amount)` method that raises it if the withdrawal exceeds the balance.
2. Write a program that handles `TypeError`, `KeyError`, and a generic `Exception` in the same block, printing which specific exception occurred.
3. Demonstrate how exceptions propagate up the call stack through three nested function calls, and where you'd ideally place the `try-except`.
4. Write a custom exception class that accepts an error code and message in its constructor and prints both when caught.
5. Explain assertions (`assert`) vs exceptions — write a small example using `assert` for a precondition check in a function that computes a square root.

## 🔴 Advance (3)

1. Design a custom exception hierarchy for an "E-commerce System" (`OrderError` as base, with `OutOfStockError`, `PaymentFailedError`, `InvalidCouponError` as subclasses) and use them in an `Order` class.
2. Implement a logging mechanism that catches exceptions across a program and logs them to a file with timestamps (using the `logging` module) instead of just printing them.
3. Write a custom context manager class (with `__enter__`/`__exit__`) that wraps a database transaction, commits on success, and rolls back and re-raises on any exception.

# Today's Assignment — Arrays

## 🟢 Basic (7)

1. Find the second largest element in an array without sorting it.
2. Check whether a given array is a palindrome (reads the same forward and backward).
3. Rotate an array to the left by `k` positions using a temporary array.
4. Find the sum and average of all elements in an array.
5. Merge two arrays into one and remove duplicate elements from the result.
6. Count how many elements in an array are greater than a given value.
7. Given an array, move all zeros to the end while keeping the relative order of non-zero elements.

## 🟡 Intermediate (5)

1. Find all pairs in an array whose sum equals a given target (without using extra space for a hash set — two-pointer approach on a sorted copy).
2. Given a sorted array, find the first and last occurrence of a given target element.
3. Find the maximum subarray sum using Kadane's Algorithm.
4. Given an array, find the missing number in a range from 1 to n (only one number is missing).
5. Rearrange an array so that positive and negative numbers alternate, starting with a positive number.

## 🔴 Advance (3)

1. Given an array, find the maximum product subarray (contiguous elements) considering that negative numbers can flip the sign.
2. Given an array of stock prices by day, find the maximum profit achievable with at most two transactions (Best Time to Buy and Sell Stock III).
3. Given an unsorted array, find the length of the longest consecutive sequence of numbers without sorting the array.

# Today's Assignment — Singly Linked List

## 🟢 Basic (7)

1. Implement a `Node` class (with `data` and `next`) and a `SinglyLinkedList` class with `insert_at_end()` and `display()` methods.
2. Write a method `insert_at_beginning()` to add a node at the head of a singly linked list.
3. Write a method `get_length()` that returns the total number of nodes without using a counter passed as a parameter.
4. Write a method `search(value)` that returns the position (index) of a value if it exists, or -1 if not found.
5. Write a method `delete_at_position(index)` to delete a node at a given index.
6. Write a method to find the sum of all node values in a singly linked list of integers.
7. Write a method `insert_after_value(target, value)` that inserts a new node right after the node containing `target`.

## 🟡 Intermediate (5)

1. Reverse a singly linked list iteratively (changing `next` pointers in a single pass).
2. Check whether a singly linked list is a palindrome (using the slow/fast pointer technique to find the middle).
3. Given two singly linked lists representing numbers (digit by digit), add them and return the result as a new linked list.
4. Rotate a singly linked list to the right by `k` places.
5. Find the intersection point of two singly linked lists (where they merge into one), without using extra space.

## 🔴 Advance (3)

1. Reverse a singly linked list in groups of `k` nodes (e.g., reverse every 3 nodes) and connect the groups back together.
2. Flatten a multilevel singly linked list where some nodes have an additional `child` pointer to another linked list, into a single-level list.
3. Given a singly linked list with a cycle, remove the cycle so the list becomes a proper NULL-terminated list, without losing any nodes.

# Today's Assignment — Doubly Linked List

## 🟢 Basic (7)

1. Implement a `Node` class (with `data`, `next`, and `prev`) and a `DoublyLinkedList` class with `insert_at_end()` and `display()` (forward direction) methods.
2. Write a method `insert_at_beginning()` for a doubly linked list, making sure both `next` and `prev` pointers are updated correctly.
3. Write a method `display_reverse()` that traverses and prints a doubly linked list from tail to head using the `prev` pointers.
4. Write a method `get_node_at(index)` that returns the node at a given position, traversing from whichever end (head or tail) is closer.
5. Write a method `insert_before_value(target, value)` that inserts a new node right before the node containing `target`.
6. Write a method to delete a node given only its value (search then delete, updating neighboring pointers correctly).
7. Write a method `to_list()` that converts a doubly linked list into a plain Python list.

## 🟡 Intermediate (5)

1. Write a method `insert_at_position(index, value)` for a doubly linked list, correctly linking both `next` and `prev` pointers of neighboring nodes.
2. Remove duplicate values from a doubly linked list while preserving the order of first occurrence.
3. Reverse a doubly linked list in-place by swapping `next` and `prev` at every node (and updating the head pointer).
4. Implement `delete_node(node_reference)` in O(1) given a direct reference to the node (not the head), leveraging the `prev` pointer.
5. Find the middle node of a doubly linked list using the slow/fast pointer technique.

## 🔴 Advance (3)

1. Implement a basic LRU (Least Recently Used) Cache using a doubly linked list + hash map, supporting `get(key)` and `put(key, value)` in O(1) time.
2. Given a doubly linked list where each node also has a `child` pointer to another doubly linked list, flatten it into a single-level doubly linked list.
3. Given a doubly linked list, sort it (e.g., using merge sort adapted for doubly linked lists) without converting it to an array first.


## 🟢 Basic (7)
 
1. Implement a `Node` class and a `CircularLinkedList` class with `insert_at_end()` that correctly links the last node back to the head.
2. Write a method `insert_at_beginning()` for a circular linked list, making sure the new head's `next` still points back correctly and the old last node updates too.
3. Write a method `display()` for a circular linked list that prints all nodes exactly once (careful not to loop forever).
4. Write a method `count_nodes()` that returns the total number of nodes in a circular linked list.
5. Write a method `search(value)` that returns True/False if a value exists in a circular linked list.
6. Write a method to delete the first node of a circular linked list, correctly re-linking the last node to the new head.
7. Write a method to delete the last node of a circular linked list, correctly updating the new last node's `next` pointer.
 
## 🟡 Intermediate (5)
 
1. Write a method `insert_at_position(index, value)` to insert a node at a given index in a circular linked list.
2. Write a method to delete a node by value from a circular linked list (handle the case where it's the only node, the head, or the tail).
3. Split a circular linked list into two halves, each forming its own circular linked list.
4. Convert a given singly linked list into a circular linked list in-place (link the last node back to the head).
5. Detect whether a given linked list (passed without any "is circular" flag) is actually circular or a normal NULL-terminated list.
 
## 🔴 Advance (3)
 
1. Solve the Josephus Problem using a circular linked list: given `n` people in a circle and every `k`-th person eliminated, find the last remaining person.
2. Given a circular linked list, find the starting node of the loop if it were merged into a bigger list at an unknown point (i.e., locate the "junction" node).
3. Implement a circular doubly linked list (each node has `next` and `prev`, and the list wraps in both directions) supporting O(1) insertion and deletion at both ends.
"""