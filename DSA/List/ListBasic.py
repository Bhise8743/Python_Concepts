
"""

@Author: Omkar Bhise

@Date: 2023-11-27 12:30:30

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-11-26 7:00:00

@Title : List Basic

"""
l = []

for i in range(3):
    a = int(input("Enter number "))
    l.append(a)


print("It print the lisLL̥t length ",len(l))

l.append("Omkar Bhise")
print(l)
print(type(l))

# list() constructor to make a list
ll = list(("one","two","three","four"))
print(ll)
print("sort the list elements  ")
ll.sort()
# add new items
ll.append("five")
print(ll)
# insert the element at the given index , shifting element to the right
# list.insert(index, elem)
ll.insert(0,"zero")
print()
print("added zero string to the index 0 ",ll)
# add the elements in the list2 to the end of the list
# using + or += similar to the extend()
ll.extend(l)
print(ll)

# search element inside the list using index
# list.index(elem)
print("searching the index 2 elements ", ll.index("four"))

# list.remove(element)  remove the element from the list
print(ll)
print("removing five from the given string ")
ll.remove("five")
print(ll)

print(ll)
print("reverse the list ")
ll.reverse()
print(ll)

# remove element form the list at any index
# list.pop(index)
print("reversed list elements ")
ll.reverse()
print(ll)


