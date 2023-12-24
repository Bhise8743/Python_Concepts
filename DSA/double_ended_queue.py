"""

@Author: Omkar Bhise

@Date: 2023-12-22 01:30:00

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-12-22 02:30:00

@Title :  Implementation of Double ended queue using Double Linked List

"""

class Node:
    def __init__(self,value):
        self.link = None
        self.prev = None
        self.value = value

class Dequeue:
    def __init__(self):
        self.head = None
        self.rear = None
    def is_empty(self):
        return self.head is None

    def enqueue(self,value):
        temp = Node(value)
        if self.is_empty():
            self.head = temp
            self.rear = self.head
            return
        self.rear.link = temp
        temp.prev = self.rear
        self.rear = temp

    def print_queue(self):
        if self.is_empty():
            print("Queue is empty ")
            return
        curr = self.head
        while curr:
            print(f"{curr.value} ",end="")
            curr= curr.link
        print()

    def remove_from_front(self):
        if self.is_empty():
            print("List is empty ")
            return
        elif self.head.link is None:
            self.head = None
            self.rear = None
            return
        temp = self.head
        self.head= temp.link
        self.head.prev = None
        temp = None

    def remove_from_last(self):
        if self.is_empty():
            print("List is empty ")
            return
        elif self.head.link is None:
            self.head = None
            self.rear = None
            return
        temp = self.rear.prev
        self.rear = None
        temp.link = None
        self.rear = temp
        temp = None


if __name__ == '__main__':
    d = Dequeue()

    while True:
        usre_inp = int(input("""
                    0. exit
                    1. enqueue
                    2. remove from front 
                    3. print queue
                    4. remove from the last
                    5. print the rear       
        """))
        match usre_inp:
            case 0:
                break
            case 1:
                value = int(input("Enter the value "))
                d.enqueue(value)
            case 2:
                d.remove_from_front()
            case 3:
                d.print_queue()
            case 4 :
                d.remove_from_last()