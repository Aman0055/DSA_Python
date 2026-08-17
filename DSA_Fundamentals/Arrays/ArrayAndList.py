"""
An array in Python is a data structure used to store multiple values of the same data type
 in a single variable. Unlike a list, which can hold different types of data,
   an array stores only homogeneous (same type) elements, making it more memory-efficient and
   suitable for numerical operations. Python provides arrays through the built-in array module,
   and for advanced mathematical and scientific computing, the NumPy library is commonly used.

Key Highlights
Stores multiple values in a single variable.
All elements must be of the same data type (homogeneous).
Indexed collection – indexing starts from 0.
Supports insertion, deletion, updating, and traversal of elements.
More memory-efficient than lists for storing large amounts of similar data.
Commonly used for mathematical calculations, data processing, and scientific computing.
Syntax
from array import array

arr = array('i', [10, 20, 30, 40, 50])
'i' represents the integer data type.
"""

from array import *

a1 = array('i', [23,16,27,47,89])
print(type(a1))

print(a1)

for i in a1:
    print(i)

print(len(a1))

for x in range(3):
    print(a1[x], end=' ')

i = 0
while (i<(len(a1))):
    print(a1[i])
    i += 1

a1.append(20)
print(a1)

# check wheather it is present how many times
print(a1.count(20))

print(a1.count(56))

# check index
print(a1.index(20))

#pop() --> delete

print(a1.pop())

print(a1.pop(0))
print("After deletion", a1)


""""
Array Methods :

append()  , count() , fromlist() , extend() , insert(), index() , pop(), reverse() ,
remove()  , tolist()   
"""

print("*"*30)
print("\tList Basics :--------------------->>")
print("*"*30)

"""
Lists : 

List is a class 
List is mutable 
List is indexed 
List is an iterable 
List can grow Dynamic array 
List can contain different type of element 


array : 
{
collection of same datatype
fixed size ,
indexed
}

Dynamic array :
{
collection of same type elements
resizable 
indexed
}

Methods of list : ---->>>>

append() , clear(), count() , indexed(), insert() , pop() , remove() , sort() ,reverse(),extend()

Builtin Methods :
len()
sum()
max()
min()
sorted()


List and Array both are grewable 
List can contain hetrogeneous data 
Array can contain homogeneous data 

Note :-->>  If you want to perform a mathematical calculations then you should use numpy array,
            by importing Numpy package , 

            Otherwise use list as it as work in a similar way and more flexible to work with.
"""