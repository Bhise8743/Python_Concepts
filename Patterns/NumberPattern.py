'''

@Author: Omkar Bhise

@Date: 2023-11-24 12:30:30

@Last Modified by: Author Name

@Last Modified time: 2023-11-24 7:00:00

@Title : to print the Number pattern  star pattern

'''

n = int(input("Enter the number "))
p=1
for i in range(n):
    for j in range(i+1):
        print(p,end=" ")
        p = p+1
    print()
