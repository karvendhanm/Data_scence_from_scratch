# Functional Tools

'''
when passing functions around, sometimes we'll want to partially apply(or curry)
functions to create a new functions. As a simple example, imagine that we have a
function of two variables.
'''
def exp(base, power):
    return base**power

'''
and we want to use it to create a function of one variable two_to_the whose input
is a power and whose output is the result of exp(2, power).
'''

# We can, of course, do this with def, but this can sometimes get unwieldy:
def two_to_the(power):
    return exp(2, power)

two_to_the(5)  # output: 32

# A different approach is to use functools.partial:

from functools import partial

def exp(base, power):
    return base ** power

exp(3, 5)

# we want functions like 2 to the power of, 3 to the power of, and 4 to the power of
two_to_the = partial(exp, 2)
three_to_the = partial(exp, 3)
four_to_the = partial(exp, 4)

print(type(two_to_the), two_to_the)

two_to_the(5)  # output 32
three_to_the(5)  # output 243
four_to_the(5)  # output 1024

# We can even use partial to fill in later arguments if you specify the name of the argument.
square_of = partial(exp, power = 2)
print(square_of(5))  # output 25

# We will also occasionally use map, reduce, and filter, which
# provide functional alternatives to list comprehensions.
from functools import partial
def double(x):
    return 2 * x

xs = [1, 2, 3, 4]
twice_xs = [double(x) for x in xs]
print(twice_xs)  # output: [2, 4, 6, 8]
twice_xs = map(double, xs)
print(list(twice_xs))  # output: [2, 4, 6, 8]
list_doubler = partial(map, double)
twice_xs = list_doubler(xs)
print(list(twice_xs))  # output: [2, 4, 6, 8]

# We can use map with multiple-argument functions if you provide multiple lists:
def multiply(x , y):
    return x*y

list(map(multiply, [4, 5, 0], [6, 7, 5]))  # output: [24, 35, 0]

# Just proof of concept unrelated to everything that came above and everything that comes below.
####
def mulitply_lists(x, y):
    return [ val1 * val2
    for val1 in x
    for val2 in y
    if x.index(val1) == y.index(val2)]

mulitply_lists([2,3,4], [4,5,6])  # output [8, 15, 24]
####

# Simliarly filter does the work of list comprehension if:
from functools import partial
xs = [1, 2, 3, 4]

def is_even(x):
    return x % 2 == 0

x_evens = [x for x in xs if is_even(x)]
print(x_evens)  # output [2, 4]
x_evens = filter(is_even, xs)
print(list(x_evens))  # output [2, 4]
# partial takes a function and its first argument
list_evener = partial(filter, is_even)
list_evener = list(list_evener(xs))
print(list_evener) # output [2, 4]

# reduce
# reduce combines the first two elements of a list, then the result with the third,
# that result with the fourth and so on, producing a single result
xs = [1, 2, 3, 4]

def multiply(x , y):
    return x*y

from functools import reduce, partial
x_product = reduce(multiply, xs)  # output: 24
list_product = partial(reduce, multiply)
list_product(xs)  # output: 24

# Enumerate
# Sometimes you will want to iterate over a list and use both its elements and their indexes.

documents = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. " \
           "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, " \
           "when an unknown printer took a galley of type and scrambled it to make a type specimen book. " \
           "It has survived not only five centuries, but also the leap into electronic typesetting, " \
           "remaining essentially unchanged. It was popularised in the 1960s with the release of " \
           "Letraset sheets containing Lorem Ipsum passages, and more recently with desktop " \
           "publishing software like Aldus PageMaker including versions of Lorem Ipsum."

# any other means of getting an index other than using enumerate is not pythonic.
for i, document in enumerate(documents):
    print(i, document)


# zip and Argument Unpacking
'''
often we will need to zip two or more lists together. zip transforms
multiple lists into a single list of tuples of corresponding elements.
'''

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
print(list(zip(list1, list2)))  # output: [('a', 1), ('b', 2), ('c', 3)]

# If the lists are different lengths, zip stops as soon as the first list ends
list1 = ["a", "b", "c", "d"]
list2 = [1, 2, 3]
print(list(zip(list1, list2)))  # output: [('a', 1), ('b', 2), ('c', 3)] (zip stopped with the shortest list)

# We can also "unzip" a list using a strange trick
pairs = [('a', 1), ('b', 2), ('c', 3)]
# the asterisk performs argument unpacking.
letters, numbers = zip(*pairs)
print(letters, numbers)  # output: ('a', 'b', 'c') (1, 2, 3)

# We can use argument unpacking with any function.
def add(a, b):
    return a + b

add(5, 6)  # output: 11
add(*[5,6])  # output: 11
# add([5,6 ])  # TypeError

# args and kwargs
# this type of function is called higher-order function
def doubler(f):
    def g(x):
        return 2 * f(x)
    return g

def f1(x):
    return x + 1

g = doubler(f1)
print(g(3))  # output: 8
print(g(-1))  # output: 0

def f2(x, y):
    return x + y

g = doubler(f2)
# print(g(1, 2))  # output: TypeError: g() takes 1 positional argument but 2 were given

# What we need is a way to specify a function that takes arbitrary arguments. We can
# do this with argument unpacking and a little bit of magic

def magic(*args, **kwargs):
    print("unamed args", args)
    print("keyword args", kwargs)

magic(1, 2, key="word", keys="word2")
'''
output
------
unamed args (1, 2)
keyword args {'key': 'word', 'keys': 'word2'}
'''
magic(1, 2, 3, 4, 5, Name="John Doe", Age=30, Gender="M")
'''
output
------
unamed args (1, 2, 3, 4, 5)
keyword args {'Name': 'John Doe', 'Age': 30, 'Gender': 'M'}
'''

def other_way_magic(x, y, z):
    return x + y + z

x_y_list = [3, 4]
z_dict = {"z":2}

other_way_magic(*x_y_list, **z_dict)

# higher order functions that takes varying number of arguments
def doubler_correct(f):
    # works no matter what kind of input function f expects
    def g(*args, **kwargs):
        return 2 * f(*args, **kwargs)
    return g

def f2(x, y, z, **kv):
    return x + y + z + sum(kv.values())

g = doubler_correct(f2)
print(g(3, 4, 5, key1=2, key2 = 6))










































