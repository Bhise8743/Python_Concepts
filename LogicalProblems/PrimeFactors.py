import math

n = int(input("Enter the number "))

def prime(n):
    for i in range(2,math.floor(math.sqrt(n)),1):
        if n % i == 0:
            return False
    return True

a = n
for i in range(2,n,1):
     if prime(i):
         while a%i == 0:
             a /= i
             print(i)
