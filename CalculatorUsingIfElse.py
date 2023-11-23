
a = int(input("Enter the first number"))
b = int(input("Enter the second number"))

print("1 for Addition")
print("2 for Substraction ")
print("3 for Multiplication")
print("4 for Division ")
print("5 for Modulous")
n = int(input("Enter your choice "))

if n == 1:
    print(a+b)
elif n == 2:
    print(a-b)
elif n == 3:
    print(a*b)
elif n == 4:
    print(a/b)
elif n == 5:
    print(a%b)
else:
    print("choice is wrong ...")