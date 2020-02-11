#!/usr/bin/python3

# Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order
# Avoid using python in-built step slicing, this should work in-place

# Test Cases
"""
    'Dark side of Moon' ---> 'Moon of side Dark'
    'Peace is Myth' ---> 'Myth is Peace'
"""


def reverse_words(strng):
    words = strng.split(" ")
    string = []
    for word in words:
        string.insert(0, word)
        " ".join(string)
    return " ".join(string)


print(reverse_words("Dark side of Moon"))


def reverse_order(x):
    return " ".join(x.split()[::-1])

print(reverse_order("Peace is Myth"))

