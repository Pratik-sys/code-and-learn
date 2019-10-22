# Question: Build a string with the numbers from 0 to 100, "0123456789101112..."

# Solution:

values = ' '.join([str(i) for i in range(0,100)])
print(values)