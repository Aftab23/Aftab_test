from timeit import timeit
import collections
from sys import getsizeof
from collections import deque
import sys
import math
from array import array

print("Hey man!")
x = 10 + 5
y = 11 + 3
print("whats upppp")

x = input("What is year of birth? ")
age = 2019 - int(x)

print(f"That means your age is {age}")

#####################################################################################################
# conditional statements
weather = input("What kind of weather is it today? ")
weather = weather.lower()

if weather == "rainy":
    print("I mostly prefer sunny weather but sometimes rainy is good")
elif weather == "snowy":
    print("time to take out those winter jackets")
elif weather == "sunny":
    print("wow, sunny! Time to visit the park today :D")
elif weather == "cloudy":
    print("well at least it's not raining :P")
else:
    print("are you living on Mars? :s")
#####################################################################################################
# ternary operator, used to simplify if else statements in one line, elif can not be used here
age = 19

message = "Enjoy your life buddy, live life conciously" if age < 20 else "Be responsible"
print(message)

#####################################################################################################
good_grades = True
student = True
graduate = False

if good_grades and student and not graduate:
    print("Congrats, you retain your scholarship!")
else:
    print("You are not eligible for a Scholarship.")

#####################################################################################################
# chaining comparison operators
age = 25

if 18 <= age < 65:
    print("Eligible!")
#####################################################################################################
# for loop
for number in range(5):
    print(f"Hello {number + 1}")
    print("Hi", number, ("." * number))

# for loop executed in a range with step increment
for number in range(1, 10, 2):
    print(number)

# break statements in for loop
successful = False
for number in range(1, 5):
    print("Attempt", number)
    if successful:
        print("Success!")
        break
    elif number == 4:
        print("Please try again later, we could not send your message")
        break

# nested loops
for x in range(4):
    for y in range(3):
        print(f"({x},{y})")

# iterables
string = "abcdef"  # a string is iterable
number_list = [1, 2, 3, 4, 5, 6]  # a list is also iterable

for letter in string:
    print(letter)

for number in number_list:
    print(number)

for loop in range(len(string)):
    print(f"{string[loop]} {number_list[loop]}")
#####################################################################################################
# while loop
number = 100
while number > 0:
    number //= 2
    print(number)

command = ""
while command != "quit":
    command = input(">").lower()
    print("ECHO", command)
#####################################################################################################
number_list = []

# inserting even numbers to a list

for numbers in range(1, 20):
    even_test = numbers % 2
    if even_test == 0:
        print(numbers)
        number_list.append(numbers)
print(f"We have {len(number_list)} even numbers")

#####################################################################################################
# FUNCTIONS that perform a task


def hello_func(name):
    print(f"Hi {name}")


hello_func("Aftab")


# FUNCTIONS that return a value

def addition_func(num1, num2):
    return num1 + num2


result = addition_func(2, 5)
print(result)

# accepting variable number of arguments in a function


def multiply(*numbers):
    result = 1
    for number in numbers:
        result *= number
    return result


# the variable number of arguments passed are passed as a tuple to the function
print("Hello")
print(multiply(2, 3, 4))
print(multiply(2, 3, "Hi"))


# functions with **args allow us to pass keyword arguments during function call and stores them as dictionary

def save_user(**user):
    print(user)
    print(user["id"])
    print(user["name"])
    print(user["age"])


save_user(id=1001, name="John", age=25)

# fizz buzz function


def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        print("fizz buzz")
    elif input % 5 == 0:
        print("buzz")
    elif input % 3 == 0:
        print("fizz")
    else:
        print(input)


fizz_buzz(15)

#####################################################################################################
# LISTS can contain strings, integers, both or even lists within lists

list_alpha = ["a", "b", "c", "d"]
List_num = [1, 2, 3, 4]
List_zeroes = [0] * 4
matrix = [[1, 2], [3, 4]]
print(matrix[1][1])
List_concat = list_alpha + List_num

print(List_zeroes)
print(matrix)
print(List_concat)


# produces list from number 1 till x
def list_append(till_x):
    list_till_x = []
    for i in range(1, till_x + 1):
        list_till_x.append(i)
    return list_till_x


print(list_append(10))

# doing the same using list comprehension
list_till_x = [num for num in range(5) if num != 0]

list_num2 = list(range(20))  # creates list of nums from 0 till 19
list_alpha2 = list("Hello World")  # creates a list from a string

print(list_num2)
print(list_alpha2)
print(len(list_num2))
print(list_num2[::-1])  # prints list in reverse order

# list unpacking
first, second, third, fourth = List_num

print(first)

first, second, *others = List_num

print(second)
print(others)

first, *other, last = List_num

print(other)
print(last)

# looping over a list
number_list = [1, 2, 3, 4]

for number in number_list:
    print(number)

alpha_list = ["a", "b", "c", "d"]

# enumerate function is used to assign indexes to values of a list
for index, alphabet in enumerate(alpha_list):
    print(index, alphabet*2)

# append/insert item to a list

alpha_list.append("e")
alpha_list.insert(0, "yo")

# removing item from list

alpha_list.pop()                # removes last item from list
alpha_list.pop(1)               # removes item from index 1 in the list

# removes a known item from list whose index is not known
alpha_list.remove("c")

# del statement helps us remove a range of items
del alpha_list[0:2]

# clear method removes all items from a list
alpha_list.clear()

# finding index of an item in a list

if "b" in alpha_list:
    index_item = alpha_list.index("b")
    print(index_item)

# counting the number of occurances of a given item in a list
alpha_list.count("b")

# sorting items in a list
sorting_list = [5, 6, 7, 1, 3, 9, 100, 50]

print(sorting_list)
# sorts list and saves changes to a new list
print(sorted(sorting_list))
print(sorting_list)
sorting_list.sort()  # sorts list and saves changes to existing list
print(sorting_list)
sorting_list.sort(reverse=True)  # sorting a list in reverse
print(sorting_list)

# customizing your own search criteria by defining key

items = [
    ("Product1", 9),
    ("Product2", 7),
    ("Product3", 8),
    ("Product4", 6)
]

# returns the price of product so we can use that to sort the list


def sort_items(item):
    return item[1]


items.sort(key=sort_items, reverse=True)
print(items)

# lambda function
# a cleaner way of defining a function we will use only once as an argument to another function
items.sort(key=lambda item: item[1], reverse=True)
print(items)

#####################################################################################################
# map function takes a lambda function and applies it to every item of the iterable object

prices = list(map(lambda item: item[1] + 5, items))

print(prices)

for price in prices:
    print(price)

#####################################################################################################
# filter function filters out those items from list for which lambda function condition is true
expensive_items = list(filter(lambda item: item[1] >= 8, items))
expensive_items.sort(key=lambda item: item[1])

print(expensive_items)

# list comprehension is an alternate and cleaner way to map and filter lists

prices = [item[1] for item in items]
print(prices)

expensive_items = [item for item in items if item[1] >= 8]
print(expensive_items)
#####################################################################################################
# zip function combines items in lists at the same indexes into an object of tuples

list1 = [1, 2, 3, 4]
list2 = [11, 22, 33, 44]

print(list(zip(list1, list2)))
print(list(zip("abcd", list1, list2)))

#####################################################################################################
# STACKS - LIFO

browsing_session = []
browsing_session.append(1)  # add items to stack
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)

browsing_session.pop()  # remove item on top of stack
print(browsing_session)

print(browsing_session[-1])  # accessing item on top of stack

# checking if stack is not empty and then accessing top most element
if not browsing_session:
    browsing_session[-1]

#####################################################################################################
# QUEUES - FIFO

# requires importing deque from collections,
# we apply deque to empty list so we can apply deque functions to it like popleft()
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)

# removes the first element from queue # requires importing deque from collections
queue.popleft()

if not queue:
    print("empty queue")

#####################################################################################################
# TUPLE is a read only list

tuple1 = (1, 2, 3)
tuple2 = 1, 2       # tuples can be defined without parenthesis as well
tuple3 = 1,         # if a tuple has only one item, it should be followed by a comma ","
tuple4 = ()         # empty tuple

print(type(tuple3))

print(tuple1 + tuple2)  # tuple concatenation

tuple1.count(1)  # returns the number of times an item exists in a tuple
tuple1.index(3)  # returns the indeax of a specified item in a tuple

print(tuple2[1])  # accessing items in a tuple
print(f"{tuple1[0:3]} hi")
print(str(tuple1[0:3]) + " yo")  # printing tuple along with a string

list = [1, 2, 3]
x = tuple(list)  # converting a list to a tuple

#####################################################################################################
# Swapping variables

x = 5
y = 10

x, y = y, x
print("x", x)
print("y", y)

#####################################################################################################
# ARRAYS contain data of a single type which is defined while initializing the array
# insesrting items that are not the same data type as defined will result in error
# we need to import array from array

numbers = array("i", [1, 2, 3])

# we can use same methods on arrays as on lists
numbers.append(4)
numbers.insert(3, 4)
numbers.remove(1)
numbers.pop()
numbers[2]  # accessing item in an array through index

#####################################################################################################
# SETS are a collection of items with no duplicates

repeated_number_list = [1, 2, 2, 3, 3, 3]
unique_set = set(repeated_number_list)
print(unique_set)

# sets are defined using curly braces
curly_set = {2, 5, 6}

# we can add and remove items from a set as well
curly_set.add(3)
curly_set.remove(5)
len(curly_set)  # to get the number of items in a set

# set operations
print(unique_set | curly_set)  # union of two sets
print(unique_set & curly_set)  # intersection of two sets
print(unique_set - curly_set)  # difference of two sets
print(unique_set ^ curly_set)  # symmetric difference of two sets

print(unique_set.union(curly_set))
print(unique_set.intersection(curly_set))
print(unique_set.difference(curly_set))

# sets are unorderd therefore we can not use indexing to access an item
# operations with sets mostly include one of the four mentioned above or to check if an item exists in a set
if 2 in curly_set:
    print("woohoo")

#####################################################################################################
# DICRIONARIES comprise of key, value pairs

dict_ex = {"x": 1, "y": 2}
dict_ex1 = dict(a=11, b=22)  # another way of defining a dictionary

dict_ex["z"] = 3  # adding key value pair to dictionary
dict_ex1["a"] = 10  # editing value assigned to a key

print(dict_ex)
print(dict_ex1["a"])  # items in dictionary need to be accessed through keys
print(dict_ex.items())  # returns key-value pairs in th form of tuples

# checking if a key exists in a dictionary
if "a" in dict_ex:
    print(dict_ex["a"])

# using get method to check if a key exists in a dictionary
print(dict_ex.get("a", 0))

# deleting key value pair from dictionary
del dict_ex["x"]

# looping over dictionary
for key in dict_ex:
    # the loop variable holds the key of an item, therefore we include dict_ex[key] in print statement
    print(key, dict_ex[key])

# this method prints key, value pairs as tuples
for x in dict_ex.items():
    print(x)

# we can also unpack the tuple and display key and value separately
for key, value in dict_ex.items():
    print(key, value)

# Dictionary Comprehension
values = {}
for x in range(5):
    values[x] = x*2

# the code below is the same as the one above but only needs one line to be written, Dictionary Comprehension
values = {x: x*2 for x in range(5)}
print(values)


#####################################################################################################
# GENERATOR OBJECTS are used when dealing with a really large data set or potentially an infinite stream
#  of data, as it does not store those values in memory
# from sys import getsizeof


# generator objects are created using parentheses
values1 = (x*2 for x in range(100000))
print("generator object size: ", getsizeof(values1))

# creating a list for the same purpose consumes much more memory
values2 = [x*2 for x in range(100000)]
print("list size:", getsizeof(values2))

# Since generator objects do not store all the items in memory, we can not calculate their lengths
# therefore using len() method on a generator object results in an error.
# We can only access items on a genarator onject when we iterate over it, therefore we can not know
# in advance how many items it contains.

#####################################################################################################
# UNPACKING OPERATOR helps to unpack a container, take out its individual elements and pass them as
# arbitrary arguments to a function

numbers = [1, 2, 3, 4]
print(*numbers)

# unpacking can be used in list creation as well
values = [*range(5), *"Hello"]
print(values)

# unpacking can be used to combine two or more lists into one
first = [1, 2, 3]
second = [4, 5, 6]
third = [*first, "hi", *second]

print(third)

# Unpacking dictionaries
first_dict = {"x": 10}
second_dict = {"x": 11, "y": 12}
# unpacking dictionaries requires using double asterisk **
third_dict = {**first_dict, **second_dict, "z": 15}
# if two dictionaries with same keys are combined, the last value of the key will be used, hence "x": 11
print(third_dict)

#####################################################################################################
# EXERCISE: Print the most repeated character in a string
# import collections

sentence = "This is a common interview question"
sentence = sentence.lower()
sentence = sentence.replace(" ", "", -1)

count_x = 0
highest_repeated = ""

# method 1
for x in sentence:
    if sentence.count(x) > count_x:
        count_x = sentence.count(x)
        highest_repeated = x

print("most repeated character:", highest_repeated)

# method 2
dict = {}

for x in sentence:
    dict[x] = sentence.count(x)


sorted_dict = sorted(dict.items(), key=lambda kv: kv[1], reverse=True)
print(sorted_dict)
print(sorted_dict[0])

#####################################################################################################
# EXCEPTIONS
# The code in the try block will always be run first, if there is no exception only then it goes to else block
# If there is an exception, code in the except block is run
# At the end the finally block will be run

try:
    age = int(input("Enter your age: "))
except:
    print("You did not enter a valid age")
else:
    print("This is only executed when there are no exceptions")

print("Code Execution Continues")

try:
    age = int(input("Enter your age: "))
except ValueError as ex:  # we can also specify exceptions and store it in a variable
    print("You did not enter a valid age")
    print(ex)
    print("Type: ", type(ex))

try:
    age = int(input("Enter your age: "))
    xfactor = 10 / age
# we can also specify multiple exceptions simultaneously
except (ValueError, ZeroDivisionError) as ex:
    print("You did not enter a valid age")
    print(ex)
    print("Type: ", type(ex))


try:
    file = open("practice.py")  # opening a file
    age = int(input("Enter your age: "))
    xfactor = 10 / age
except:
    print("You did not enter a valid age")
else:
    print("This is only executed when there are no exceptions")
# "finally" clause will always be executed at the end whether there is an exception or not, it is mostly used to release any external resources (files, network connections, DB connections etc.) that are being used
finally:
    file.close()  # closing the file that was previously opened


# "with" statement is used to automatocally release external resources
try:
    with open("practice.py") as file:  # when we open a file using a "with" statement python will automatically call the .close() function whether we have a "finally" clause or not
        print("File opened")
        # when an object supports enter and exit methods, it supports Context Management Protocol, which means we can use that object with the "with" statement
        # file.__enter__
        # file.__exit__  # python will automatically call the exit method to release external resources due to which we do not need a "finally" clause here
    age = int(input("Enter your age: "))
    xfactor = 10 / age
except:
    print("You did not enter a valid age")
else:
    print("This is only executed when there are no exceptions")

# using multiple external resources at the same time
try:
    with open("practice.py") as file, open("another.txt") as target:
        print("File opened")
except:
    print("You did not enter a valid age")


# Raising Exceptions
def x_factor(age):
    if age <= 0:
        # if an exception is reached, the remaining part of the code will not be executed
        raise ValueError("Age should be greater than zero")
    return 10 / age


try:
    x_factor(0)
except ValueError as error:
    print(error)

# Cost or Raising Exceptions
# from timeit import timeit

# The part of code for which we need to calculate time should be in comments
code1 = """
def x_factor(age):
    if age <= 0:
        raise ValueError("Age should be greater than zero")
    return 10 / age


try:
    x_factor(-1)
except ValueError as error:
    pass    # pass statement does not do anything, we use it because we can not have an empty except block
"""


code2 = """
def x_factor(age):
    if age <= 0:
        return None     # returning None instead of raising exception, None is an object that represents absence of a value
    return 10 / age



value = x_factor(-1)
if value == None:
    pass
"""

print("first code time", timeit(code1, number=10000))
print("second code time", timeit(code2, number=10000))
# Only raise exceptions when you really have to as it slows down the overall performance of the program
# If you can get by, by using if statements, do that instead

#####################################################################################################
# CLASSES are a bluebrint for creating new objects of that type
# OBJECTS are instances of a class


class Point:
    def draw(self):
        print("draw")


point = Point()  # initializing point object
point.draw()
print(type(point))
# to check if an object is an instance of a given class
print(isinstance(point, Point))


class Point1:

    # class attributes have the same values across all instances of a class
    default_color = "red"

    # methods defined in a class should have at least one parameter which by convention is "self"
    # defining constructor (magic method), which is executed when we create new object
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point {self.x}, {self.y}")

    # first parameter "cls" in the zero method is a reference to the class. By convention when defining a class method, we call its first parameter "cls"
    @classmethod  # declaration done to extend the behavior of this method
    def zero(cls):
        return cls(0, 0)  # this is exactly like calling Point1(0, 0)


# A class or an object bundles data (variables/attributes) and functions (methods) related to that data into one unit
# e.g. a human can have attributes like color, height, weight and functions like eat, walk, talk etc.
point1 = Point1(1, 2)  # initializing point1 object
point1.draw()

# since objects are dynamic, we can create attributes outside the class as well
point1.z = 10

# the attributes x, y and z are instance attributes since their values can vary depending on the instance they are being used by
point2 = Point(5, 6)
point2.z = 20

# we can read a class level attribute via a class reference or an object reference
print(point1.default_color)
print(Point1.default_color)

# we can also change value assigned to the class level attribute based on class level or attribute level
# attribute value changed only for this particular instance of Point1 class
point1.default_color = "blue"
# attribute value changed for all instcances of Point class
Point1.default_color = "yellow"

# Class methods can be used to create objects. They are also called factory methods since they are "creating" objects
# Here we do not need to pass parameters 0,0 to the zero method since we already defined the zero method with these parameters in the Point1 class
point3 = Point1.zero()
point3.draw()
