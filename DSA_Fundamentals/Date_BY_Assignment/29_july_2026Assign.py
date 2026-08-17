"""
# Today's Assignment — OOPs

## 🟢 Basic (7)

1. Create a `Book` class with `title`, `author`, and `price`. Add a method `discounted_price(percent)` that returns the price after discount.
2. Create a `Dog` class with a class variable `species = "Canine"` shared by all objects, and instance variables `name` and `breed`.
3. Explain the difference between `__init__` and a regular method with a small `Movie` class example.
4. Create a `Circle` class that takes `radius` and has methods `area()` and `circumference()`.
5. Create a `Student` class with a method `is_pass(marks)` that returns True/False based on a passing threshold of 40.
6. What is encapsulation? Demonstrate it using a `Employee` class where `__salary` is private and accessed only via a `get_salary()` method.
7. Create two classes `Wallet` and `User`, where `User` "has-a" `Wallet` (composition) — demonstrate accessing wallet balance through the user object.

## 🟡 Intermediate (5)

1. Create a base class `Animal` with a method `sound()`, and derived classes `Cat`, `Dog`, `Cow` that override it. Loop through a list of animal objects and call `sound()` on each (polymorphism).
2. Demonstrate the use of `super()` in a derived class `Manager` that inherits from `Employee`, calling the parent constructor before adding extra attributes.
3. Create an abstract base class `PaymentMethod` (using `abc`) with an abstract method `pay(amount)`, implemented differently in `CreditCard` and `UPI` classes.
4. Explain the difference between method overloading and method overriding. Since Python doesn't support true overloading, show a workaround using default arguments or `*args`.
5. Implement `__eq__` and `__lt__` in a `Student` class so that student objects can be compared by marks, and can be sorted using `sorted()`.

## 🔴 Advance (3)

1. Design a "Hotel Room Booking System" using OOP — classes for `Room`, `Guest`, and `Booking`, with proper encapsulation and a method to check room availability before booking.
2. Implement the Factory design pattern: a `ShapeFactory` class that returns a `Circle`, `Square`, or `Triangle` object based on a string input, without the client code needing to know the class directly.
3. Build a small "Employee Management System" showing multilevel inheritance (`Person` → `Employee` → `Manager`) with method overriding at each level, and a method that prints the full inheritance chain of any given object using `__class__.__mro__`.

# Today's Assignment — Exception Handling

## 🟢 Basic (7)

1. Write a program that takes two numbers and performs division, handling `ZeroDivisionError` with a custom message.
2. Write a program that converts a list of strings to integers, handling `ValueError` for any non-numeric entry (skip and continue instead of crashing).
3. Explain what happens when an exception is NOT caught — write an example and describe the traceback.
4. Write a program that accesses a dictionary key and handles `KeyError` by providing a default value instead.
5. Write a program using `try-except-else` where the `else` block only runs if no exception occurred (e.g., successful file read).
6. Explain the purpose of the `finally` block using an example where a file is always closed regardless of an exception.
7. Write a program that raises a `ValueError` manually using the `raise` keyword when a user enters a negative number for age.

## 🟡 Intermediate (5)

1. Create a custom exception `InvalidAgeError` and use it in a function `set_age(age)` that raises it if age is negative or above 150.
2. Write a program that handles `TypeError`, `ValueError`, and a generic `Exception` in the same block, printing which specific exception occurred.
3. Demonstrate how exceptions propagate up the call stack through three nested function calls, and where you'd ideally place the `try-except`.
4. Write a custom exception class that accepts extra info (like an error code) in its constructor and prints it when caught.
5. Explain assertions (`assert`) vs exceptions — write a small example using `assert` for a precondition check in a function.

## 🔴 Advance (3)

1. Design a custom exception hierarchy for a "Library System" (`LibraryError` as base, with `BookNotFoundError`, `BookAlreadyIssuedError`, `MemberLimitExceededError` as subclasses) and use them in a `Library` class.
2. Implement a logging mechanism that catches exceptions across a program and logs them to a file (using the `logging` module) instead of just printing them.
3. Write a custom context manager class (with `__enter__`/`__exit__`) that wraps a risky operation, logs any exception that occurs, and re-raises it only if it's not of a specified "ignorable" type.

# Today's Assignment — Arrays

## 🟢 Basic (7)

1. Find the frequency of each element in an array using a dictionary.
2. Check whether a given array contains any duplicate elements.
3. Find the index of a given element in an array (linear search) without using `.index()`.
4. Compute the cumulative sum array (prefix sum) of a given array.
5. Separate an array into two lists: one with positive numbers, one with negative numbers.
6. Find the difference between the sum of even-indexed and odd-indexed elements.
7. Given an array, replace every element with the next greater element on its right (last one becomes -1) — brute-force approach is fine.

## 🟡 Intermediate (5)

1. Find the leaders in an array (an element is a leader if it's greater than all elements to its right).
2. Given a sorted array, remove duplicates in-place and return the length of the unique portion.
3. Find the equilibrium index of an array (an index where the sum of elements on the left equals the sum on the right).
4. Given an array of 0s, 1s, and 2s, sort it in-place in a single pass (Dutch National Flag problem).
5. Find the majority element in an array (the element that appears more than n/2 times), ideally in O(n) time and O(1) space (Moore's Voting Algorithm).

## 🔴 Advance (3)

1. Given an array representing elevation/heights, calculate how much rainwater can be trapped between the bars (Trapping Rain Water problem).
2. Given an array, find the minimum number of jumps required to reach the last index, where each element represents the maximum jump length from that position.
3. Given an unsorted array, find three elements whose sum is closest to a given target value (3Sum Closest).

# Today's Assignment — Strings

## 🟢 Basic (7)

1. Count the total number of words in a sentence (without using `.split()` — manual approach).
2. Check whether a given string contains only digits.
3. Capitalize the first letter of every word in a sentence (Title Case) manually, without `.title()`.
4. Find the length of a string without using `len()`.
5. Replace all occurrences of a given character in a string with another character, without using `.replace()`.
6. Check if a string starts and ends with the same character.
7. Print all substrings of a given string.

## 🟡 Intermediate (5)

1. Given a string, check if it can be rearranged to form a palindrome.
2. Find the most frequently occurring character in a string.
3. Given a sentence, reverse the order of words (but keep each word's letters in the same order), e.g., `"I love Python"` → `"Python love I"`.
4. Implement a basic Caesar cipher: shift each letter in a string by `k` positions.
5. Given two strings, check if one string can be formed by rearranging the letters of the other (with different letter counts allowed as leftovers) — essentially, check if one string is a subsequence of another.

## 🔴 Advance (3)

1. Given a string, group all anagrams together from a list of words (e.g., `["eat","tea","tan","ate","nat","bat"]` → grouped anagram sets).
2. Implement the Rabin-Karp string matching algorithm (using rolling hash) to find all occurrences of a pattern in a text.
3. Given a string containing just the characters `(`, `)`, `{`, `}`, `[`, `]`, determine if the input string has valid (balanced) parentheses using a stack-based approach.

# Today's Assignment — Singly Linked List

## 🟢 Basic (7)

1. Implement a `Node` class (with `data` and `next`) and a `SinglyLinkedList` class with an `insert_at_end()` method and a `display()` method.
2. Write a method `insert_at_beginning()` to add a node at the head of a singly linked list.
3. Write a method to count the total number of nodes in a singly linked list.
4. Write a method `search(value)` that returns True/False if a value exists in the list.
5. Write a method to delete the first node (head) of a singly linked list.
6. Write a method to delete the last node of a singly linked list.
7. Write a method `insert_at_position(index, value)` to insert a node at a given index.

## 🟡 Intermediate (5)

1. Reverse a singly linked list iteratively (changing `next` pointers in a single pass).
2. Find the middle node of a singly linked list using the slow/fast pointer technique.
3. Detect if a singly linked list has a cycle using Floyd's Cycle Detection algorithm.
4. Remove all duplicate values from an unsorted singly linked list.
5. Find the N-th node from the end of a singly linked list in one traversal (without computing length first).

## 🔴 Advance (3)

1. Reverse a singly linked list recursively, and explain what happens on the call stack at each level.
2. Merge two sorted singly linked lists into one sorted singly linked list without using extra array storage.
3. Given a singly linked list with a cycle, find the exact node where the cycle begins (not just whether a cycle exists).

# Today's Assignment — Doubly Linked List

## 🟢 Basic (7)

1. Implement a `Node` class (with `data`, `next`, and `prev`) and a `DoublyLinkedList` class with `insert_at_end()` and `display()` (forward direction) methods.
2. Write a method `insert_at_beginning()` for a doubly linked list, making sure both `next` and `prev` pointers are updated correctly.
3. Write a method `display_reverse()` that traverses and prints a doubly linked list from tail to head using the `prev` pointers.
4. Write a method to count the total number of nodes in a doubly linked list.
5. Write a method `search(value)` to check whether a value exists in a doubly linked list.
6. Write a method to delete the first node (head) of a doubly linked list, correctly updating the new head's `prev` pointer.
7. Write a method to delete the last node (tail) of a doubly linked list, correctly updating the new tail's `next` pointer.

## 🟡 Intermediate (5)

1. Write a method `insert_at_position(index, value)` for a doubly linked list, correctly linking both `next` and `prev` pointers of neighboring nodes.
2. Write a method to delete a node by value from a doubly linked list (handle head, tail, and middle cases separately).
3. Reverse a doubly linked list in-place by swapping `next` and `prev` at every node (and updating the head pointer).
4. Explain why a doubly linked list is more efficient than a singly linked list for deletion when you already have a reference to the node to delete — implement `delete_node(node_reference)` in O(1).
5. Find the middle node of a doubly linked list using the slow/fast pointer technique.

## 🔴 Advance (3)

1. Implement a basic LRU (Least Recently Used) Cache using a doubly linked list + hash map, supporting `get(key)` and `put(key, value)` in O(1) time.
2. Convert a given singly linked list into a doubly linked list in-place (constructing correct `prev` pointers throughout).
3. Given a doubly linked list, sort it (e.g., using merge sort adapted for doubly linked lists) without converting it to an array/list first.

"""