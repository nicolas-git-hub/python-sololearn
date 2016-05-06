# Functional programming is a style of programming that (as the name suggests) is
# based around functions.
# A key part of functional programming is higher-order functions. We have seen this idea
# briefly in the previous lesson on functions as objects.
# Higher-order functions take other functions as arguments, or return them as results.
#
# Example:

def apply_twice(func, arg):
    return func(func(arg))

def add_five(x):
    return x + 5

print(apply_twice(add_five, 10))


# The function apply_twice takes another function as its argument and calls it twice inside its body.

#
# Pure functions
#
# Functional programming seeks to use pure functions.
# Pure functions have no side effects, and return a value that depends only on their arguments.
# This is how functions in math work: for example, the cos(x) will, for the same value of x, always
# return the same result.
# Below are examples of pure and impure functions.
#
# Pure functions:
#

def pure_function(x, y):
    temp = x + 2 * y
    return temp / (2 * x + y)

#
# Impure function:
#

some_list = []

def impure(arg)
    some_list.append(arg)

#
# The function above is not pure, because it changed the state of some_list
