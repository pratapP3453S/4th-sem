# Design a program for creating a machine which accepts string having equal no. of 1’s and 0’s.

def Check_equal_zero_one(binary_string):
    Zeros = binary_string.count("0")
    Ones = binary_string.count("1")
    if Zeros == Ones:
        return True
    else:
        return False
    
binary_string = (input("Enter a binary string : "))
if Check_equal_zero_one(binary_string):
    print("The number of 0 and 1 are equal.")
else:
    print("The number of 0 and 1 are not equal.")