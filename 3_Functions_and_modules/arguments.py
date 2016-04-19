# Most functions take arguments.
# The example bellow defines a function that takes one argument.

def print_with_exclamation(word):
    print(word + "!")

print_with_exclamation("spam")
print_with_exclamation("eggs")
print_with_exclamation("Python")

# Another function with one argument

print("\n")

def print_double(x):
    print(2 * x)

print_double(3)

# You can also define functions with more than one argument;
# separate them with commas.

print("\n")

def print_sum_twice(x, y):
    print(x + y)
    print(x + y)

print_sum_twice(5, 8)

# Function arguments can be used as variables inside the function definition.
# However, they cannot be referenced outside of the function's definition.
# This also applies to other variables created inside a function.

print("\n")

def function(variable):
    variable += 1
    print(variable)

function(7)

# print(variable)

# The above call doesn't work and had to be commented in order to
# the rest of the code to work.

# Technically, parameters are the variables in a function definition,
# and arguments are the values put into parameters when fucntions are called.

# Exercise: Fill the blanks to define a function that prints "Yes", if its
# parameter is an even number, and "No" otherwise.

print("\n")

def even(x):
    if x % 2 == 0:
        print("Yes, " + str(x) + " is even.")
    else:
        print("No, " + str(x) + " is not even.")

even(0)
even(1)
even(2)
even(573)
