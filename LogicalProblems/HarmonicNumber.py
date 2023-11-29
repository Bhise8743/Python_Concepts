
'''

@Author: Omkar Bhise

@Date: 2023-11-24 11:00:30

@Last Modified by: Author Name

@Last Modified time: 2021-02-11 18:00:30

@Title : Harmonic number problem given inside the  logical problem list

'''
n = int(input("Enter the number "))

p = 0
i = 2
for i in range(1,n):
    q = 1 / i
    p = p + q
    # print(q)

print(n," th Harmonic number is ",p)