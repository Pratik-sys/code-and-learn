#!/usr/bin/python3

#Problem: Determine if a number is a power of two.
#referal : https://stackoverflow.com/questions/600293/how-to-check-if-a-number-is-a-power-of-2

#Test Cases
'''
    None -> TypeError
    0 -> False
    1 -> True
    2 -> True
    15 -> False
    16 -> True
'''
def is_number_power_of_two(x):
    """
    The function checks whether the give numbe is power of two
    """
    if x is None:
        raise TypeError('x cannot ne none')
    if x < 0:
        raise ValueError('number cannot br negative')
    while x != 0:
        return (x & (x-1) == 0) # what is (x & (x-1)? that's the binary representation.   


print(is_number_power_of_two(3))
print(is_number_power_of_two(2))