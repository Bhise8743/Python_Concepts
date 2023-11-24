'''

@Author: Omkar Bhise

@Date: 2023-11-24 12:30:30

@Last Modified by: Author Name

@Last Modified time: 2023-11-24 12:30:30

@Title : to print the Triangle star pattern

'''

n = int(input("Enter the size "))

for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()