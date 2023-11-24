'''

@Author: Omkar Bhise

@Date: 2023-11-24 12:30:30

@Last Modified by: Author Name

@Last Modified time: 2023-11-24 7:00:00

@Title : to print the Numeric pattern star pattern

'''

n = int(input("Enter the size "))

for i in range(n):
    for j in range(1,n-i+1,1):
        print(j,end=" ")
    print()