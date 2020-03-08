#!/usr/bin/python3

class Stack():
    """In stack, a new element is added at one end and an element is removed from that end only."""

    def __init__(self):
        self.item = []

    def push(self,item):
        self.item.append(item)

    def size(self):
        return len(self.item)

    def pop(self):
        return self.item.pop()

    def is_empty(self):
        return self.item == []

    def peek(self):
        if not self.is_empty():
            return self.item[-1]

    def get_stack(self):
        return self.item


new_stack = Stack()
new_stack.push(90)
new_stack.push(34)
new_stack.push(45)
new_stack.push(21)
new_stack.pop()
new_stack.push(80)

print(new_stack.size())
print(new_stack.get_stack())
print(new_stack.peek())
