# Unit 1 Session 2 - Problem Set Version 1

def main():
    # print_list(["Squirtle", "Gengar", "Charizard", "Pikachu"])


    # doubled([1, 2, 3])


    # print(rdoubled([1, 2, 3]))


    # lst = [1,-2,-3,4]
    # flipped_lst = flip_sign(lst)
    # print(flipped_lst)


    # lst = [5,22,8,10,2, 100]
    # max_diff = max_difference(lst)
    # print(max_diff)


    # numbers = [12,8,2,4,4,1,1,1,10]
    # counter = count_less_than(numbers,5)
    # print(counter)


    # lst = [1,3,3,7]
    # evens_lst = get_evens(lst)
    # print(evens_lst)


    # multiples_of_five()


    # lst = find_divisors(24)
    # print(lst)


    # fizzbuzz(13)


    # lst = [5,1,3,8,2,3,4,5]
    # print_indices(lst)


    lst = [1,4,5,2,8]
    position = linear_search(lst,10)
    print(position)







# Problem 1: Print List
def print_list(list):
    for item in list:
        print(item)



# Problem 2: Print Doubled List
def doubled(list):
    for i in range(len(list)):
        print(list[i] * 2)



# Problem 3: Return Doubled List
def rdoubled(list):
    result = []
    for i in range(len(list)):
        result.append(list[i] * 2)

    return result



# Problem 4: Flip Signs
def flip_sign(list):
    result = []
    for i in range(len(list)):
        result.append(list[i] * -1)

    return result



# Problem 5: Max Difference
def max_difference(list):
    min = list[0]
    for i in range(1, len(list)):
        if list[i] < min:
            min = list[i]

    max = list[0]
    for i in range(1, len(list)):
        if list[i] > max:
            max = list[i]

    return max - min



# Problem 6: Below Threshold
def count_less_than(list, threshold):
    count = 0
    for num in list:
        if num < threshold:
            count += 1

    return count



# Problem 7: Evens List
def get_evens(list):
    result = []
    for num in list:
        if num % 2 == 0:
            result.append(num)

    return result # returns an empty list, not null



# Problem 8: Multiples of Five
def multiples_of_five():
    for i in range(1, 101):
        if i % 5 == 0:
            print(i)



# Problem 9: Divisors
def find_divisors(n):
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)

    return result



# Problem 10: FizzBuzz
def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)



# Problem 11: Print the Index
def print_indices(list):
    for i in range(len(list)):
        print(i)



# Problem 12: Linear Search
def linear_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
        
    return -1



main()