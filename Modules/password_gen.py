#!/usr/bin/python3

# Write a password generator in Python.
# Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password.

"""
No test cases. 
This question is left open-ended as it may vary various implemention.
Using two or more different modules is allowed. 
"""
import random


def generate_password(digits, low_case, up_case, symbol):
    # combine the characters from the arrya that has been passed.
    combine_cahr = digits + low_case + up_case + symbol

    # randomly select atleast one char from each  array.
    rand_digit = random.choice(digits)
    rand_upper_char = random.choice(low_case)
    rand_lower_char = random.choice(up_case)
    rand_symbol = random.choice(symbol)
    # combine the each character driven from above
    temp_pass = rand_digit + rand_upper_char + rand_lower_char + rand_symbol

    password = temp_pass + random.choice(combine_cahr)

    return (f'"{password}" is the random generated password') 


print(
    generate_password(
        ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
        [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
        ],
        [
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "M",
            "N",
            "O",
            "p",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z",
        ],
        ["@", "#", "$", "%", "=", ":", "?", ".", "/", "|", "~", ">", "*", "(", ")"],
    )
)

import secrets
import string
'''
The secrets module is used for generating random numbers for managing important data such as passwords, account authentication, security tokens, and related secrets, that are cryptographically strong. 
'''
def gen_password():
    alphabets = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password =  ''.join (secrets.choice(alphabets) for i in range(10)) 
    return password 

print(f'"{gen_password()}" is the random generated password')