#!/usr/bin/python3

def binary_search_recursive(a, x, start=0, end=None):
    """ Efficient program for searching the element in an array 
        with recursive way with O(logn) time complexity"""
    if end is None:
        end = len(a) - 1
    if start > end: # this the base conditon, at some we need to stop the recursion.
        return -1

    mid = (start + end) // 2
    if x == a[mid]:
        return mid
    elif x < a[mid]:
        return binary_search_recursive(a, x, start, mid-1)
    else:
       return binary_search_recursive(a, x, mid+1, end)

a = [ 2, 3, 4, 10, 40 ] 
x = int(input("Enter element:"))
result = binary_search_recursive(a,x)
if result != -1:
    print(f'element {x} is present at index {result}')
else:
    print(f'element {x} does not exist in an array')

