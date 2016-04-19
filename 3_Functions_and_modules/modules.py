#  Modules are pieces of code that other people have written to fulfill
# common tasks, such as generating random numbers, performing
# mathematical operations, etc.
#
# The basic way to use a module is to add "import module_name" at the
# top of your code, and then using module_name.var to access functions
# and values with the name var in the module.
#
# The following example uses the random module to generate random numbers.

import random

for i in range(5):
    value = random.randint(1, 6)
    print(value)

# The code uses the "randint" function defined in the "random" module
# to print 5 random numbers in the range 1 do 6.


# Another example of module usage
print("\n")
import math
num = 10
print(math.sqrt(num))

# There is another kind of import that can be used if you only need
# certain functions from a module
#
# These take the form "from module_name import var" and then var can
# be used as if it were define normally in your code.
#
# For example, to import only the "pi" constant from the math module:

from math import pi
print(pi)

# Use comma separated list to import multiple objects. For example:

print("\n")
from math import sqrt, pi

square_area = float(81)
square_side = math.sqrt(square_area)
print("Square area: " + str(square_area) + "\nSquare side: " + str(square_side))
print("-------------------------------")
circle_radius = float(5)
circle_area = pi * (circle_radius ** 2)
print("Circle radius: " + str(circle_radius) + "\nCircle area: " + str(circle_area))

# Trying to import a module that isn't available causes an importError

# import some_module <- code had to be commented

# You can import a module or object under a different name using
# the "as" keyword. This is mainly used when a module or object
# has a long or confusing name.

print("\n")
from math import sqrt as square_root
print(square_root(100)) 

# Exercise:
# What is the output of this code?

print("\n")
def func(x):
    res = 0
    for i in range(x):
        res += i
        # print(res)
    return res

print(func(4))

# Output: 6
