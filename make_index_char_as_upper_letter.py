l = ["omkar", "ravi", "divyansh", "rajesh", "amit"]
ll = []

l = sorted(l,key=len)
# ans = sorted(l,key=lambda )
print(l)


def con(s, i):
    ans = list(s)
    ass = ans[i].upper()
    ans[i] = ass
    anss = "".join(ans)
    ll.append(anss)


for i in range(len(l)):
    if len(l[i]) > i:
        con(l[i], i)
    else:
        ll.append(l[i])
print(ll)
