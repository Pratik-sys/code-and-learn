#!/usr/bin/python3

# Question
# Define a function which can print a dictionary where the keys are numbers between 2 and 20 (both included) and the values are square of keys. Bonus for writing another function which only print values. Hint: items()

'''
Expected Output: {2:4,3:9....20:400}
'''
def square_print():
    d = {}
    for i in range(1,21):
        d[i] =  i**2
    return list(d.items())


print(square_print())





