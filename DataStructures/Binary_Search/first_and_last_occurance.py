# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
# Your algorithm's runtime complexity must be in the order of O(log n).
# If the target is not found in the array, return [-1, -1].

def occurance(a,x,serchfirst):
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
first = occurance(a,x,True)
last = occurance(a,x,False)

if first and last == -1:
    print(f'{x} occured 0 times')
else:
    print(f'Element {x}"s first occurane is {first} and last occurance is {last}')