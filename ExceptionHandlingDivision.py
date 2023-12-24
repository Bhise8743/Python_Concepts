"""

@Author: Omkar Bhise

@Date: 2023-11-24 12:30:30

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-11-30 9:00:00

@Title :  Basic of Exception Handling

"""
a = 10
b = 20

try:
    print("resource open ")
    print(a/b)
    k = int(input("Enter the number "))
    print(k)

except ZeroDivisionError as e:
    print("You can not divide number by zeros ", e)
except ValueError as e:
    print("Invalid Input")
except Exception as a:
    print("Something went wrong ")
else:
    print("Try Block Executed successfully ...")
finally:

    print("Resource closed ")  #it execute with or without try block