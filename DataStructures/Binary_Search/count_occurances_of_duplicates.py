# Given a sorted array of n elements, possibly with duplicates, find the number of occurrences of the target element.

def first_occ(a,x):

    start = 0 
    end = len(a)-1
    result = - 1
    while start <= end:
        mid = (start+end)//2

        if x == a[mid]:
            result = mid
            end = mid - 1
        elif x < a[mid]:
            end = mid -1
        else:
            start = mid+1
    return result

a = [2,4,10,10,10,18,20]
x = 10
pac = first_occ(a,x)

if pac != -1:
    print(f'first occurance of {x} is at index {pac}')
else:
    print("Element not found")  