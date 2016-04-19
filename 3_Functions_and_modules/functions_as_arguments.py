# Functions can also be used as arguments of other functions

def add(x, y):
    return x + y

def do_twice(func, x, y):
    return func(func(x, y), func(x, y))

a = 5
b = 10

print(do_twice(add, a, b))

# Observation: from now on extended comments will be written with #
# As you can see, the function do _twice takes a function as its
# argument and calls it in its body
