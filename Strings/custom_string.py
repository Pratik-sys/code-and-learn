# Given a string 'S' , u need to tell whether it is 'customs string or not'.
# A string is called 'customs String' , if distance between adjacent character is 1.

# Consider that the alphabets are arranged in cyclic manner from 'a' to 'z'. distance between any character 'x' and 'y' will be defined as minimum number of steps it takes 'x' to reach 'y'. Here, character 'x' can  start moving clockwise or anti-clockwise in order to reach at position where character 'y' is placed.

# Print 'YES' if it is customs string else print 'NO', for each test case.

"""
aba ---> YES
zza ---> NO
bcd ---> YES
"""

def custom_string(strng):
    lst = list(strng)
    for i in range(len(lst) - 1):
        if abs(ord(lst[i]) - ord(lst[i+1])) == 1:
          continue
        else:
            return False
    return True

print(custom_string("aba"))
print(custom_string("abaz"))
print(custom_string("abcdca"))
