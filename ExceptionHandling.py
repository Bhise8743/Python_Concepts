"""

@Author: Omkar Bhise

@Date: 2023-11-24 12:30:30

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-11-29 1:00:00

@Title :  Basic of Exception Handling

"""

class NegativeNumberException(Exception):       #Cuatome exception 
    pass

while True:
    try:
        user_choise = int(input("Enter the number "))
        if user_choise < 0:
            raise NegativeNumberException("Entered Number is Negative ")
    except ValueError:
        print("ValueError Invalid Number ")
        break
    except NegativeNumberException as ex:
        print(ex)
        break
    except Exception as ex:
        print("Base Exception clss ",ex)
        break
    else:   #else execute if the try block execute
        print("Else block executed program run succsesfully ")
    finally:    #will execute after try or except block
        print("Finally Block executed with or without exceptions ")



