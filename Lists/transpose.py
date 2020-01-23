#!/usr/bin/python3
    
# Given a 2D array A, your task is to convert all rows to columns and columns to rows.


"""
Input:
[
    [13 4 8 14 1],
    [9 6 3 7 21],       
    [5 12 17 9 3]
]

Output
    |
    v
 [
    [13 9 5],
    [4 6 12],
    [8 3 17],
    [14 7 9],
    [1 21 3]
 ]
"""


def transpose(x):
    res = [[x[j][i] for j in range(len(x))] for i in range(len(x[0]))]
    for r in res:
        print(r)

print(transpose([[13, 4, 8, 14, 1], [9, 6, 3, 7, 21], [5, 12, 17, 9, 3]]))

