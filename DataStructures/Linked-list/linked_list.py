#!/usr/bin/python3

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linked_list:
    def __init__(self):
        self.head = None

    #This function returns the linked list.
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next   
    #Append function appends the element into  empty list 
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        # below code is for, if the liked list is not empty
        # and we have to point it to the next node.
        last_node  = self.head
        while last_node.next:
            last_node = last_node.next 
        last_node.next = new_node


l = Linked_list()
l.append("A")
l.append("B")
l.append("C")
l.apend("D")


l.print_list()