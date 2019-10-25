import random
from datetime import date
import calendar
import math
import sys
import datetime

# EXERCISE 1
# Write a Python program to print the following string in a specific format
print("Twinkle, twinkle, little star,\n \t \t How I wonder what you are!\n \t \t \t \t Up above the world so high,\n \t \t \t \t Like a diamond in the sky.\n Twinkle, twinkle, little star,\n \t \t How I wonder what you are")


# EXERCISE 2
# Write a Python program to get the Python version you are using.
print(sys.version)


# EXERCISE 3
# Write a Python program to display the current date and time.
#import datetime
now = datetime.datetime.now()
print("Current date and time : ")
print(now.strftime("%Y/%m/%d %H:%M:%S"))


# EXERCISE 4
# Write a Python program which accepts the radius of a circle from the user and compute the area.
radius = float(input("please enter radius: "))
area = math.pi * (radius**2)
print(f"r= {radius}")
print(f"Area = {area}")


# EXERCISE 5
# Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
print(f"{last_name[::-1]} {first_name[::-1]}")


# EXERCISE 6
# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
user_input_string = input("Enter your comma separated numbers: ")
user_list = user_input_string.split(",")
print(user_list)
print(tuple(user_list))


# EXERCISE 7
# Write a Python program to accept a filename from the user and print the extension of that.
user_input_file = input("Enter your file name with extension: ")
user_list = user_input_file.split(".")
print(f"Your file extension is {user_list[-1]}")


# EXERCISE 8
# Write a Python program to display the first and last colors from the following list.
color_list = ["Red", "Green", "White", "Black"]
print(color_list[0] + " " + color_list[-1])


# EXERCISE 9
# Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
print(
    f"Your exams will start from {exam_st_date[0]} / {exam_st_date[1]} / {exam_st_date[2]}")


# EXERCISE 10
# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
user_input_number = input("Please enter your number: ")
n = int(user_input_number)
nn = int(user_input_number*2)
nnn = int(user_input_number*3)
result = n + nn + nnn
print(result)


# EXERCISE 11
# Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).


# EXERCISE 12
# Write a Python program to print the calendar of a given month and year.
# import calendar
year = int(input("Please enter the year: "))
month = int(input("Please enter the month: "))

for i in range(3):
    first_week_day = input(
        "Please enter the day you yould like to start the week with: ").lower()

    if first_week_day == "monday":
        first_week_day = 0
        break
    elif first_week_day == "tuesday":
        first_week_day = 1
        break
    elif first_week_day == "wednesday":
        first_week_day = 2
        break
    elif first_week_day == "thursday":
        first_week_day = 3
        break
    elif first_week_day == "friday":
        first_week_day = 4
        break
    elif first_week_day == "saturday":
        first_week_day = 5
        break
    elif first_week_day == "sunday":
        first_week_day = 6
        break
    else:
        print(f"The entered day is not correct, retries remaining {2 - i}")

    if i == 2:
        print("Retries exceeded, start of week automatically set to Monday")
        first_week_day = 0

calendar.setfirstweekday(first_week_day)
print(calendar.month(year, month))


# EXERCISE 13
# Write a Python program to print the following here document.


# EXERCISE 14
# Write a Python program to calculate number of days between two dates. Sample dates : (2014, 7, 2), (2014, 7, 11)
# from datetime import date
date1 = input("Enter your first date in the format YYYY, MM, DD: ").split(",")

for i in range(len(date1)):  # converting list items from string to integer
    date1[i] = int(date1[i])

try:
    d0 = date(date1[0], date1[1], date1[2])
except ValueError:
    print("Please type a valid date in correct format")
    date1 = input(
        "Enter your first date in the format YYYY, MM, DD: ").split(",")
    for i in range(len(date1)):
        date1[i] = int(date1[i])
    d0 = date(date1[0], date1[1], date1[2])


date2 = input("Enter your second date in the format YYYY, MM, DD: ").split(",")

for i in range(len(date2)):
    date2[i] = int(date2[i])

try:
    d1 = date(date2[0], date2[1], date2[2])
except:
    print("Please type a valid date in correct format")
    date2 = input(
        "Enter your second date in the format YYYY, MM, DD: ").split(",")
    for i in range(len(date2)):
        date2[i] = int(date2[i])
    d1 = date(date2[0], date2[1], date2[2])


delta = abs(d1 - d0)
print(f"Difference in date: {delta.days} days")


# EXERCISE 15
# Write a Python program to get the volume of a sphere with radius 6.
radius = int(input("Enter the radius of sphere: "))

area = (4/3)*(math.pi)*(radius**3)

print(f"Volume: {area}")


# EXERCISE 16
# Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference
number = int(
    input("Enter the number you would like to calculate the differenc from 17: "))

if number > 17:
    difference = (number - 17)*2
    print(difference)
else:
    difference = 17 - number
    print(difference)


# EXERCISE 17
# Write a Python program to test whether a number is within 100 of 1000 or 2000.
number = int(input("Please enter your number: "))

if (abs(number - 1000)) < 100:
    print("Number is within 100 of 1000")
elif (abs(number - 2000) < 100):
    print("Number is within 100 of 2000")
else:
    print("You serious?")


# EXERCISE 18
# Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.
def sum(x, y, z):
    if x == y and y == z:
        return(3*(x+y+z))
    else:
        return(x+y+z)


print(sum(10, 10, 10))
print(sum(10, 11, 12))


# EXERCISE 19
# Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.
def AddIs(string):
    if string[0:2] != "Is":
        return("Is" + string)
    else:
        return(string)


print(AddIs("IsMyName"))
print(AddIs("Hello"))


# EXERCISE 20
# Write a Python program to get a string which is n (non-negative integer) copies of a given string.
string = input("Enter your string: ")
number = int(input("How many copies of string would you like: "))

print(string*number)


# EXERCISE 21
# Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.
number = int(input("Enter your number: "))


def EvenOdd(number):
    if number % 2 == 0:
        return("Number is Even")
    else:
        return("Number is Odd")


print(EvenOdd(number))

# EXERCISE 22
# Write a Python program to count the number 4 in a given list.
x = [1, 4, 5, 4, 6, 9, 4]

y = [num for num in x if num == 4]

print(len(y))


# EXERCISE 23
# Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2.
string = input("Please input your string: ")
number = int(input("Enter the copies you want for the first two characters: "))


def first_two_char(str, num):
    if len(str) >= 2:
        return str[0:2]*num
    return str*num


print(first_two_char(string, number))


# EXERCISE 24
# Write a Python program to test whether a passed letter is a vowel or not.
string = input("Please input your letter: ")

try:
    int(string)
    print("Please enter a valid letter")
    string = input("Please input your letter: ")
except:
    if len(string) > 1:
        print("Please enter a single letter only")
        string = input("Please input your letter: ")


def vowel_check(s):
    if s == "a" or s == "e" or s == "i" or s == "o" or s == "u":
        return "Vowel"
    return "Not a vowel"


print(vowel_check(string))


# EXERCISE 25
# Write a Python program to check whether a specified value is contained in a group of values.
list1 = [1, 2, 3, 4]

value = int(input("Enter the number you would like to search: "))

if value in list1:
    print(True)
else:
    print(False)


# EXERCISE 26
# Write a Python program to create a histogram from a given list of integers.


# EXERCISE 27
# Write a Python program to concatenate all elements in a list into a string and return it.
list1 = [1, 2, 3, 4, "a", "b"]


def lst_to_str(lst):
    str1 = ""
    for item in lst:
        str1 += str(item)
    return str1


print(lst_to_str(list1))


# EXERCISE 28
# Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence.
numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 743, 527
]


even_numbers = []

for num in numbers:
    if num % 2 == 0 or num == 237:
        even_numbers.append(num)
        if num == 237:
            break

print(*even_numbers)


# EXERCISE 29
# Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

print(color_list_1 - color_list_2)  # difference of two sets


# EXERCISE 30
# Write a Python program that will accept the base and height of a triangle and compute the area.
base = int(input("Please enter your base: "))
height = int(input("Please enter your height: "))

area = 0.5 * base * height
print(area)


# EXERCISE 31
# Write a Python program to compute the greatest common divisor (GCD) of two positive integers.


# EXERCISE 32
# Write a Python program to get the least common multiple (LCM) of two positive integers.


# EXERCISE 33
# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
num1 = 2
num2 = 2
num3 = 3


def add(n1, n2, n3):
    if n1 == n2 or n1 == n3 or n2 == n3:
        return 0
    else:
        return n1 + n2 + n3


print(add(num1, num2, num3))


# EXERCISE 34
# Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.


#################################################################################################################

# Exercise 4: Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
number = int(input("Please enter your number: "))
divisors = []

for i in range(1, (number + 1)):
    if number % i == 0:
        divisors.append(i)

print(divisors)


# Exercise 5: Take two lists, say for example these two and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
#import random
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

set_a = set(a)
set_b = set(b)

intersection_a_b_set = set_a & set_b

print("a: ", set_a)
print("b: ", set_b)
print("intersection set of a and b", intersection_a_b_set)

intersection_a_b_list = []

for item in intersection_a_b_set:
    intersection_a_b_list.append(item)

intersection_a_b_list.sort(reverse=True)  # this setep is just for fun
print("intersection list of a and b", intersection_a_b_list)


# Generating random lists and performing same operations
list_c_len = random.randint(5, 10)
list_d_len = random.randint(5, 10)

c = []
d = []

for i in range(0, list_c_len):
    x = random.randint(1, 15)
    c.append(x)

for i in range(0, list_d_len):
    x = random.randint(1, 15)
    d.append(x)


set_c = set(c)
set_d = set(d)
intersection_c_d_set = set_c & set_d


print("c: ", set_c)
print("d: ", set_d)
print("intersection set of c and d", intersection_c_d_set)

intersection_c_d_list = []

for item in intersection_c_d_set:
    intersection_c_d_list.append(item)

print("intersection list of c and d", intersection_c_d_list)


# Exercise 6: Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
string1 = input("Please enter your sitring: ")

list_from_string = list(string1)

reversed_string = list_from_string[::-1]


def palindrome_or_not(list, rev_list):
    if list == rev_list:
        print("Your string is palindrome!")
    else:
        print("Your string is NOT palindrome!")


palindrome_or_not(list_from_string, reversed_string)


# Exercise 7: Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

b = [item for item in a if item % 2 == 0]

print(b)


# Exercise 8: Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
replay = ""

while replay != "n":

    player1 = input("Rock, Paper or Scissor: ").lower()
    player2 = input("Rock, Paper or Scissor: ").lower()

    if (player1 == "rock" and player2 == "scissor") or (player1 == "paper" and player2 == "rock") or (player1 == "scissor" and player2 == "paper"):
        print("Player 1 Wins!!!")
    elif (player2 == "rock" and player1 == "scissor") or (player2 == "paper" and player1 == "rock") or (player2 == "scissor" and player1 == "paper"):
        print("Player 2 Wins!!!")
    else:
        print("DRAW!!")

    replay = input("Would you like to replay(y/n)? ")

print("Thank you for playing the game, see you again some time.")


# Exercise 9: Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
rand_number = str(random.randint(1, 9))
guesses = 0
replay = ""

print(rand_number)  # prinitng randomly generated number here for testing purposes

while replay != "exit":

    rand_guess = input("Please enter your guess between 1 and 9: ").lower()

    if rand_guess == "exit":
        break
    elif rand_guess == rand_number:
        print("You got it right!")
        guesses += 1
        break
    elif int(rand_guess) < 1 or int(rand_guess) > 9:
        print("The number you entered is not between 1 and 9.")
    elif (int(rand_guess) - int(rand_number)) > 0:
        print("You guessed too high")
        guesses += 1
    elif (int(rand_guess) - int(rand_number)) < 0:
        print("You guessed too low")
        guesses += 1

print("Total Guesses:", guesses)


# Exercise 10: Take two lists, say for example these two, and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes. Write this using at least one list comprehension.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


common_elements = [item_a for item_a in set(    # creating list to set to remove duplicates
    a) for item_b in set(b) if item_a == item_b]
print(common_elements)


# Exercise 11: Ask the user for a number and determine whether the number is prime or not.
def prime(num):
    divisors = 0
    for i in range(2, num):
        if num % i == 0:
            divisors += 1
    if divisors == 0:
        print(f"Number {num} is PRIME")
    else:
        print(f"Number {num} is NOT Prime")


prime(5)


# Exercise 12: Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.
string1 = input(
    "Please enter your list of numbers separated by commas: ").replace(" ", "")

list1 = string1.split(",")

for i in range(len(list1)):
    list1[i] = int(list1[i])

# list comprehension to create new list of first and last item from original list
new_list = [item for item in list1 if (item == list1[0] or item == list1[-1])]

print(list1)
print(new_list)


# Exercise 13: Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
fib_len = int(input("Enter the length of Fibonacci sequence you desire: "))


def generate_fib(fib_len):
    fib_list = [1, 1]
    for i in range(2, fib_len):
        new_entry = fib_list[i-1] + fib_list[i-2]
        fib_list.append(new_entry)
    return fib_list[0:fib_len]


print(generate_fib(fib_len))


# Exercise 14: Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
string1 = input(
    "Please enter your list of numbers separated by commas: ").replace(" ", "")

list1 = string1.split(",")


def using_set(list1):
    set1 = set(list1)
    list1 = list(set1)
    return list1


print(using_set(list1))


def using_loop(test):
    non_repeating_list = []
    for item in test:
        if item not in non_repeating_list:
            non_repeating_list.append(item)
    return non_repeating_list


print(using_loop(list1))


# Exercise 15: Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order.
list1 = input(
    "Please enter the sentence you want to reverse print: ").split(" ")


def reverse_print(list1):
    list1 = list1[::-1]
    for i in range(len(list1)):
        if list1[i] != list1[-1]:
            list1[i] = list1[i] + " "

    string1 = "".join(list1)  # converting list to string
    return string1


print(reverse_print(list1))


# Exercise 16: Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.


# Exercise 18: Create a program that will play the “cows and bulls” game with the user.
rand_num = str(random.randint(1000, 9999))
print(rand_num)
print(len(rand_num))
run_condition = True  # setting condition True to make sure while loop runs at least once


def cows_bulls(rand_num):
    user_guess = input("Please enter your guess: ")
    guesses = 0
    while run_condition:
        cow = 0
        bull = 0
        for i in range(len(rand_num)):
            if rand_num[i] == user_guess[i]:
                cow += 1
            elif user_guess[i] in rand_num:
                bull += 1

        guesses += 1
        print("Cows:", cow)
        print("Bulls:", bull)
        print("Guesses:", guesses)

        if user_guess == rand_num:
            print("You won")
            break
        else:
            user_guess = input("Please enter your guess: ")


cows_bulls(rand_num)


# Exercise 19:
