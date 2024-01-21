# Exercise 5: Check if the first and last number of a list is the same
# Write a function to return True if the first and last number of a given list is same. 
# If numbers are different then return False.

# pseudocode
# def func
#   if else statement that print True or False
# assigning list1
# assigning list2
# calling def func

# Function
def checking(list):
    if list[0] == list[-1]:
        print(f"Given list: {list}")
        print(f"The result is {True}.")
    else:
        print(f"Given list: {list}")
        print(f"The result is {False}.")

# Given
numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

# Calling functions
checking(numbers_x)
checking(numbers_y)