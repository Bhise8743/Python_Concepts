"""

@Author: Omkar Bhise

@Date: 2023-12-24 01:00:30

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-12-24 03:30:00

@Title :  Write a python code to reverse content of every second word in a string python code
          Write a python code to print the even number character and odd numbers characters
"""


def reverse_second_word(s):
    l = s.split()
    i = 0
    l1 = []
    while i<len(l):
        if i%2 == 0:
            l1.append(l[i])
        else:
            l1.append(l[i][::-1])
        i += 1
    out = " ".join(l1)
    print(out)

def print_char_At_even_and_odd(s):
    i = 0
    print("Print at even number char : ",end=" ")
    while i < len(s):
        print(f"{s[i]}",end=" ")
        i += 2
    print("\nPrint at Odd Number char : ",end="")
    i = 1
    while i < len(s):
        print(f"{s[i]}",end=" ")
        i += 2


if __name__ == '__main__':
    inp = input("Enter the string ")
    # inp = "one two three four five six seven eight nine ten"
    reverse_second_word(inp)
    print_char_At_even_and_odd(inp)