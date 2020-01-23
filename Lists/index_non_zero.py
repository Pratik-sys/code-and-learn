#!/usr/bin/python3

# Index of Non-Zero elements in a list
# Write a program to find positions of all the integers other than 0.

"""
[6, 7, 0, 1, 0, 2, 0, 12] --->  [0, 1, 3, 5, 7]
"""

def positions(x):
    a = []
    for i,v in enumerate(x):
        if v !=0:
            a.append(i)
    return a

print(positions([6, 7, 0, 1, 0, 2, 0, 12]))
