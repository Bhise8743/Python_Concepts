"""

@Author: Omkar Bhise

@Date: 2023-12-24 09:30:00

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-12-24 02:30:00

@Title :  Implementation Insertion sort

"""

"""
        96 24 35 15 47
        
        i = 1 , j =i-1 = 0 , key = 24
        24 99 35 15 47
        
        i= 2 j=1  key = 35
        24 35 99 15 47
        
        i= 3 j=2  key = 15
        24 35 15 99 47
        24 15 35 99 47
        15 24 35 99 47
        
        i = 4 j= 3 key = 47
        15 24 35 47 99          
"""


def insertion_sort(l):
    for i in range(1,len(l)):
        key = l[i]
        j = i-1
        while j>=0 and l[j]>key:
            l[j+1] = l[j]
            j -= 1
        l[j+1] = key

def soer(l):
    for i in range(1,len(l)):
        key = l[i]
        j = i-1
        while j>=0 and l[j]>key:
            l[j+1] = l[j]
            j -= 1
        l[j+1] = key


if __name__ == '__main__':
    l = []
    n = int(input("Enter the size of list "))
    print("Enter the list elements ")
    for i in range(n):
        l.append(int(input()))

    print(f"Before sorting the list is {l}")
    soer(l)
    # insertion_sort(l)
    print(f"After sorting the list is {l}")


