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


# Problem 7: Unscamble and Divide

main()