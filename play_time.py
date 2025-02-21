# Demo 2/20/2025:

# Problem 8: Above the Threshold
# Write a function above_threshold() that takes in a list of integers lst 
# and an integer threshold as parameters. The function iterates through 
# the original list and returns a new list containing only numbers that are 
# greater than threshold.

# def above_threshold(lst, threshold):
#     pass
# Example Usage:

# lst = [8,2,13,11,4,10,14]
# new_lst = above_threshold(lst, 10)
# print(new_lst)
# Example Output: [13,11,14]

# ********************** UMPIRE METHOD ****************************

# Understand
#   [] <-- will this always have values, will it be empty, not equal to
#   Threshold <-- negative numbers?
#   Output: new list

# Plan
#   Declare a new list variable "result"
#   Look at each value in the input list in order
#   #   Compare current value with the input parameter called "threshold"
#   #   Check if the current value is greater than "threshold"
#   #   #   Add the current value to the result list called "result"
#   Return the new list called "result"

# Implement

# *****************************************************************


def main():

    # sum_range(3, 9)

    lst = ["squirtle", "gengar", "charizard", "pikachu", "blastoise"]
    print_list(lst)



# Problem 1
# Problem 2
# Problem 3
# Problem 4
# Problem 5
# Problem 6
# Problem 7
# Problem 8
# Problem 9
# Problem 10
# Problem 11
# Problem 12
# Problem 14



#   Input: a value called "start", a value called "stop" - inclusive
#   Output: a value called "sum" - return

#   Plan
#   #   Declare a variable called "sum" initialize at 0
#   #   Count from the value of parameter "start" to the parameter "stop" 
#   #   #   Add the counter to "sum" during each iteration
#   #   Return the "sum" variable

def sum_range(start, stop):
    sum = 0
    for i in range(start, stop + 1):
        sum += i

    return sum



# Problem 1
# input: list as a parameter called "list"
# output: printing each value in "list"

# declare the function and call it print_list()
# take in a parameter called "list"
# check each current value in the list - string
#   #   print each current value to the console

def print_list(list):
    for pokemon in list:
        print(pokemon)



main()