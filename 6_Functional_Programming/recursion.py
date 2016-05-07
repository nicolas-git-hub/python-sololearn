# Recursion is a very important concept in functional programming.
# The funcdamental part of recursion is self-reference - function calling themselves.
# It is used to solve problems that can be broken up into easier sub-problems of the same type.
#
# A classic example of a function that is implemented recursively is the factorial function, which
# finds the product of all positive integers below a specific number.
#
# For example, 5! (5 factorial) is 5 * 4 * 3 * 2 * 1 (120).
#
# To implement this recursively, notice that 5! = 5 * 4!, 4! = 4 * 3!, 3! = 3 * 2!, and so on.
# Generaly, n! = n * (n-1)! .
#
# Futhermore, 1! = 1. This is known as the base case, as it can be calculated without performing any
# any more factorials.
# Below is a recursive implementation of the factorial function.

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)

print(factorial(5))


# The base case acts as the exit condition of the recursion.


# Recursive functions can be infinite, just like infinite while loops.
# These often occur when you forget to implement the base case.
# Below is an incorrect version of the factorial function.
# It has no base case, so it runs until the interpreter runs out of memory an crashes.

# def my_factorial(x):                    # Block commented so the rest of the script could run.
#     return x * my_factorial(x - 1)

# print(my_factorial(5))


#
# Recursion can also be indirect.
# One function can call a second, which calls the first, which calls the second, and so on.
# This occur with any number of functions.
#
# Example:

def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x - 1)

def is_odd(x):
    return not is_even(x)

print(is_odd(17))
print(is_even(23))
