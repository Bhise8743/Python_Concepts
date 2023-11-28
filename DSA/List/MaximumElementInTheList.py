"""

@Author: Omkar Bhise

@Date: 2023-11-24 12:30:30

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-11-26 7:00:00

@Title : find largest element in the list
         find the smallest element in the list

"""

a = []
n = int(input("Enter the size of the list "))
print("Enter the list elements ")
for i in range(n):
    p = int(input())
    a.append(p)

me = 0
se = 1000
for i in range(len(a)):
    if a[i]>me:
        me = a[i]
    if a[i]<se:
        se = a[i]
print("Maximum element in the list is : ", me)
print("Smallest element in the list is : ", se)