# Unit 1 Session 1

def main():
    # hello_world()


    # todays_mood()


    # print_menu("Ramen")


    # print(sum(20, 8) * 2)


    # print(product(22, 7))


    # output = classify_age(18)
    # print(output)
    # output = classify_age(7)
    # print(output)
    # output = classify_age(50)
    # print(output)


    # time = what_time_is_it(2)
    # print(time)
    # time = what_time_is_it(7)
    # print(time)
    # time = what_time_is_it(12)
    # print(time)


    # blackjack(24)
    # blackjack(19)
    # blackjack(21)
    # blackjack(10)


    # my_list = [3, 1, 6, 7, 5]
    # print(get_first(my_list))


    # my_list = [3, 1, 6, 7, 5, 8]
    # print(get_last(my_list))


    # counter(7)


    # print(sum_ten())
    

    # print(sum_positive_range(6))


    # print(sum_range(3, 9))


    # print_negatives([3, -2, 2, 1, -5, -8, -99])


    # *COMPLETED*






















# Problem 1: Hello World!
def hello_world():
    print("Hello, world!")


# Problem 2: Today's Mood
def todays_mood():
    mood = "Sad"
    print("Today's mood: " + mood)


# Problem 3: Lunch Menu
def print_menu(menu):
    print("Lunch today is: " + menu)


# Problem 4: Sum of Two Integers
def sum(a, b):
    return a + b


# Problem 5: Product of Two Integers
def product(a, b):
    return a * b


# Problem 6: Classify Age
def classify_age(age):
    if age < 18:
        return "child"
    else:
        return "adult"


# Problem 7: What Time is It?
def what_time_is_it(hour):
    if hour == 2:
        return "taco time!"
    elif hour == 12:
        return "peanut butter jelly time!"
    else:
        return "nap time!"


# Problem 8: Blackjack
def blackjack(score):
    if score == 21:
        print("Blackjack!")
    elif score > 21:
        print("Bust!")
    elif score >= 17 and score < 21:
        print("Nice hand!")
    elif score < 17:
        print("Hit me!")


# Problem 9: First Item
def get_first(list):
    if not list:
        return None
    
    return list[0]


# Problem 10: Last Item
def get_last(list):
    if not list:
        return None
    
    return list[len(list) - 1]


# Problem 11: Counter
def counter(stop):
    for i in range(1, stop + 1):
        print(i)


# Problem 12: Sum of 1 to 10
def sum_ten():
    sum = 0
    for i in range(1, 11):
        sum += i

    return sum


# Problem 13: Total Sum
def sum_positive_range(stop):
    sum = 0
    for i in range (1, stop + 1):
        sum += i

    return sum


# Problem 14: Total Sum in Range
def sum_range(start, stop):
    sum = 0
    for i in range(start, stop + 1):
        sum += i

    return sum


# Problem 15: Negative Numbers
def print_negatives(list):
    count = 0
    for i in range(len(list)):
        if list[i] < 0:
            print(list[i])
            count += 1

    if not count:
        print(None)
    








main()