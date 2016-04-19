# Exceptions occour when something goes wrong, due to incorrect code or input.
# When an exception occors, the program immediately stops.
# The following code produces the ZeroDivisionError exception by trynig to
# divide 7 by 0.

num1 = 7
num2 = 0
print(num1 / num2)

# Different execptions are raised for different reasons.
#
# Common exceptions:
# ImportError:  an import fails;
# IndexError: a list is indexed with an out-of-range number;
# NameError: an unknown variable is used;
# SyntaxError: the code can't be parsed properly;
# TypeError: a function is called on a value of an inappropriate type;
# ValueError: a function is called on a value of the correct type, but
# with an inappropriate value

# Python has several others built-in exceptions, such as
# ZeroDivisionError and OSError.
# Third-party libraries also often define their own exceptions.
