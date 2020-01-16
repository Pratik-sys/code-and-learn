# Write a program to find possible Words using given characters.
###
# No repeated character allowed
###

"""
Input : word_dict = ["go","bat","me","eat","goal","boy", "run"]
        arr = ['e','o','b', 'a','m','g', 'l']
Output : go, me, goal. 
"""
from collections import Counter


def possible_words(word_dict, arr):
    new_list = []
    for value in word_dict:
        dict = Counter(value)
        flag = 1
        for key in dict.keys():
            if key not in arr:
                flag = 0
            # this check below is essential
            if arr.count(key) != dict[key]:
                flag = 0
        if flag == 1:
            new_list.append(value)
    return new_list


print(
    possible_words(
        word_dict=["goo", "bat", "me", "eat", "goal", "boy", "run"],
        arr=["e", "o", "b", "a", "m", "g", "l"],
    )
)

