#!/usr/bin/python3

# Write a program that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

# Write at least two different functions to do this
# Test Cases
"""
    [1,2,3,4,3,4] ---> [1,2,3,4]
    [5,9,9,9,6] ----> [5,9,6]
"""


def del_dups_1(x):
    new = []
    for value in x:
        if value not in new:
            new.append(value)
    return new


print(del_dups_1([5, 9, 9, 9, 6]))


import collections


def del_dups_2(x):
    return list(collections.OrderedDict.fromkeys(x))


print(del_dups_2([1, 2, 3, 4, 3, 4]))

