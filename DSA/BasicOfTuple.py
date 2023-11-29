"""

@Author: Omkar Bhise

@Date: 2023-11-24 12:30:30

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-11-27 7:00:00

@Title :  Basic of Tuple

"""
# Tuple are used to store multiple items in a single variable

# tuple is faster than list

# A tuple is a collection which is ordered and Unchangeable

t = ("p", "r", "o", "g", "r", "a", "m", 5)
print(t[2], "  ", t[3])   #accsessing using index
# Negative indexing
print(t[-2])
print(t[-1])

# sliding
print(t[1:5])       #excluding
print(t[-1])

print("length of tuple is ", len(t))
print(t)

# tuple constructor
tup = tuple(("apple", "banana", "cherry", "orange"))
print(tup)