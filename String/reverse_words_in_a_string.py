"""

@Author: Omkar Bhise

@Date: 2023-12-22 01:30:00

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-12-22 02:30:00

@Title :  String is palindrome or not

"""


def reverse_word(s):
    ans = s.split()[::-1]
    l = []
    for i in ans:
        l.append(i)
    ans = " ".join(l)
    print(ans)

def reverse(s):
    ans = list(s.split())
    # print(ans)
    ans.reverse()
    l = []
    for i in ans:
        l.append(i)
    print(" ".join(l))

def revesered_w(s):
    word = s.split(" ")
    rev = " ".join(reversed(word))
    print(rev)


if __name__ == '__main__':
    ans = input("Enter the string ")
    reverse_word(ans)
    reverse(ans)
    reverse_word(ans)
