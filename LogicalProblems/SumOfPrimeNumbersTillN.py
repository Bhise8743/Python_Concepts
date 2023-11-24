import math

n = int(input("Enter the number "))

def prime(n):
    for i in range (2,math.floor(math.sqrt(n))+1,1):
        if n%i == 0:
            return False
    return True

ans = 0
for i in range(2,n,1):
    if prime(i):
        ans += i
        print(i," ",ans)

print("Sum of prime Numbers Till is : ",ans)
