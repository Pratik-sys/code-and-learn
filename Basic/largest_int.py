#!/usr/bin/python3

# Given a list of numbers(unsorted), write a praogram to write a Python Program to find the largerst number in the given list.
# Write various methods with Justification
"""
Input : A = [14,2,8, 90]
Output: 90

Input : B = [56, 31, 40, 9]
Output: 56
"""

# Solution:

def largest(arr):
    '''
    This function returns the the largest numbr from the givn list 
    '''
    return max(arr)
  
arr =  [14,2,8, 90]
print(largest(arr))



