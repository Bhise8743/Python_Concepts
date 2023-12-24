"""

@Author: Omkar Bhise

@Date: 2023-12-24 09:30:00

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-12-24 02:30:00

@Title :  Implementation Selection Sort

"""
"""
        99 66 12 35 47 12
        i = 0 , min_ind = 2
        12 66 99 35 47 12
        i = 1 , min_ind = 5
        12 12 99 35 47 66
        i = 2 ,min_ind = 3
        12 12 35 99 47 66
        i = 3 ,min_ind =4
        12 12 35 47 99 66
        i = 4 , min_ind = 5
        12 12 35 47 66 99
        
        i = 5 j = 6  condition false 
"""


def selection_sort(l):
    for i in range(len(l)):
        min_ind = i
        for j in range(i + 1, len(l)):
            if l[j] < l[min_ind]:
                min_ind = j
        temp = l[i]
        l[i] = l[min_ind]
        l[min_ind] = temp


if __name__ == '__main__':
    l = []
    n = int(input("Enter the list size "))
    print("Enter the list elements ")
    for i in range(n):
        t = int(input())
        l.append(t)
    print(f"Before sorting {l}")
    selection_sort(l)
    print(f"After sorting {l}")
