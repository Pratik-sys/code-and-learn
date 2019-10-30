# Write a function int fib(int n) that returns Fn. For example, if n = 0, then fib() should return 0. If n = 1, then it should return 1. For n > 1, it should return Fn-1 + Fn-2.


"""
Input: 100
Output : 218922995834555169026
"""
# Solution: Method 2 ( Use Dynamic Programming )

FibonacciArray = [0, 1]


def fibonacci(n):
    """
    This function returns the the fibonaaci number
    """
    if n < 0:
        print("we don't do that here")
    elif n <= len(FibonacciArray):
        return FibonacciArray[n - 1]
    else:
        NewFibonnaciArray = fibonacci(n - 1) + fibonacci(n - 2)
        FibonacciArray.append(NewFibonnaciArray)
        return NewFibonnaciArray


print(fibonacci(100))
