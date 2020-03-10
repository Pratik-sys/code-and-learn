#!/usr/bin/python3

# Reverse the string using stack operation .

def reverse_string(inpt_str):
    """ The fucntion reverses the string using stack operation."""
    stack = []
    for i in range(len(inpt_str)):
        stack.append(inpt_str[i])
        # As append is inbuilt function for list, shows the similar result as push 
    string = ""
    for _ in range(len(inpt_str)):

        string+= stack.pop()
        # The emptry string getss added with the everty signe item poped
       
    return string

print(reverse_string("HELLO"))