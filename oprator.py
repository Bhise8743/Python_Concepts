
"""

@Author: Omkar Bhise

@Date: 2023-11-24 12:30:30

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-11-26 7:00:00

@Title : to print the Operators In Pythons and there uses

"""
# Arithmetic Operator
# Assignment Operator
# Comparison Operator
# Logical Operator
# Identity Operator
# Membership Operator
# Bitwise Operator 
a = 10

b = 50
print("...........Arithmatic Operator ..........")
print("Addition ", a+b)
print("Subtraction : ", a-b)
print("Multiplication : ", a*b)
print("Division : ", a/b)
print("Flore Division its round the result : ", a // b)
print("Modulous : ", a % b)
print("Modulous 1 : ", b % a)

print("Assignment Operator ........")
print(a)
a += 1
print(a)


print("Comparison Oeprator ..........")
# == , != , > , < , >= , <=

print("a == b ",a == b)
print("a > b ",a > b)

print("Logical Operator ...........")

# and , or , not
print("a < 10 and b < 10 ",a < 10 and b < 10)

print("not(a < 10) ",not(a < 10))

print("Identity Operator ............")

x = ["apple","banana"]

y = ["apple","banana"]

z = x

print("x is y ",x is y)
# It will check the memory location
print("x is z ",x is z)
print("x == y", x == y)

print("x is not y ",x is not y)
print("x is not z ", x is not z)

print("Membership Operator ............")

print("pineapple not in x : ","pineapple" not in x)
print("Pineapple in x : ","pineapple" in x)
print("banana in x : ","banana" in x )

print("Bitwise Operator ...............")
# & | ^ ~ << >>
print("a | b : ",a | b)
print("a & b : ",a & b)
print(a," ~a : ",~a)

