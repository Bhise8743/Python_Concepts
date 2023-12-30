"""

@Author: Omkar Bhise

@Date: 2023-12-30 10:30:00

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-12-22 11:00:00

@Title :  sum of list ele and split the sum print the new list

"""


"""
Given two arrays of positive integers, add their elements into a new array. The solution should add both arrays,
 one by one starting from the 0'th index, and split the sum into individual digits if it is a 2–digit number.

Input : [23, 5, 2, 7, 87], [4, 67, 2, 8]
Output: [2, 7, 7, 2, 4, 1, 5, 8, 7]

Input : [], [4, 67, 2, 8]
Output: [4, 6, 7, 2, 8]

"""


def demo(p, l):
    """
        Description:
            split the sum and append in the ans list in reverse order
        Parameter:
             p : sum value
             l : None
    """
    ll = []
    if p < 10:
        l.append(p)
    else:
        while p > 10:
            t = p % 10
            ll.append(t)
            p //= 10
        ll.append(p)

    ll = ll[::-1]
    for i in ll:
        l.append(i)


if __name__ == '__main__':
    l1 = [23, 5, 2, 7, 87]
    l2 = [4, 67, 2, 8]

    # l1 = []
    # l2 = [4, 67, 2, 8]

    l = []

    i = 0
    j = 0
    while i < len(l1) and j < len(l2):
        p = l1[i] + l2[j]
        i += 1
        j += 1
        demo(p, l)

    while i < len(l1):
        demo(l1[i], l)
        i += 1

    while j < len(l2):
        demo(l2[j], l)
        j += 1

    print(f"Ans : {l}")
