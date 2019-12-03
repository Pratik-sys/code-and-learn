#!/usr/bin/python3

# Write a function named capital_indexes. The function takes a single parameter, which is a string. Your function should return a list of all the indexes in the string that have capital letters.
'''
capital_indexes("HeLlO") :return [0, 2, 4].
'''

def capital_indexes(s):
    '''
    s : string
    return a: list
    '''
    return [i for i, c in enumerate(s) if c.isupper()]

print(capital_indexes("HeLlO"))