"""

@Author: Omkar Bhise

@Date: 2023-12-22 11:30:00

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-12-22 02:30:00

@Title :  Implementation of Stack using Linked List

"""


class Node:
    def __init__(self, value):
        self.value = value
        self.link = None


class Stack:
    def __init__(self):
        self.head = None
        self.rear = None

    def is_empty(self):
        return self.head is None

    def push(self, value):
        temp = Node(value)
        if self.is_empty():
            self.head = temp
            self.rear = self.head
        else:
            self.rear.link = temp
            self.rear = temp

    def pop(self):
        if self.is_empty():
            print("Stack is Empty")
            return
        curr = self.head
        while curr.link.link is not None:
            curr = curr.link
        curr.link = None
        self.rear = curr

    def peek_ele(self):
        return self.rear.value

    def print_list(self):
        if self.is_empty():
            print("List is empty ")
            return
        curr = self.head
        while curr:
            print(f"{curr.value}  ", end="")
            curr = curr.link
        print()


if __name__ == '__main__':
    s = Stack()

    while True:
        user_inp = int(input("""
                0. exit
                1. push
                2. pop
                3. print stack
                4. peek
        """))
        match user_inp:
            case 0:
                break
            case 1:
                value = int(input("Enter teh value "))
                s.push(value)
            case 2:
                s.pop()
            case 3:
                s.print_list()
            case 4:
                print(f"Peek element is {s.peek_ele()}")
