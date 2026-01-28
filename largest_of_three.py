# written 1/20/26 by Lydia Allen
# takes three integers from the user and converts them from strings to integers
first = input("Enter first number: ")
first = float(first)
second = input("Enter second number: ")
second = float(second)
third = input("Enter third number: ")
third = float(third)
# nested if statements
if first>= second:
    if first >= third:
        print(first)
    else:
        print(third)
else:
    if second >= third:
        print(second)
    else:
        print(third)