"""
# Today's Assignment — Stacks

## 🟢 Basic (7)

1. Implement a `Stack` class using a Python list with `push()`, `pop()`, `peek()`, and `is_empty()` methods.
2. Write a program to check if a string of parentheses `()` only (no other brackets) is balanced, using a stack.
3. Reverse a string using a stack (push each character, then pop them all).
4. Implement a stack using two queues.
5. Write a function that uses a stack to check whether a given string is a palindrome.
6. Convert a decimal number to its binary representation using a stack (push remainders, pop to build result).
7. Write a program to find the minimum element in a stack in O(1) time using an auxiliary stack.

## 🟡 Intermediate (5)

1. Evaluate a postfix expression (e.g., `"23*54*+"`) using a stack.
2. Convert an infix expression (e.g., `"a+b*c"`) to postfix notation using a stack (Shunting Yard style).
3. Given an array, find the next greater element for every element using a stack (O(n) approach).
4. Implement a function to sort a stack using only one additional stack (no arrays).
5. Given a string containing digits and brackets like `"3[a2[c]]"`, decode it into `"accaccacc"`-style expanded strings using a stack.

## 🔴 Advance (3)

1. Given a histogram represented as an array of bar heights, find the area of the largest rectangle that can be formed (Largest Rectangle in Histogram).
2. Design a stack that supports `push`, `pop`, `top`, and retrieving the minimum element, all in O(1) time (Min Stack).
3. Given an array of daily temperatures, find how many days you'd have to wait for a warmer temperature for each day, using a monotonic stack.

# Today's Assignment — Queues

## 🟢 Basic (7)

1. Implement a `Queue` class using a Python list with `enqueue()`, `dequeue()`, `front()`, and `is_empty()` methods.
2. Implement a queue using two stacks.
3. Write a program to reverse the first `k` elements of a queue, keeping the rest in the same order.
4. Implement a Circular Queue class with a fixed size, correctly handling the wrap-around condition.
5. Write a function to check if a queue is a palindrome sequence (without converting it fully to a list first).
6. Implement a Deque (double-ended queue) using Python's `collections.deque`, demonstrating insertion/removal from both ends.
7. Given a queue of integers, interleave the first half with the second half (e.g., `1,2,3,4,5,6` → `1,4,2,5,3,6`).

## 🟡 Intermediate (5)

1. Implement a `generate_binary_numbers(n)` function that uses a queue to generate binary representations of numbers from 1 to n.
2. Given a stream of characters, design a data structure using a queue that returns the first non-repeating character at any point in the stream.
3. Simulate a round-robin CPU scheduling algorithm using a queue, given a list of processes and their burst times.
4. Implement a Sliding Window Maximum using a deque — given an array and window size `k`, find the maximum in every window.
5. Design a queue that also supports retrieving the maximum element in O(1) time.

## 🔴 Advance (3)

1. Given a matrix of 0s and 1s (0 = obstacle), find the shortest path from the top-left to the bottom-right cell using BFS with a queue.
2. Implement a task scheduler that, given a list of tasks and a cooldown period `n`, finds the minimum number of intervals needed to complete all tasks (using a queue/heap combination).
3. Design a data structure `MovingAverage` that calculates the moving average of the last `k` values in a stream, using a queue internally.

# Today's Assignment — Recursion

## 🟢 Basic (7)

1. Write a recursive function to calculate the factorial of a number.
2. Write a recursive function to calculate the sum of digits of a number.
3. Write a recursive function to check whether a string is a palindrome.
4. Write a recursive function to compute the nth Fibonacci number.
5. Write a recursive function to reverse a string.
6. Write a recursive function to find the maximum element in an array.
7. Write a recursive function to calculate `x` raised to the power `n`.

## 🟡 Intermediate (5)

1. Write a recursive function to generate all subsets (the power set) of a given array.
2. Write a recursive function to generate all permutations of a given string.
3. Solve the Tower of Hanoi problem recursively for `n` disks, printing each move.
4. Write a recursive function to compute the Greatest Common Divisor (GCD) of two numbers (Euclidean algorithm).
5. Write a recursive function that solves a maze (2D grid) by finding if a path exists from start to end, exploring in four directions.

## 🔴 Advance (3)

1. Solve the N-Queens problem using recursion and backtracking — print all valid board configurations for a given `n`.
2. Given a set of numbers, find all unique combinations that sum up to a given target (Combination Sum), using recursion with backtracking.
3. Implement a recursive Sudoku solver that fills a partially completed 9x9 board following Sudoku rules.

# Today's Assignment — Sorting Algorithms

## 🟢 Basic (7)

1. Implement Bubble Sort and count the number of swaps it performs on a given array.
2. Implement Selection Sort on an array of integers.
3. Implement Insertion Sort and explain why it's efficient for nearly-sorted arrays.
4. Given an array, sort it and then find the second largest and second smallest elements.
5. Write a program to sort an array of strings by their length.
6. Implement a function that checks whether a given array is sorted (ascending or descending).
7. Sort an array of 0s and 1s only, in a single pass, without using a built-in sort.

## 🟡 Intermediate (5)

1. Implement Merge Sort on an array and explain its time complexity for best, average, and worst cases.
2. Implement Quick Sort on an array, using the last element as pivot.
3. Implement Counting Sort for an array of integers within a known small range.
4. Given an array of intervals, sort and merge all overlapping intervals.
5. Implement Cycle Sort and use it to find the missing number in an array containing `1` to `n` with one missing.

## 🔴 Advance (3)

1. Implement Merge Sort to count the number of inversions in an array (pairs where `i < j` but `arr[i] > arr[j]`).
2. Given a very large array that doesn't fit in memory, describe and implement a simplified version of External Merge Sort.
3. Implement a randomized Quick Sort (random pivot selection) and compare its performance against the standard version on a nearly-sorted array.

# Today's Assignment — Searching & Hashing

## 🟢 Basic (7)

1. Implement Linear Search on an unsorted array.
2. Implement Binary Search (iterative) on a sorted array.
3. Implement Binary Search recursively on a sorted array.
4. Given an array, use a hash set to find if any two elements sum up to a given target (Two Sum).
5. Use a dictionary to count the frequency of each word in a sentence.
6. Given two arrays, find their intersection using a hash set.
7. Write a program to find the first non-repeating element in an array using a hash map.

## 🟡 Intermediate (5)

1. Given a sorted array that has been rotated, search for a target element in O(log n) time.
2. Find the floor and ceiling of a given number in a sorted array using binary search.
3. Given an array, find the longest consecutive sequence of numbers (e.g., `[100,4,200,1,3,2]` → `1,2,3,4`) using a hash set, in O(n) time.
4. Implement a simple HashMap class from scratch (with collision handling via chaining) supporting `put()`, `get()`, and `remove()`.
5. Given an array of integers, find all pairs with a given difference `k` using a hash set.

## 🔴 Advance (3)

1. Given a 2D matrix sorted row-wise and column-wise, search for a target element in O(m+n) time.
2. Design a data structure that supports `insert`, `remove`, and `getRandom` all in O(1) average time (Insert Delete GetRandom O(1)).
3. Given an array of integers, find the smallest positive integer missing from it, in O(n) time and O(1) extra space.

"""