"""

@Author: Omkar Bhise

@Date: 2023-12-22 01:30:00

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-12-22 02:30:00

@Title :  String is palindrome or not

"""


# write a python code to reverse the internal content of the word
def reverse_internal_content_of_string(s):
    l = s.split()
    print(l)
    l1 = []
    for i in l:
        l1.append(i[::-1])
    out = " ".join(l1)
    print(out)


def revrese_w(s):
    l = s.split()
    l1 = l[::-1]
    out = " ".join(l1)
    print(out)


if __name__ == '__main__':
    ans = input("Enter the string ")
    revrese_w(ans)
    reverse_internal_content_of_string(ans)
