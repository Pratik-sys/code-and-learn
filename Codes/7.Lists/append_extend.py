# Append: Adds its argument as a single element to the end of a list. The length of the list increases by one.


the_list = ["Helo", "for"]
the_list.append("worlds")
print(the_list)

# Output: ['Helo', 'for', 'worlds']

# NOTE: A list is an object. If you append another list onto a list, the first list will be a single object at the end of the list.

a_list = ["Trick", "or", "Treats"]
b_list = [6, 0, 4, 1]
a_list.append(b_list)
print(a_list)

# Output:['Trick', 'or', 'Treats', [6, 0, 4, 1]]


# extend(): Iterates over its argument and adding each element to the list and extending the list. The length of the list increases by number of elements in it’s argument.

a_list = ["Highway", "to"]
b_list = ["hell", "ya"]
a.extend(b_list)
print(a_list)

# Output:['Highway, 'to' ,'hell', 'ya']

# NOTE: A string is an iterable, so if you extend a list with a string, you’ll append each character as you iterate over the string.

a_list = ["To", "your", 78, 0, 4, 1]
my_list.extend("mondays")
print(my_list)

# Output: ['geeks', 'for', 6, 0, 4, 1, 'm', 'o', 'n', 'd', 'a', 'y', 's']

# Time Complexity:
# Append has constant time complexity i.e.,O(1).
# Extend has time complexity of O(k). Where k is the length of list which need to be added.

