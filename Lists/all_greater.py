# Write a program to verify that in the list all the values are greater than the given
# number k
# Wiring at-least one pythonic way/function is mandatory
"""
    a = [90,80, 70, 40, 20, 65], k = 30 ----> False
    a = [90,80, 70, 40, 20, 65], k = 10 ----> True
"""


def all_greater(arr, k):
    return all(i > k for i in arr)


print(all_greater([90, 80, 70, 40, 20, 65], k=30))

