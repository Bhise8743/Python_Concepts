
n = int(input("Enter the number "))

p = 0
i = 2
for i in range(1,n):
    q = 1 / i
    p = p + q
    # print(q)

print(n," th Harmonic number is ",p)