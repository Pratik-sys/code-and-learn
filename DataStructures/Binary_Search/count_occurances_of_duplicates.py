#!/usr/bin/python3

# Given a sorted array of n elements, possibly with duplicates, find the number of occurrences of the target element.

def count_occ(a,x,serchfirst):
    """ gives the count of occurance of element in the array """
    start = 0 
    end = len(a)-1
    result = - 1
    while start <= end:
        mid = (start+end)//2

        if x == a[mid]:
            result = mid
            if serchfirst:
                end = end - 1
            else:
                start = mid + 1
        elif x < a[mid]:
            end = mid -1
        else:
            start = mid+1
    return result

a = [1,1,3,3,5,5,5,5,5,9,9,11]
x = 5
first = count_occ(a,x,True)

if first == -1:
    print(f'count  of {x} is 0')
else:
    last = count_occ(a,x,False)
    print(f'count of {x} is {last-first+1}')