#!/usr/bin/python3


# Consecutive zeros

# The goal of this challenge is to analyze a binary string consisting of only zeros and ones. Your code should find the biggest number of consecutive zeros in the string.
# Define a function named consecutive_zeros that takes a single parameter, which is the string of zeros and ones. Your function should return the number described above.
#  For example, given the string:


"""
"1001101000110"

The biggest number of consecutive zeros is 3. 
"""

def consecutive_zeros(n):
    """
    function named consecutive_zeros that takes a single parameter, which is the string of zeros and ones
    and finds the biggest number of consecutive zeros in the string.
    """
    return max(map(len, n.split('1')))

print(consecutive_zeros("1001101000110"))