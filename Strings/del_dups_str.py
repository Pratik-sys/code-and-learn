#!/usr/bin/python3

# Given a string S. Your task is to remove all duplicates characters from the string S
#
# Note:
# 1.) Order of characters in output string should be same as given in input string.
# 2.) String S contains only lowercase characters ['a'-'z'].

"""
programming  ---> progamin
disco ---> disco
ramayan ---> ramyn 
"""


def remove_dup_string(strng):
    lst = list(strng)
    new = []   
    for value in lst:
        if value not in new:
            new.append(value)
            new_str = ''. join([str(i) for i in new])
    return new_str



print(remove_dup_string("programming"))