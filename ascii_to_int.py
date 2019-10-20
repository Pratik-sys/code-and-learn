# Question: How to convert a string to a number that consists of letters ASCII code. Example: 'abcd' -> 979899100. Write a program for this.

# Solution:

rat = input("enter the ASCII code:") 
p1 = list(rat)
r2 = [ord(i) for i in rat]

print(p1)
print(r2)