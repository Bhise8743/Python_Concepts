"""

@Author: Omkar Bhise

@Date: 2023-11-27 12:30:30

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-11-28 12:30:00

@Title : Write a Python function that takes two lists and returns
True if they have at least one common member.

"""

def commn_Ele(l1,l2):
    res = False

    for i in l1:
        for j in l2:
            if i == j:
                res = True
                return res
    return res

print("two list is common  element or not ")
print(commn_Ele([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))