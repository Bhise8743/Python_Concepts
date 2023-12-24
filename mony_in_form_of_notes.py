#
#
d = {}
#
n = int(input("Enter the Amount : "))
#
# if n // 500 > 0:
#     ans = n // 500
#     n = n % 500
#     d.update({500:ans})
#
# if n // 200 > 0:
#     ans = n // 200
#     n = n % 200
#     d.update({200:ans})
# if n // 100 > 0:
#     ans = n // 100
#     n = n % 100
#     d.update({100:ans})
#
# if n // 50 > 0:
#     ans = n // 50
#     n = n % 50
#     d.update({50:ans})
# if n // 20 > 0:
#     ans = n // 20
#     n = n % 20
#     d.update({20:ans})
# if n // 10 > 0:
#     ans = n // 10
#     n = n % 10
#     d.update({10:ans})
# if n // 5 > 0:
#     ans = n // 5
#     n = n % 5
#     d.update({5:ans})
# if n // 2 > 0:
#     ans = n // 2
#     n = n % 2
#     d.update({2:ans})
# if n // 1 > 0:
#     ans = n // 1
#     n = n % 1
#     d.update({1:ans})
# print(d)

l = (500,200,100,50,20,10,5,2,1)
for i in l:
    if n // i> 0:
        ans = n // i
        n = n % i
        d.update({i: ans})
print(d)