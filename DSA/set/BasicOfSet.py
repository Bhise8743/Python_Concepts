"""

@Author: Omkar Bhise

@Date: 2023-11-24 12:30:30

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-11-29 10:00:00

@Title : Basic of the sets
"""

# set DS is a collection of unique elements

s = set()

s.add(12)
s.add("python")
s.update((45, 62, 78))

# it remove the element if exist other wise give the error
s.remove("python")

print(s)

# it remove the element if exist other wise nothing happens
s.discard("Python")

# it pop the random element in the list
s.add(85)
print(s)
print("It poped one element", s.pop())

print(s)

n = {14,45,85}

print("Union of two set ", s.union(n))
print()
print("intersection : ", s.intersection(n))
print()
print(s)
print(n)
# print the only differnt element of the first set only
print("Diffrence ", s-n)
