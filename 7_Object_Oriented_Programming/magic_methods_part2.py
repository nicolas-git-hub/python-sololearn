# More magic methods for common operators:
#
# __sub__ for -
# __mul__ for *
# __truediv__ for /
# __floordiv__ for //
# __mod__ for %
# __pow__ for **
# __and__ for &
# __xor__ for ^
# __or__ for |
#
#
# The expression x + y is translated into x.__add__(y).
#
# However, if x hasn't implemented __add__, and x and y are different types, then y.__add(x) is called.
#
# There are equivalent r methods for all magic methods methods just mentioned.
#
# Example:

class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __truediv__(self, other):
        line = '=' * len(other.cont)
        return '\n'.join([self.cont, line, other.cont])

spam = SpecialString('spam')
hello = SpecialString('Hello World!')
print(spam / hello)


# In the example above, we defined the division operation for our class SpecialString.
