"""

@Author: Omkar Bhise

@Date: 2023-12-24 01:00:30

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-12-24 03:30:00

@Title :  Write a python code to reverse python code

"""


# slice  --> piece of the code
# s[begin:end:step] --> it return the [begin to end-1 index ]
# if step value is positive it goes form left to right
# if step value is negative then it goes form the right to left
# step value can not zero if zero it give ERROR
# [::1]
# [::-1]  revers the string

# reversed --> parameter as a string and return a reversed object
def reversed_str(s):
    rev = reversed(s)
    print(type(rev))
    out = "".join(rev)
    print(out)


def reverse_str_mani(s):
    # i = 0
    j = len(s) - 1
    out = ""
    while j > 0:
        out = out + s[j]
        j -= 1
    print(out)


if __name__ == '__main__':
    ans = input("Enter the string ")
    # out = ans[::0]   #ValueError: slice step cannot be zero
    out = ans[::-1]
    print(out)
    reversed_str(ans)
    reverse_str_mani(ans)
