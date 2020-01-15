# Write a program to find first repeated word in a string in Python using(Dictionary).
# In case of no repition return 'No_reps_found'


"""
Input : "In the light, turing down the machine that broke"
Output : the
 
Input : "I will die trying"
Output : 'No_reps_found'

Input : "he had had he"
Output : he
"""

from collections import Counter
def firstRepeat(input):
    new = input.split(' ')
    dict1 = Counter(new)
    for value in dict1:
        if dict1[value]>1:
            return value
        else:
            return "NO_reps_found"
print(firstRepeat("he had"))


