"""

@Author: Omkar Bhise

@Date: 2023-11-27 12:30:30

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-11-28 12:00:00

@Title : List Basic

"""

l = []
sumOflsitEle = 0
mulOfListEle = 1
n = int(input("Enter the list size "))
print("Enter the list elements ")
for i in range(n):
    p = int(input())
    l.append(p)
    sumOflsitEle += l[i]
    mulOfListEle *= l[i]

print("sum of list eledment is ", sumOflsitEle)
print("Multiplication of the list element is ", mulOfListEle)


