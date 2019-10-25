import math

print("hello world!")

x = 1
y = x+5
print(y*5)

y = True
print(y)

name = "Aftab \n Lateef"
print(name)
len_name = len(name)
print(len_name)
print(name[0:5])

first = "Aftab"
last = "Lateef"

# formatted strings
print(f"{first} {last}")
print(f"{len(first)} {5+5}")

print(name.upper())

# strip method
strip_example_var = " hi hello hi "
print(strip_example_var.strip())
print(strip_example_var.lstrip())
print(strip_example_var.rstrip())

# find method
print(name.find("e"))  # returns index of character or characters in string
print(name.find("atee"))

# replace method
print(strip_example_var.replace("h", "p", 2))  # the third argument is count
print(strip_example_var.replace("l", "j"))

# in operator
# returns boolean depending on expression found or not
print("hi" in strip_example_var)
print("ho" in strip_example_var)

# not in operator
print("ho" not in strip_example_var)

str_var = "abcd"
int_var = 1234
bool_var = True
float_var = 1.111

# referencing in print statement
print("%s and %i and %s and %f" % (str_var, int_var, bool_var, float_var))


# augmented assignment
x += 5

# division result as integer instead of float
print(5//3)

# representing complex numbers with "j" as the imaginary part
y = 2 + 3j

# methods used on numbers
print(round(3.6))
print(abs(-1.5))  # returns absolute value
print(math.ceil(2.2))
print(math.floor(2.7))
