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

    list_to_number([1, 0, 3])















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



main()