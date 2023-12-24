"""

@Author: Omkar Bhise

@Date: 2023-11-04 10:30:30

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-11-04 9:00:00

@Title :  Basic of Exception Handling

"""


def exe():
    num1 = int(input("Enter the first number "))
    num2 = int(input("Enter the second number "))

    try:
        div = num1 / num2  # class : NameError  -->name 'num' is not defined
        print(f"Division is {div}")  # class : ZeroDivisionError  --> division by zero
        print(f"Division answer in the int formate {num1 // num2}")
    except Exception as p:
        print(p)
        print(p.__class__)
    except :
        print()

if __name__ == '__main__':
    exe()
