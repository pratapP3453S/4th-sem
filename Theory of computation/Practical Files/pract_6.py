# Design a program for accepting decimal number divisible by 2.

while True:
    num = float(input("Enter a decimal number : "))
    if num % 2 == 0:
        print("Accepted")
        break
    else:
        print("Number is not divisible by 2.")