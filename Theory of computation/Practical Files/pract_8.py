# Design a program for creating a machine which count number of 1’s and 0’s in a given string.

def count_ones_zeros(input_string):
    count_ones = 0
    count_zeros = 0

    for char in input_string:
        if char == '1':
            count_ones += 1
        elif char == '0':
            count_zeros += 1
    return count_ones, count_zeros

def main():
    user_input = input("Enter a string : ")
    ones, zeros = count_ones_zeros(user_input)

    print(f"Number of '1's : {ones}")
    print(f"Number of '0's : {zeros}")

if __name__ == "__main__":
    main()