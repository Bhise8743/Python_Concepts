"""

@Author: Omkar Bhise

@Date: 2023-11-24 12:30:30

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-11-29 9:30:00

@Title : Basic Of Dictionary

"""
# dict stores the data in the form of key value pairs

# Empty Dict
d ={0:"Zero", 2:"Two"}

d[1] = "One"

# Key value is uniqe

print(d[2])     #if not persent it give the exeseption

print(d)

d.update(dsd='Three')
d.update({2:"ten"})
# print the keys only
print(d.keys())
# print the values only
print(d.values())
#print both the key and values
print(d.items())

print("Print the poped items", d.popitem())  #it return the poped items
print(d)

print(d)

print("pop the 0 key values", d.pop(0))
print(d)