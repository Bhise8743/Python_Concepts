"""

@Author: Omkar Bhise

@Date: 2023-12-22 01:30:00

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-12-22 02:30:00

@Title :  Implementation of Double Linked List

"""


class Node:
    def __init__(self, value):
        self.value = value
        self.link = None
        self.prev = None


class DoubleLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        return self.head is None

    def add_node_at_beginning(self, value):
        temp = Node(value)
        if self.is_empty():
            self.head = temp
        else:
            temp.link = self.head
            self.head.prev = temp
            self.head = temp

    def add_node_at_last(self, value):
        temp = Node(value)
        if self.is_empty():
            self.head = temp
        else:
            curr = self.head
            while curr.link:
                curr = curr.link
            curr.link = temp
            temp.prev = curr

    def print_list(self):
        p = 0
        if self.is_empty():
            print("List is empty")
        else:
            curr = self.head
            while curr:
                p += 1
                print(f"{curr.value}  ", end="")
                curr = curr.link
            print()

    def add_node_at_any_pos(self, value, pos):
        if pos == 1:
            self.add_node_at_beginning(value)
            return
        temp = Node(value)

        curr = self.head
        pre = None
        while pos > 1 and curr.link is not None:
            pre = curr
            curr = curr.link
            pos -= 1

        pre.link = temp
        temp.prev = pre
        temp.link = curr
        curr.pre = temp

    def delete_first_node(self):
        if self.is_empty():
            print("List is already Empty ")
            return
        elif self.head.link is None:
            self.head = None
            return
        temp = self.head
        self.head = self.head.link
        self.head.prev = None
        temp = None

    def delete_last_node(self):
        if self.is_empty():
            print("List is already Empty ")
            return
        elif self.head.link is None:
            self.head = None
            return
        curr = self.head
        while curr.link.link is not None:
            curr = curr.link
        curr.link = None

    def length_of_list(self):
        p = 0
        curr = self.head
        while curr:
            p += 1
            curr = curr.link
        return p

    def delete_node_at_any_pos(self, pos):
        if self.is_empty():
            print("list is already empty ")
            return
        elif pos == 1:
            self.delete_first_node()
            return
        curr = self.head
        pre = None
        while pos > 1:
            if curr.link.link is None:
                self.delete_last_node()
                return
            pre = curr
            curr = curr.link
            pos -= 1

        temp = curr
        pre.link = curr.link
        curr.link.prev = pre
        temp = None


if __name__ == '__main__':
    l = DoubleLinkedList()
    while True:
        user_inp = int(input("""
                    0. exit
                    1. add at beginning 
                    2. add at last                    
                    3. print list
                    4. add at any position 
                    5. delete first node 
                    6. delete last node
                    7. delete any position node 
                    
        """))
        match user_inp:
            case 0:
                break
            case 1:
                value = int(input("Enter the value "))
                l.add_node_at_beginning(value)
            case 2:
                value = int(input("Enter teh value "))
                l.add_node_at_last(value)
            case 3:
                l.print_list()
            case 4:
                value = int(input("Enter the value "))
                pos = int(input("Enter the position "))
                l.add_node_at_any_pos(value, pos)
            case 5:
                l.delete_first_node()
            case 6:
                l.delete_last_node()
            case 7:
                pos = int(input("Enter the position "))
                l.delete_node_at_any_pos(pos)
