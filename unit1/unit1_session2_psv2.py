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


    list = [1, 2, 3, 4, 5]
    # print(list)
    reversed_list = reverse_list(list)
    print(reversed_list)













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

# *** Understand ***

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

# --------------------
# Function Steps
# --------------------

# Pass argument into reverse list function
# Initialize a new list
# For each element in the input list, starting from the last element:
#   # Append the element to the new list
# Return the new list

def reverse_list(list):
    result = []
    for i in range(len(list) - 1, -1, -1):
        result.append(list[i])
    
    return result



main()