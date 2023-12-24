"""

@Author: Omkar Bhise

@Date: 2023-12-22 11:30:00

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-12-22 02:30:00

@Title :  Implementation of Queue using Linked List

"""


class Node:
    def __init__(self, value):
        self.value = value
        self.link = None


class Queue:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None


    def enqueue(self, value):
        temp = Node(value)
        if self.is_empty():
            self.head = temp
        else:
            curr = self.head
            while curr.link:
                curr = curr.link
            curr.link = temp
    def length_of_queue(self):
        if self.is_empty():
            print("Queue is empty ")
            return 0
        curr = self.head
        length = 0
        while curr:
            length += 1
            curr = curr.link
        return length

    def dequeue(self):
        if self.is_empty():
            print("Queue is already empty ")
            return
        temp = self.head
        self.head = temp.link
        temp = None

    def print_queue(self):
        if self.head is None:
            print("Queue is Empty ")
        curr = self.head
        while curr:
            print(f"{curr.value}  ",end="")
            curr = curr.link
        print()



if __name__ == '__main__':
    q = Queue()

    q.print_queue()
    q.dequeue()
    q.print_queue()

    try:
        while True:
            user_inp = int(input("""
                                   0. exit
                                   1. Enqueue
                                   2. Dequeue
                                   3. Print queue
                                   4. print length of queue  
                                   """))
            match user_inp:
                case 0:
                    break
                case 1:
                    value = int(input("Enter the value "))
                    q.enqueue(value)
                case 2:
                    q.dequeue()
                case 3:
                    q.print_queue()
                case 4:
                    print(f"Length of queue is {q.length_of_queue()}")
    except Exception as ex:
        print(ex)