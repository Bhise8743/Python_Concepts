"""

@Author: Omkar Bhise

@Date: 2023-12-22 11:30:00

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-12-22 02:30:00

@Title :  Implementation of Stack using list

"""


class Stack:
    def __init__(self):
        self.stack = []

    def append(self, value):
        self.stack.append(value)

    def pop(self):
        if self.is_empty():
            print("stack is Empty ")
            return
        self.stack.pop()

    def print_stack(self):
        print(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        print(f"peak element is {self.stack[len(self.stack)-1]}")

if __name__ == '__main__':
    s = Stack()
    s.pop()
    s.append(12)
    s.append(47)
    s.append(87)
    s.append(17)
    s.print_stack()
    s.pop()
    s.peek()
    s.print_stack()

    try :
        while True:
            user_inp = int(input("""
                            0. exit
                            1. append
                            2. pop
                            3. Print stack 
                            4. print the peak elements
                                 """))
            match user_inp:
                case 0:
                    break
                case 1:
                    value = int(input("Enter the value "))
                    s.append(value)
                case 2:
                    s.pop()
                case 3:
                    s.print_stack()
                case 4:
                    s.peek()
    except Exception as ex:
        print(ex)
