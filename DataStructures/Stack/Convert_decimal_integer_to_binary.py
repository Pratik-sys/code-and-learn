#!/usr/bin/python3

# Convert deciaml to binary using Stack Operation 

def Convert(num):
    """ The functions returns the binary format of the interger """
    stack = [] # using empty list as stack.
    while num > 0 :
        reminder = num % 2
        stack.append(reminder)
        num = num // 2
    bin_num = ""
    for _ in range(len(stack)):
        bin_num+=str(stack.pop()) 
        # combining the pope element with empty string to get the output.
    return bin_num
print(Convert(45))
