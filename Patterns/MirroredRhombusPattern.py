'''

@Author: Omkar Bhise

@Date: 2023-11-24 12:30:30

@Last Modified by: Author Name

@Last Modified time: 2023-11-24 12:30:30

@Title : to print the Mirrored Rhombus star pattern

'''

n = int(input("Enter the number "))

for i in range(n):
    for k in range(n-i,0,-1):
        print(" ",end=" ")
    for j in range(n):
        print("*",end=" ")
    print()