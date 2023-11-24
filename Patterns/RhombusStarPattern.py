'''

@Author: Omkar Bhise

@Date: 2023-11-24 12:30:30

@Last Modified by: Author Name

@Last Modified time: 2023-11-24 12:30:30

@Title : to print the rhombus star pattern

'''

n = int(input("ENter the size "))

for i in range(n):
    for k in range(i):
        print(" ",end=" ")
    for j in range(n):
        print("*",end=" ")
    print()