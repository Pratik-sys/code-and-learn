<<<<<<< HEAD
# Given a list of numbers, write a python program to print all the even numbers in a given list.
'''
Input : A = [1,2,3,4,5,6,7,8]
Output : [2,4,6,8]
'''

# Solution:

def even_num(inp_list):
    new_list = list(inp_list)
    list_of_even = ([i]/2  for i in new_list)

even_num(input('enter the lsit:'))

=======
#!/usr/bin/python3
# Given a list of numbers, write a python program to print all the even numbers in a given list.
"""
Input : A = [1,2,3,4,5,6,7,8]
Output : [2,4,6,8]
"""


def even_num(inp_list):
    """
    This function returns the even numbers from the given list 
    """
    even_list = list(inp_list)
    for num in even_list:
        if int(num) % 2 == 0:
            print(num, end=" ")


even_num([20,34,55,67])
>>>>>>> c6344b086016115104904a06a4c9fc862c08b161

