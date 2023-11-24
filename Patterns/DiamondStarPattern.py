'''

@Author: Omkar Bhise

@Date: 2023-11-24 12:30:30

@Last Modified by: Author Name

@Last Modified time: 2023-11-24 7:00:00

@Title : to print the Diamond Inverted star pattern

'''

n = int(input("Enter the size "))

for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for k in range(i*2+1):
        print("*",end=" ")
    print()

for i in range(n-1):
    for j in range(i+1):
        print(" ",end=" ")
    for k in range((n-i-1)*2-1):
        print("*",end=" ")
    print()