# Problem: Given an int, repeatedly add its digits until the result is one digit.

"""
Basic Test Cases:
- None input -> TypeError
- negative input -> ValueError
- 9 -> 9
- 138 -> 3
- 65536 -> 7
"""

def add_int(num):
    if num is None:
        raise TypeError('num cannot be none')
    if num < 0: 
        raise ValueError('number cannot br negative')
    digits = []
    while num != 0:
        digits.append(num % 10)
        num //= 10

    digits_num = sum(digits)
    if digits_num >= 10:
        return add_int(digits_num)
    else:
        return digits_num
print(add_int(1234))
