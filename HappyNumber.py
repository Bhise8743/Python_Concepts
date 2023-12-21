
# d = {"one":"two","three":"four"}

# ans = dict{k,v for k,v in d




def squrt(n):
    return n*n


def demo(n):
    ans = 0
    while n > 0:
        t = n % 10
        ans += squrt(t)
        n //= 10
    print(ans)
    return ans


if __name__ == '__main__':
    n = int(input("Enter the number "))

    while n>= 10:
        n = demo(n)

    if n == 1:
        print("Happy number ")
    else:
        print("Not happy number ")

