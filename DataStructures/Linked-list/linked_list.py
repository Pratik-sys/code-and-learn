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

    # prepend fuction inserts the new node at the begining of the linked list 
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node 

    # insert after function inserts the new node bweteen the head node and previous node.
    def insert_after(self, prev_node, data):
        if not prev_node:
            print("previous node doesn't exist")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node



l = Linked_list()
l.append("A")
l.append("B")
l.append("C")
l.append("D")
l.prepend("E")
l.insert_after(l.head.next, "F")
l.print_list()

