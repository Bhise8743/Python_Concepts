"""

@Author: Omkar Bhise

@Date: 2023-12-20 11:30:00

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-12-20 02:30:00

@Title :  User Registration Problem

"""


class Node:
    def __init__(self, value):
        self.value = value
        self.link = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node_at_begining(self, value):
        """
        Description: This function used to add new node at the beginning of the list

        Parameter: self object as parameter. and Value from the user

        Return: None

        """
        if self.head is None:
            self.head = Node(value)
        else:
            temp = Node(value)
            temp.link = self.head
            self.head = temp

    def append_node(self, value):
        """
        Description: This function used to add node at the last of list .

        Parameter: self object as parameter. and value from the user

        Return: None

        """
        temp = Node(value)
        if self.head is None:
            self.head = temp
        else:
            curr = self.head
            while curr.link is not None:
                curr = curr.link
            curr.link = temp

    def add_node_at_pos(self, value, pos):
        """
        Description: This function used to add node at any position in the list .

        Parameter: self object as parameter.  value and pos from the user

        Return: None
        """
        temp = Node(value)
        curr = self.head
        pre = None

        while pos > 0 and curr is not None:
            pos -= 1
            pre = curr
            curr = curr.link
        pre.link = temp
        temp.link = curr

    def update_node_at_pos(self, value, pos):
        """
        Description: This function used to update node value in the list  .

        Parameter: self object as parameter. value  and pos from the user

        Return: None
        """
        curr = self.head
        while pos > 1 and curr.link is not None:
            curr = curr.link
            pos -= 1
        curr.value = value

    def remove_first_node(self):
        """
        Description: This function used to remove first node of list .

        Parameter: self object as parameter.

        Return: None
        """
        temp = self.head
        self.head = temp.link
        print(f"{temp.value} is deleted successfully")
        temp = None

    def remove_last_node_of_list(self):
        """
        Description: This function used to remove last node of list .

        Parameter: self object as parameter.

        Return: None
        """
        if self.head == None:
            print("List alrady Empty ")
        elif self.head.link == None:
            self.head = None
        else:
            sec_last = self.head  # 1 - 2 - 3
            while sec_last.link.link:
                sec_last = sec_last.link
            sec_last.link = None




    def remove_at_any_pos_node(self,pos):
        """
        Description: This function used to remove node at an position in list .

        Parameter: self object as parameter. and pos form the user

        Return: None
        """
        if self.head is None:
            print("List is empty ")
        if pos == 1:
            self.remove_first_node()
            return
        curr = self.head
        pre = None
        while curr.link and pos>1:
            pos -= 1
            pre = curr
            curr = curr.link
        temp = curr
        pre.link = curr.link
        temp = None

    def print_list(self):
        """
        Description: This function used to print the list value

        Parameter: self object as parameter.

        Return: None
        """
        if self.head is None:
            print("List is Empty ")
        else:
            curr = self.head
            while curr is not None:
                print(f"{curr.value} ", end="")
                curr = curr.link

    def search_element(self,ele):
        """
        Description: This function used to search value in list 2.

        Parameter: self object as parameter. ele from the user

        Return: None
        """
        curr = self.head
        while curr:
            if curr.value == ele:
                print(f"{ele} is present ")
                return
            curr = curr.link
        print("Element is Not present ")


if __name__ == '__main__':
    l = LinkedList()
    try:
        while True:
            user_inp = int(input("""
                        0. exit
                        1. add node at beginning 
                        2. add node at last or append node
                        3. print the list 
                        4. add node at any position 
                        5. update the value at position 
                        6. Remove first node from the list  
                        7. Remove last element in the list 
                        8. Remove node of any position 
                        9. Search node value present or not in a list
            """))
            match user_inp:
                case 1:
                    value = int(input("Enter the value "))
                    l.add_node_at_begining(value)
                case 2:
                    value = int(input("Enter the value "))
                    l.append_node(value)
                case 3:
                    l.print_list()
                case 4:
                    value = int(input("Enter the value "))
                    pos = int(input("Enter the position "))
                    l.add_node_at_pos(value, pos)
                case 5:
                    value = int(input("Enter the value "))
                    pos = int(input("Enter the position "))
                    l.update_node_at_pos(value, pos)
                case 6:
                    l.remove_first_node()
                case 7:
                    l.remove_last_node_of_list()
                case 8:
                    pos = int(input("Enter the position "))
                    l.remove_at_any_pos_node(pos)
                case 9:
                    ele = int(input("Enter the searching element"))
                    l.search_element(ele)
                case 0:

                    break
    except Exception as ex:
        print(ex)
