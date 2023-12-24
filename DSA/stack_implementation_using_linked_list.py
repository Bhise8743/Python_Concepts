"""

@Author: Omkar Bhise

@Date: 2023-12-22 01:30:00

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-12-22 02:30:00

@Title :  Implementation of Stack using Double Linked List

"""

class Node:
    def __init__(self,value):
        self.value = value
        self.link = None
        self.prev = None

class Stack:
    def __init__(self):
        self.head = None
        self.peek = None
    def is_empty(self):
        return self.head is None

    def push(self,value):
        temp = Node(value)
        if self.is_empty():
            self.head = temp
            self.peek = self.head
            return
        self.peek.link = temp
        temp.prev = self.peek
        self.peek = temp

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return
        elif self.head.link is None:
            self.head = None
            self.peek = None
            return

        temp = self.peek
        self.peek = self.peek.prev
        self.peek.link = None
        temp = None

    def print_stack(self):
        if self.is_empty():
            print("Stack is Empty ")
            return
        curr = self.head
        while curr:
            print(f"{curr.value}  ",end="")
            curr = curr.link


if __name__ == '__main__':
    s = Stack()
    while True:
        user_inp = int(input("""
                    0. exit
                    1. push
                    2. pop
                    3. print stack
                    4. print peek                    
        """))
        match user_inp:
            case 0:
                break
            case 1:
                value = int(input("Enter the value "))
                s.push(value)
            case 2:
                pass
                s.pop()
            case 3:
                s.print_stack()
            case 4:
                print(f"Peek of the stack is {s.peek.value}")