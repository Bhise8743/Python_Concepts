import math

n = int(input("Enter the number "))
flag = 0
for i in range(2,math.floor(math.sqrt(n)),1):
    if n%i ==0:
        print(n," Not prime number ")
        flag = 1
        break

if flag == 0:
    print(n," is prime number ")











