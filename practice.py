from collections import deque
import math
import datetime
import calendar
from datetime import date
from sys import getsizeof
import collections
from timeit import timeit
import random

"""
my_file = open("/home/aftab/Desktop/BLE_Test.txt")
print(my_file.read())
my_file.close()


# mode = "r" is to read content of file, "w" is to overwrite, "a" is to append to existing data in file
with open("/home/aftab/Desktop/BLE_Test.txt", mode="r") as my_file:
    print(my_file.read())

with open("/home/aftab/Desktop/BLE_Test.txt", mode="a") as my_file:
    my_file.write("\n hello man")
"""


"""
list1 = [1, 2, 3]
list2 = [11, 22, 33, 44]

print(list(zip(list1, list2)))
print(list(zip("abcde", list1, list2)))

string = "abcdef"  # a string is iterable
number_list = [1, 2, 3, 4, 5, 6]  # a list is also iterable


def temp(**user):
    print(user["name"])
    print(user["age"])
    print(user["profession"])


temp(name="Aftab", age=30, profession="Engineer")

num_range = list(range(5))
print(num_range)

first = "Aftab"
last = "Lateef"

print(f"My first name is {first} and last name is {last}")

# template strings

self_introduction = "Hello, my first name is {} and last name is {}"  # defining template
# using defined template and passing values
with_names = self_introduction.format("Aftab", "Lateef")
print(with_names)
"""


for i in range(256):
    hex_from_i = str(hex(i))
    hex_replaced = hex_from_i.replace("0", "\\", 1)
    if len(hex_replaced) == 3:
        hex_replaced_again = hex_replaced.replace("\\x", "\\x0")
        print(hex_replaced_again, end="")
    else:
        print(hex_replaced, end="")
