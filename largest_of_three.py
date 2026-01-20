# takes three integers from the user and converts them from strings to integers
first = input("Enter first number: ")
first = int(first)
second = input("Enter second number: ")
second = int(second)
third = input("Enter third number: ")
third = int(third)
# uses if statement to compair the first and second numbers
if first > second:
# if the first is bigger, compair the first with the third
    if first > third:
        largest = first
    else:
        largest = third
# if the second is bigger than the first compair the second with the third
else:
    if second >third:
        largest = second
    else:
        largest = third
# all comparisons are done, now it is time to print the largest number.
# if there is a tie, it will still print the correct number because all we care about is the number, not if it is the first second or third input
print(largest)