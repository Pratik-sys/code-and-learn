#!/usr/bin/python3
# Question: Build a string with the numbers from 0 to 100.
'''
Input : range (0,100)
Output : "0123456789101112..."
'''

# Solution:

def string(num1, num2):
    '''
    This functions returns the string with the numbers from 0 to 100
    '''
    print(''.join([str(i) for i in range(num1, num2)]))

string(0,101)