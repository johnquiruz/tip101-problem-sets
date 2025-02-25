# Unit 2 Session 1

def main():
 
#  TEST FOR PROBLEM 1:
#  list = [5, 1, 22, 25, 6, -1, 8, 10]
#  sequence = [1, 6, -1, 10, 22]
#  print(is_subsequence(list, sequence))


# TEST FOR PROBLEM 2:
#  keys = ["peanut", "dragon", "star", "pop", "space"]
#  values = ["butter", "fly", "fish", "corn", "ship"]

#  print(create_dictionary(keys, values))

#  dict = create_dictionary(keys, values)

#  print(dict)
#  print(dict["space"])
#  print(dict.keys())
#  print(dict.values())
#  print(dict.items())





###################################### FUNCTIONS #######################################

# Problem 1: Subsequence

# UNDERSTAND
#
# This function takes in two list parameters, the first one called 'list'
# and the second one is called 'sequence'. The function checks if the values
# is the SECOND parameter EXISTS in the FIRST parameter. RETURN a BOOLEAN 
# TRUE if 'sequence' is a subsequence of 'list' and FALSE otherwise.
#
# INPUT DATATYPES: 
#   # a list of integers called 'list', LIST
#   # a list of integers called 'sequence', LIST
#
# OUTPUT, DATATYPES:
#   # a counter called 'count', INTEGER

# PLAN
#
# Define the function called 'is subsequence'.
# Declare a variable called 'count' and set it equal to 0.
# Check if the 'sequence' parameter is smaller than the 'list' parameter.
#   # If it is not smaller, return the boolean false.
#   # If it is smaller, do the following:
#   #   # Check each element in 'sequence' one at a time:
#   #   #   # Compare to each element in 'list':
#   #   #   #   # If the current element in 'subsequence' equals the current element in 'list':
#   #   #   #   #   # Add a one to the counter 'count'.
#   #   #   #   # If it is NOT equal:
#   #   #   #   #   # RETURN false
#   #   # Compare the value of 'count' and the LENGTH of the list 'sequence' to see if EQUAL:
#   #   #   # RETURN TRUE if they are equal.

# IMPLEMENT

def is_subsequence(list, sequence):
 count = 0

 if len(sequence) < len(list):
  for i in range(len(sequence)):
   for j in range(len(list)):
    if sequence[i] == list[j]:
     count += 1

 if count == len(sequence):
  return True
 
 return False



# Problem 2: Create a Dictionary

# UNDERSTAND
#
# This function is passed a list of values (just strings?) called 'keys' that will represent the keys
# of a dictionary (parameter 1), and a list of values called 'values' that will represent the values
# of the keys (parameter 2). The function creates a dictionary called 'dict' out of these two parameters which are
# assumed to have the same lengths.
#
# INPUT, DATATYPE:
#   # a list of strings for the keys, LIST
#   # a list of strings for the values, LIST
#
# OUTPUT, DATATYPE:
#   # a dictionary with keys and their corresponding values, DICTIONARY

# PLAN
#
# Define a function called 'create dictionary' that takes in two parameters called 'keys' and 'values'
# Declare an empty dictionary called 'dict'
# Iterate through every element in parameter one 'keys' keeping track of the index (using range/len method)
#   # Set the current element in parameter one 'keys' to a new spot in the dictionary 'dict'
#   # Map the current element in parameter two 'values' to the newly set key in the dictionary 'dict'
# Return dictionary 'dict'

# IMPLEMENT

def create_dictionary(keys, values):
 dict = {}

 for i in range(len(keys)):
  dict[keys[i]] = values[i]

 return dict





main()