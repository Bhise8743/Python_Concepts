"""

@Author: Omkar Bhise

@Date: 2023-12-24 01:30:00

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-12-24 02:30:00

@Title :  Implementation Bubble sort

"""

"""
    81 23 77 25 14     Given list 
    
    23 81 77 25 14
    14 81 77 25 23
    
    14 77 81 25 23
    14 25 82 77 23
    14 23 82 77 25
    
    14 23 77 82 25
    14 23 25 82 77
    
    14 23 25 77 82
    
"""


def bubble_sort(l):
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[j] < l[i]:
                temp = l[i]
                l[i] = l[j]
                l[j] = temp


if __name__ == '__main__':
    l = []
    n = int(input("Enter the list size "))
    print("Enter the list elements ")
    for i in range(n):
        t = int(input())
        l.append(t)
    print(f"Unsorted list : {l}")
    bubble_sort(l)
    print(f"Sorted list is {l}")
