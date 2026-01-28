# written 1/28/26 by Lydia Allen
# funtion that takes three integers from the user and converts them from strings to integers

first = input("Enter first number: ")
first = float(first)
second = input("Enter second number: ")
second = float(second)
third = input("Enter third number: ")
third = float(third)
# uses a function built on if statement to compair the first to both the second and third.
def max_num(first, second, third):
    if first >= second and first >= third:
        return first
# if the second is bigger than the first and the third, it will print the second
    elif second >= first and second >= third:
        return second
# if the two statements above are not true, then the third must be the biggest. this will print the third.
    else:
        return third

print(max_num(first, second, third))