#!/usr/bin/python3

# Problem: Find the difference of two integers without using the + or - sign.


# Test Cases
"""
    None input -> TypeError
    7, 5 -> 2
    -5, -7 -> 2
    -5, 7 -> -12
    5, -7 -> 12
"""
def sub(x,y):
    """
    Gives the difference of the two integers without using the arithmetic operators(-)
    """
    while (y!=0):
        borrow = (~x) & y
        x = x^y
        y = borrow <<1
    return x
    
print(sub(7,5))