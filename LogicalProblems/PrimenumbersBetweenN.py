import math

def prime(n):
    for i in range(2,math.floor(math.sqrt(n))+1,1):
        if n%i == 0:
            return False
    return True

n = int(input("Enter the number "))

for i in range(2,n,1):
    if prime(i):
        print(i)


