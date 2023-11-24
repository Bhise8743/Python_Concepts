'''

@Author: Omkar Bhise

@Date: 2023-11-24 12:30:30

@Last Modified by: Author Name

@Last Modified time: 2023-11-24 6:30:00

@Title : to print the Inverted Pyramid star pattern

'''

n = int(input("Enter the  size "))

for i in range(n):
    for k in range(i):
        print(" ",end=" ")
    for j in range((n-i-1)*2+1):
        print("*",end=" ")
    print()