# Unit 1 Session 2 - Problem Set Version 2

def main():
    # temperatures = convertTemp(23.00)
    # print(temperatures)


    # scores = [84,73,92,95,88]
    # avg_score = average(scores)
    # print(avg_score)


    # lst = [6,9,81,20]
    # new_lst = increment_values(lst)
    # print(new_lst)


    # lst = [5,2,3,9,10]
    # flag1 = check_num(lst,9)
    # flag2 = check_num(lst,4)
    # print(flag1)
    # print(flag2)


    # nums = [0, 4, 3, 1, 5]
    # missing_num = find_missing(nums)
    # print(missing_num)


    # list = [1, 2, 3, 4, 5]
    # # print(list)
    # reversed_list = reverse_list(list)
    # print(reversed_list)


    # nums = [2, 5, 1, 8, 6, 5, 3, 3, 3]
    # odd_nums = get_odds(nums)
    # print(odd_nums)


    # multiplication_table(7)

    # list_to_number([1, 0, 3])

    # nums = [0,0,100,1,0,2,3,0,0,4]
    # new_nums = move_zeroes(nums)
    # print(new_nums)


    # nums = [3,4,8,1,5,2,3,32]
    # print_odd_indices(nums)

    lst = [1,2,6,5,2,1,3,2,2]
    index_list = find_all_occurrences(lst, 1)
    print(index_list)















# Problem 1: Convert Temperature
def convertTemp(celsius):
    ans = []
    kelvin = celsius + 273.15
    fahrenheit = celsius * 1.80 + 32.00

    ans.append(kelvin)
    ans.append(fahrenheit)

    return ans



# Problem 2: Average Score
def average(scores):
    sum = 0

    for nums in scores:
        sum += nums

    avg = sum / len(scores)

    return avg



# Problem 3: Increment by 1
def increment_values(list):
    result = []

    for i in list:
        result.append(i + 1)

    return result



# Problem 4: Check for Number
def check_num(list, num):
    for i in list:
        if i == num:
            return True
        
    return False



# Problem 5: Missing Number
def find_missing(list):
    list.sort()
    
    for i in range(len(list)):
        if list[i] != i:
            return i
    
    return len(list)



# Problem 6: Reverse List

# *** Understand *************************

# This is a function in which a client inputs a list of integers
# and returns a new list containing the integers of the parameter
# in reverse order.

# --------------------
# Sample run:
# --------------------

# list = [1, 2, 3, 4, 5]
# reversed_list = reverse_list(list)
# print(reversed_list)

# Output: [5, 4, 3, 2, 1]

# --------------------
# Input, Datatypes:
# --------------------

# list, list

# --------------------
# Output, Datatypes:
# --------------------

# reversed_list, list

# --------------------
# Process
# --------------------

# for loop, iterate in reverse order
# append method

# ************ PLAN ***************************

# --------------------
# Function Steps
# --------------------

# Pass argument into reverse list function
# Initialize a new list
# For each element in the input list, starting from the last element:
#   # Append the element to the new list
# Return the new list

# ************ IMPLEMENT ************************

def reverse_list(list):
    result = []
    for i in range(len(list) - 1, -1, -1):
        result.append(list[i])
    
    return result



# Problem 7: Get Odd Numbers

# UNDERSTAND

# This function takes an input LIST of INTEGERS as a parameter
# and RETURNS a NEW LIST of ODD elements from the input.

# Input, Datatypes: a list of integers (sign unspecified)
# Output, Datatypes: a list of odd integers (sign unspecified)
# Calculcations, Control Flow: for-loop, no methods

# PLAN

# Define a function called "Get odds"
# Define a list of integers called "numbers" as a parameter
# Inside function, reserve an empty new list called "result" for odd integers
# Check each element in the list parameter, "numbers"
#   # If the current element is not divisible by 2
#   #   # Add the element to the new list, "result"
# Return the new list "result" to the client

# IMPLEMENT

def get_odds(numbers):
    result = []
    for i in numbers:
        if i % 2 != 0:
            result.append(i)

    return result



# Problem 8: Multiplication Table

# UNDERSTAND

# This function takes a SINGLE INTEGER parameter from the client
# and PRINTS the MULTIPLES of that integer 10 times

# Input, Datatypes:
#   # "number", integer
# Output, Datatypes: 
#   # 10 numbers that are multiples of the input, integers
# Calculation, Control Flow: 
#   # multiple of "number" = "number" + "number"
#   # for-loop using range method

# PLAN

# Define a function called "multiplication table"
# Declare a parameter called "number"
# Declare a variable called "sum" and set it to 0
# Declare a for loop that will repeat 10 times
#   # Add the parameter "number" to the "sum" and assign the value to "sum"
#   # Print the "sum" to the console

# IMPLEMENT

def multiplication_table(number):
    sum = 0
    for i in range(1, 11):
        sum = number + sum
        print(sum)



# Problem 9: Create Number

# UNDERSTAND

# This function takes a LIST of INTEGERS 
# BETWEEN 0 AND 9 (inclusive/exclusive unspecified) and 
# combines those integers into a SINGLE INTEGER (NOT a string); 
# this single integer is then RETURNED to the client.

# Input, Datatypes:
#   # a list of digits called "digits", list
#
# Output, Datatypes:
#   # a single integer called "result", integer
#
# Calculation:
#   # N/A

# PLAN

# Define a function called "list to a number"
# Declare a list of integers called "digits" as the parameter
# Declare a string variable called "result" (to be later converted to an integer)
# Check each element in the input parameter "digits"
#   # Add current element to the string "result" by concatenation
# Convert the datatype of "result" from a string to an integer
# Return the integer "result" to the client

# IMPLEMENT

def list_to_number(digits):
    result = ""

    for i in digits:
        result = result + str(i)

    result = int(result)

    print(result)



# Problem 10: Move Zeroes

# UNDERSTAND

# This function takes a LIST OF INTEGERS as a parameter and creates
# a NEW LIST that contains the values of the parameter list but is sorted so that 
# any existing zeroes in it are all pushed to the end of the list. The
# NON-ZERO INTEGERS in the list MAINTAIN THEIR RELATIVITY amongst each other and
# the new list is RETURNED to the client.

# Input, data types:
# list of integers called "numbers", list
#
# Output, data types:
# an integer variable called "count"
# list of integers called "sorted", list
#
# Calculations:
# count the amount of zeroes in the parameter

# PLAN

# Define the function
# Declare the list of integers called "numbers" as a parameter
# Declare a variable called "count"
# Declare an empty list called "sorted"
# Check each element in the parameter "numbers"
#   # if the number is a zero
#   #   # increment the counter by 1
#   # otherwise, if the number is non-zero
#   #   # add the current number to the new list "sorted"
# Declare a loop to iterate the same number of times as the amount of zeroes in "count"
#   # On the current iteration, add 1 zero to the new list "sorted"
# Return the new list "sorted"

# IMPLEMENT
def move_zeroes(numbers):
    zero_count = 0
    sorted = []

    for number in numbers:
        if number == 0:
            zero_count += 1
        else:
            sorted.append(number)
    
    for i in range(zero_count):
        sorted.append(0)

    return sorted



# Problem 11: Odd Indices

# UNDERSTAND

# This function takes in any size LIST OF INTEGERS (signed) as a parameter
# and prints each element inside of it that exists in an odd index (ex. indices: 1, 3, 5, 7, etc.)
# Zero does NOT count as an odd number.

# Input, data types:
#   # list of integers called "numbers", list
#
# Output, data types:
#   # each element in the parameter that falls on an odd index, integer
#
# Calculations:
#   # N/A

# PLAN 

# Define the function called "print odd indices"
# Declare a list of integers called "numbers" as the parameter
# Check each element in the list - use the range method since we need to know the index
#   # If the position of the index is not divisible by 2
#   #   # Print the element inside the list on the current index

# IMPLEMENT

def print_odd_indices(numbers):
    for i in range(len(numbers)):
        if i % 2 != 0:
            print(numbers[i])



# Problem 12: List Occurrences

# UNDERSTAND

# This function takes in a LIST OF INTEGERS (sign unspecified) and a SINGLE INTEGER
# as the parameters and creates A NEW LIST that contains INDICES where the single parameter
# OCCURS in the parameter list. RETURNS it.

# Input, data types:
#   # list of integers called "numbers", list
#   # a variable called "target", integer
#
# Output, data types:
#   # new list called "occurences", list
#
# Calculations, data types:
#   # N/A

# PLAN
# Define the function and call it "find all occurences"
# Declare a list of integers called "numbers" as the parameter
# Declare a variable called "target" as the second parameter
# Declare a new list called "occurrences"
# Check each element in the parameter
#   # Compare each element with the second parameter "target"; if they match
#   #   # Save the index of that element into the new list "occurrences"
# Return the new list "occurrences"

# IMPLEMENT

def find_all_occurrences(numbers, target):
    occurrences = []
    for i in range(len(numbers)):
        if numbers[i] == target:
            occurrences.append(i)

    return occurrences


main()