def main():
    # greet_user("John")


    # diff = difference(3, 8)
    # print(diff)


    # concatenate_list([1, 2, 3, 4])


    # sleep_assessment(10)
    # sleep_assessment(4)
    # sleep_assessment(12)
    # sleep_assessment(9)


    # tip1 = calculate_tip(44.53, "average")
    # print(tip1)
    # tip2 = calculate_tip(44.53, "poor")
    # print(tip2)
    # tip3 = calculate_tip(44.53, "excellent")
    # print(tip3)


    # rock_paper_scissors("rock", "rock")
    # rock_paper_scissors("scissors", "rock")
    # rock_paper_scissors("scissors", "paper")
    # rock_paper_scissors("rock", "paper")
    # rock_paper_scissors("paper", "rock")


    # print(halve_list([2, 4, 6, 8]))


    # list = [8, 2, 13, 11, 4, 10, 14, 20, 100, 1123]
    # print(above_threshold(list, 10))


    # countdown(10, 10)


    # print(power(2, 5))
    # print(power(3, 3))


    # print(list_length([2, 4, 6, 8, 10, 12, 14, 16, 18]))


    # print(factorial(5))


    # print(squares([1, 2, 3, 4]))


    # print(multiply_list([1, 2, 3], 3))


    # print(count_evens([1, 5, 7, 9]))
    # print(count_evens([2, 4, 6, 8]))


    











# Problem 1: Hello User!
def greet_user(name):
    print("Hello, " + name)


# Problem 2: Calculate Difference
def difference(a, b):
    return a - b


# Problem 3: List Concatenation
def concatenate_list(nums):
    ans = []
    for i in range(2):
        for i in range(len(nums)):
            ans.append(nums[i])

    print(ans)


# Problem 4: Sleep Assessment
def sleep_assessment(hours):
    if hours < 8:
        print("Oof, go back to bed!")
    elif hours >= 8 and hours <= 10:
        print("You got a good night's rest!")
    elif hours > 10:
        print("You're a sleep prodigy!")


# Problem 5: Calculate Tip
def calculate_tip(bill, service_quality):
    if service_quality == "poor":
        return bill * .10
    elif service_quality == "average":
        return bill * .15
    elif service_quality == "excellent":
        return bill * .20
    else:
        return None
    


# Problem 6: Rock, Paper, Scissors
def rock_paper_scissors(player1, player2):
    if player1 == "rock" and player2 == "rock" or player1 == "paper" and player2 == "paper" or player1 == "scissors" and player2 == "scissors":
        print("It's a tie!")
    elif player1 == "rock" and player2 == "scissors" or player1 == "paper" and player2 == "rock" or player1 == "scissors" and player2 == "paper":
        print("Player 1 wins!")
    elif player2 == "rock" and player1 == "scissors" or player2 == "paper" and player1 == "rock" or player2 == "scissors" and player1 == "paper":
        print("Player 2 wins!")


# Problem 7: Unscramble and Divide
def halve_list(list):
    result = []
    for num in list:
        halved = num / 2
        result.append(halved)

    return result


# Problem 8: Above the Threshold
def above_threshold(list, threshold):
    result = []
    for i in range(len(list)):
        if list[i] > threshold:
            result.append(list[i])

    return result


# Problem 9: Countdown
def countdown(m, n):
    for i in range(m):
        if m >= n:
            print(m)
            m -= 1


# Problem 10: Calculate Power
def power(base, exponent):
    result = base ** exponent
    return result


# Problem 11: Length of List
def list_length(list):
    count = 0
    for num in list:
        count += 1

    return count


# Problem 12: Calculate Factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i

    return result


# Problem 13: Count the Squares
def squares(list):
    result = []
    for i in range(len(list)):
        result.append(list[i] ** 2)

    return result


# Problem 14: Multiply List
def multiply_list(list, multiplier):
    result = []
    for i in range(len(list)):
        result.append(list[i] * multiplier)

    return result


# Problem 15: Count Evens
def count_evens(list):
    evens = 0
    for i in range(len(list)):
        if list[i] % 2 == 0:
            evens += 1

    return evens


main()