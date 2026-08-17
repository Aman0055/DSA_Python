"""
# OOPs (Object-Oriented Programming) — Practice Questions

## 🟢 Basic (7)

1. Create a `Student` class with attributes `name`, `roll_no`, and `marks`. Add a method `display()` that prints all details.
2. Create a `Car` class with a constructor that sets `brand` and `model`, and a method `start()` that prints "Car started".
3. What is the difference between an instance variable and a class variable? Write a small class demonstrating both (e.g., a `Counter` class that tracks total objects created).
4. Create a `Rectangle` class with `length` and `breadth`. Add methods `area()` and `perimeter()`.
5. Explain the four pillars of OOP (Encapsulation, Abstraction, Inheritance, Polymorphism) with one real-life example each.
6. Create a `BankAccount` class with `balance` as a private attribute (`__balance`). Add `deposit()` and `withdraw()` methods, and explain why direct attribute access should be avoided.
7. Create a `Person` class and an `Employee` class that inherits from it. `Employee` should add a `salary` attribute on top of `Person`'s `name` and `age`.

## 🟡 Intermediate (5)

1. Implement method overriding: create a base class `Shape` with a method `area()` that returns 0, and derived classes `Circle` and `Square` that override `area()` correctly.
2. Demonstrate multiple inheritance with a `Flyable` class and `Swimmable` class, combined into a `Duck` class. Explain how Python resolves the Method Resolution Order (MRO).
3. Create an abstract class `Vehicle` using the `abc` module with an abstract method `fuel_type()`. Implement it in `PetrolCar` and `ElectricCar`.
4. Explain and demonstrate `@staticmethod` vs `@classmethod` vs instance methods using a `MathUtils` or `Employee` class example.
5. Implement operator overloading: create a `Vector` class where `+` adds two vectors and `__str__` gives a readable output like `Vector(3, 4)`.

## 🔴 Advance (3)

1. Design a mini "Library Management System" using OOP: classes for `Book`, `Member`, and `Library`, with proper encapsulation, composition (Library "has" Books/Members), and methods to issue/return books with validation.
2. Implement the Singleton design pattern in Python (ensure only one instance of a `DatabaseConnection` class can ever exist).
3. Build a small class hierarchy simulating a "Smart City Traffic Management System" (e.g., `Vehicle` → `Car`, `Bus`, `EmergencyVehicle`) using inheritance, polymorphism, and abstraction — where each vehicle type overrides a `priority_at_signal()` method differently.

# Exception Handling — Practice Questions

## 🟢 Basic (7)

1. Write a program that divides two numbers entered by the user and handles `ZeroDivisionError` gracefully.
2. Write a program that takes user input and converts it to an integer, handling `ValueError` if the input isn't a valid number.
3. Explain the difference between `try`, `except`, `else`, and `finally` with a simple example that uses all four.
4. Write a program that accesses a list element by index and handles `IndexError` if the index is out of range.
5. Write a program that opens a file that may not exist, and handles `FileNotFoundError` with a friendly message.
6. What is the difference between an "error" and an "exception" in Python? Give two examples of each.
7. Write a program with a dictionary lookup that handles `KeyError` when the key doesn't exist.

## 🟡 Intermediate (5)

1. Create a custom exception class `InsufficientBalanceError` and use it inside a `withdraw()` method of a `BankAccount` class.
2. Write a program that catches multiple exception types (`ValueError`, `TypeError`, `ZeroDivisionError`) in a single `try` block using separate `except` clauses, and explain why catching a bare `except:` is risky.
3. Demonstrate exception chaining — raise a new exception from within an `except` block using `raise NewError(...) from original_error`.
4. Write a function with nested `try-except` blocks (an inner block for file reading, an outer block for data processing) and explain how exceptions propagate.
5. Explain and demonstrate the use of `finally` for resource cleanup (e.g., closing a file or database connection) even when an exception occurs.

## 🔴 Advance (3)

1. Design a custom exception hierarchy for a mini banking system (e.g., a base `BankError`, with subclasses `InsufficientFundsError`, `InvalidAccountError`, `NegativeDepositError`), and write a `Bank` class that raises the appropriate ones.
2. Implement a retry mechanism using a decorator: write a `@retry(times=3)` decorator that retries a function if it raises a specific exception, before finally failing.
3. Write a context manager (using `__enter__`/`__exit__` or `contextlib`) that manages a resource (like a simulated DB connection) and suppresses/logs a specific exception type while still cleaning up properly.

# Arrays — Practice Questions

## 🟢 Basic (7)

1. Find the largest and smallest element in an array without using built-in `max()`/`min()` functions.
2. Reverse an array in-place without using slicing or a built-in reverse function.
3. Find the sum and average of all elements in an array.
4. Count the number of even and odd elements in an array.
5. Check if a given array is sorted in ascending order.
6. Find the second largest element in an array.
7. Given an array, move all zeroes to the end while keeping the order of non-zero elements.

## 🟡 Intermediate (5)

1. Find all pairs in an array whose sum equals a given target value (Two Sum problem).
2. Rotate an array to the right by `k` steps, in-place.
3. Find the missing number in an array containing `n` distinct numbers from `0` to `n`.
4. Find the maximum subarray sum (Kadane's Algorithm) for a given array of integers.
5. Given an array, find all the duplicate elements without using extra space (or with O(1) extra space where possible).

## 🔴 Advance (3)

1. Given an array, find the length of the longest consecutive sequence of elements (e.g., `[100, 4, 200, 1, 3, 2]` → longest sequence is `1,2,3,4` → answer `4`), in O(n) time.
2. Merge two sorted arrays into one sorted array in-place without using extra space (the first array has enough trailing empty slots to hold both).
3. Given an array of stock prices per day, find the maximum profit achievable with at most two transactions (buy/sell twice, can't hold more than one share at a time).

# Strings — Practice Questions

## 🟢 Basic (7)

1. Reverse a string without using slicing (`[::-1]`) or a built-in reverse function.
2. Check if a given string is a palindrome (ignoring case).
3. Count the number of vowels and consonants in a string.
4. Count the frequency of each character in a string and print it (e.g., using a dictionary).
5. Check if two strings are anagrams of each other.
6. Convert a string to uppercase/lowercase manually without using `.upper()`/`.lower()`.
7. Remove all whitespace from a string without using `.replace()` or `.strip()` directly (loop-based approach).

## 🟡 Intermediate (5)

1. Find the first non-repeating character in a string.
2. Check if a string contains all unique characters (no repeats), without using a set directly (try a manual approach too).
3. Given a string, find the longest substring without repeating characters.
4. Implement basic string compression (e.g., `"aaabbbccd"` → `"a3b3c2d1"`); if compressed string isn't shorter, return the original.
5. Check if one string is a rotation of another (e.g., `"waterbottle"` is a rotation of `"erbottlewat"`).

## 🔴 Advance (3)

1. Implement a basic pattern-matching function (find all starting indices where a substring `pat` occurs in a string `txt`) — try implementing it without using `.find()`/`.index()`, similar to the naive string-matching algorithm.
2. Given a string, find the longest palindromic substring.
3. Given two strings, find the minimum number of edit operations (insert, delete, replace) to convert one string into the other (Edit Distance / Levenshtein Distance).

# Linked List — Practice Questions

## 🟢 Basic (7)

1. Implement a singly linked list class with a `Node` class and methods to `insert_at_end()` and `display()`.
2. Write a method to insert a node at the beginning of a linked list.
3. Write a method to find the length (number of nodes) of a linked list.
4. Write a method to search for a given value in a linked list and return whether it exists.
5. Write a method to delete a node with a given value from a linked list.
6. Write a method to insert a node at a specific position (index) in a linked list.
7. Write a method to find the sum of all node values in a linked list of integers.

## 🟡 Intermediate (5)

1. Reverse a singly linked list (iteratively).
2. Find the middle element of a linked list in a single pass (slow/fast pointer approach).
3. Detect whether a linked list contains a cycle (Floyd's Cycle Detection / slow-fast pointer).
4. Remove duplicate values from an unsorted linked list.
5. Find the N-th node from the end of a linked list in a single traversal.

## 🔴 Advance (3)

1. Reverse a linked list recursively (not iteratively), and explain the recursion stack behavior.
2. Merge two sorted linked lists into a single sorted linked list.
3. Given a linked list with a cycle, find the starting node of the cycle (not just detect that a cycle exists).

"""