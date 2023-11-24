'''

@Author: Omkar Bhise

@Date: 2023-11-24 12:30:30

@Last Modified by: Author Name

@Last Modified time: 2023-11-24 12:30:30

@Title : to print the Pyramid star pattern

'''


n = int(input("Enter the number "))

for i in range(n):
    for k in range(n-i-1):
        print(" ",end=" ")
    for j in range(i*2+1):
        print("*",end=" ")
    print()