#!/usr/bin/python3
# Question: How to convert a string to a number that consists of letters ASCII code. 

'''
Input = 'abcd'
Output = 979899100
'''

# Solution:

def ascii_to_int(inp_string):
  '''
  This functions returns the ascii value of the string, character by character
  '''
  list_of_char = list(inp_string)
  list_of_intger = [ord(i) for i in list_of_char]
  for i , v in enumerate(list_of_intger):
    print(v, end='')

ascii_to_int(input('Enter the the char:'))
