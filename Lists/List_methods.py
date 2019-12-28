#!/usr/bin/python3

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
a_list.extend(b_list)
print(a_list)

# Output:['Highway, 'to' ,'hell', 'ya']

# NOTE: A string is an iterable, so if you extend a list with a string, you’ll append each character as you iterate over the string.

a_list = ["To", "your", 78, 0, 4, 1]
a_list.extend("mondays")
print(a_list)

# Output: ['To', 'your', 78, 0, 4, 1, 'm', 'o', 'n', 'd', 'a', 'y', 's']

# Time Complexity:
# Append has constant time complexity i.e.,O(1).
# Extend has time complexity of O(k). Where k is the length of list which need to be added.

# Insert: Inserts an item at the defined index.

Fruit_basket = ["apple","grapes","oranges","mangoes"]
Fruit_basket.insert(3, "watermelon")  #Syntax: list.insert(<position, element)
print(Fruit_basket)

# Output: ['apple', 'grapes', 'oranges', 'watermelon', 'mangoes']


#Remove: Removes the item from the given list.

Fruit_basket = ["apple","grapes","oranges","watermelon","mangoes"]
Fruit_basket.remove("mangoes") #Syntax: list.remove(<element>)
print(Fruit_basket)

# Output: ['apple', 'grapes', 'oranges', 'watermelon']

# pop: Removes the element from the given index 

Fruit_basket = ["apple","grapes","oranges","watermelon","mangoes"]
Fruit_basket.pop(0) #Syntax: list.pop(<position>)
print(Fruit_basket)

# Output: ['grapes', 'oranges', 'watermelon', 'mangoes']

# clear: Removes all the elements from the list

Fruit_basket = ["apple","grapes","oranges","watermelon","mangoes"]
Fruit_basket.clear() #Syntax: list.clear()
print(Fruit_basket)

# Output: []

# Index:Returns the index of first occurrence.

Fruit_basket = ["apple","grapes","oranges","watermelon","mangoes"]
print(Fruit_basket.index("grapes")) #Syntax: list.index(<element>)

# Output: 1

# Count: Counts the number of occurance of the item in the list 
Fruit_basket = ["apple","grapes","oranges","watermelon","mangoes", "apple"]
print(Fruit_basket.count("apple")) #Syntax: list.count(<element>)

# Output: 2

# Sort and Reverse: Sort the given data structure (both tuple and list) in ascending order.

new_list = [2, 1, 3, 5, 3, 8]
new_list.sort(reverse=False) #Syntax: list.sort([key,[Reverse_flag]])
print(new_list) #it will print the sorted kept flag to False.
print(new_list) 

# Output: [1, 2, 3, 3, 5, 8]

# Note: Key and reverse_flag are not necessary parameter and reverse_flag is set to False, if nothing is passed through sorted().

new_list = [2, 1, 3, 5, 3, 8]
new_list.sort(reverse=True) #list.sort([key,[Reverse_flag]])
print(new_list) #it will print the reverse list as the flag is set True

# Output: [8, 5, 3, 3, 2, 1]

# Copy: Returnd the copy of the list

Fruit_basket = ["apple","grapes","oranges","watermelon","mangoes", "apple"]
copy_list = Fruit_basket.copy() #new_list = list.copy()
print("The copied list:", copy_list)

# Output: The copied list: ['apple', 'grapes', 'oranges', 'watermelon', 'mangoes', 'apple']