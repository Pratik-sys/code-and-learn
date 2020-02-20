def binary_search(a,x):
    """Efficient program for searching the element in an array 
       with ittrative way with O(logn) time complexity
    """
    start = 0 
    end = len(a)-1

    while start<= end:
        mid = (start+end)//2 
        if x == a[mid]:
            return mid
        elif x < a[mid]:
            end = mid-1
        else:
            start = mid+1
    return -1

a = [2, 3, 4, 10, 40]
x = int(input("Enter element:"))
result = binary_search(a,x)
if result != -1:
    print(f'element {x} is present at index {result}')
else:
    print(f'element {x} does not exist in an array')
