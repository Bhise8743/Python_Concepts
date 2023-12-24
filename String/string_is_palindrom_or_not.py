"""

@Author: Omkar Bhise

@Date: 2023-12-22 01:30:00

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-12-22 02:30:00

@Title :  String is palindrome or not

"""


def palindrome(s):
    mid = (len(s) - 1) // 2
    i = 0
    j = len(s) - 1
    while i <= j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


def symmetry(s):
    n = len(s)
    flag = 0
    if n % 2:
        mid = n // 2 + 1
    else:
        mid = n // 2
    i = 0
    j = mid

    while i < mid and j < n:
        if s[i] == s[j]:
            i += 1
            j += 1
        else:
            flag = 1
            break
    if flag == 0:
        print("The entered String is Symmetrical ")
    else:
        print("The entered string is not Symmetrical ")


if __name__ == '__main__':

    s = "nitin"
    if palindrome(s):
        print("String is palindrome")
    else:
        print("String is not palindrome ")

    symmetry(s)
