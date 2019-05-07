# A crash course in Python

import this  # Zen of Python

# Whitespace Formatting

for i in [1, 2, 3, 4, 5]:
    print(i)
    for j in [1, 2, 3, 4, 5]:
        print(j)
        print(i + j)
    print(i)
print('done looping')

# using backslash to denote that the statement continues onto the next line.
two_plus_three = 2 + \
                 3
print(two_plus_three)

# Modules

import re
my_regex = re.compile("[0-9]+", re.I)
print(type(my_regex))

# If you already have an "re" we can use an alias.
import re as regex
my_regex = regex.compile("[0-9]+", regex.I)

# these functions/values can be used without qualifications
from collections import defaultdict, Counter
lookup = defaultdict(int)
my_counter = Counter()

match = 10
from re import *
print(match)

# Functions
# Python functions are first class. So a function can be
# assigned to a variable.

# Example
def double(x):
    return 2*x

# function has been assigned to a variable
my_double = double

# now the above variable can be used to call the function
my_double(14)  # ans: 28

# we can even pass a function, another function as a parameter
def apply_to_one(function, value):
    '''

    :param function: a function which takes value as a parameter
    :param value:
    :return:
    '''
    return function(value)

apply_to_one(my_double, 14)  # ans: 28


# It is also easy to create short anonymous function called lambda
apply_to_one(lambda x: x*2, 14)  # ans: 28
apply_to_one(lambda x: x**2, 14)  # ans: 196

# Even we can assign lambdas to variables. But it is not recommended
another_double = lambda x: x*2  # don't do this
another_double(12)  # ans: 24

# Functions can even have default parameters.
def my_print(message = "my default message"):
    print(message)

my_print("Hello world")
my_print()

# It is sometimes useful to specify arguments by name
def subtract(a = 0, b = 0):
    return a - b

subtract(5, 4)
subtract(0, 5)
subtract(b = 5)

# Strings
#backslash is used to encode special characters
tab_string = "\t"
print(tab_string)
print(len(tab_string))

# we can create raw strings in python using r""
not_tab_string = r"\t"
print(not_tab_string)
print(len(not_tab_string))

# if raw string symbol r"" is not used, another backslash needs to be used
raw_string_not_used = "\\t"
print(raw_string_not_used)
print(len(raw_string_not_used))

# We can create multiline strings using triple-double-quotes
mutli_line_string = """This is the first line
and this is the second line
and this is the third line
"""

mutli_line_string_single = '''This is the first line
and this is the second line
and this is the third line
'''

print(mutli_line_string)
print(mutli_line_string_single)

# Exceptions
try:
    print(0/0)
except ZeroDivisionError:
    print("cannot divide by zero")
























