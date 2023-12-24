"""

@Author: Omkar Bhise

@Date: 2023-12-22 11:30:00

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-12-22 02:30:00

@Title :  Implementation of Queue using List

"""


class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.is_empty():
            print("Queue is already Empty ")
        self.queue.pop(0)

    def length_of_queue(self):
        return len(self.queue)

    def print_queue(self):
        print(self.queue)

if __name__ == '__main__':
    q = Queue()

    while True:
        user_inp = int(input("""
                0. exit
                1. Enqueue
                2. Dequeue
                3. print queue
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
                print(f"Length of Queue is {q.length_of_queue()}")