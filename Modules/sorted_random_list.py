# Get a sorted list of random integers with unique elements
# Given lower and upper limits, generate a sorted list of random numbers with unique elements, starting from start to end.

"""
Input: num:10, start:100, end:200
Output: [102, 118, 124, 131, 140, 148, 161, 166, 176, 180]

Input: num:5, start:1, end:100
Output: [37, 49, 64, 84, 95]
"""
import random
def sorted_random(num, start, end):
    '''
    To-do: Change a default value to the desirable value
    start < end, always
    '''
   
    return sorted(random.randint(start, end) for i in range(num))
    
print(sorted_random(10, 1, 200))