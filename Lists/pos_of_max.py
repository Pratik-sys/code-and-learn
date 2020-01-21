# Find the positions of maximum element of list.
# Assume the list  can have multiple maximum elements and hence multiple maximum positions.
# Return the list with index of max element
# The catch is to do it one-liner

"""
    a = [3,9,1,5,8,9] ----> [1,5]
    a = [20,40,80,80,78,80] ----> [2,3,5]
   
"""


def pos_max(arr):
    """
    arr : list
    function returns a list of indices of max element
    """
    return[i for i, v in enumerate(arr) if v == max(arr)]

print('Ouput for the first test case:', pos_max([3,9,1,5,8,9]))

print('Ouput for the second test case:', pos_max([20,40,80,80,78,80] ))