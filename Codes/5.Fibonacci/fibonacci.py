# Write a function int fib(int n) that returns Fn. For example, if n = 0, then fib() should return 0. If n = 1, then it should return 1. For n > 1, it should return Fn-1 + Fn-2.


"""
Input: 9
Output : 34
"""
def fib(n):
    '''
    This function returns the the fibonaaci series
    '''
    if n < 0 :
        print("we don't do that here")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(9))
